import math
import os
from datetime import datetime

import bleach
import magic
import pytz
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import paginator
from django.core.exceptions import ValidationError
from django.core.paginator import InvalidPage
from django.db.models import F, Q
from django.http import Http404
from django.shortcuts import (Http404, HttpResponseRedirect, redirect, render,
                              reverse)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from hurry import filesize

from fun import funvalue, settings
from fun.fundef import default_bleach_clean

from .apps import EduhubConfig
from .modelforms import ContentModelForm, FuncontentModelForm, LabelModelForm
from .models import (Content, Funclassification, Funcontent, Label,
                     content_name, funcontent_name, label_name)

# Create your views here.

max_cover_size = 500*1024

max_pdf_content_file_size = 5 * math.pow(1024, 2)
max_video_content_file_size = 100 * math.pow(1024, 2)

label_create_template   = f'{EduhubConfig.name}/{label_name}{funvalue.create_html}'
label_detail_template   = f'{EduhubConfig.name}/{label_name}{funvalue.detail_html}'
label_delete_template   = f'{EduhubConfig.name}/{label_name}{funvalue.delete_html}'
label_update_template   = f'{EduhubConfig.name}/{label_name}{funvalue.update_html}'
label_list_template     = f'{EduhubConfig.name}/{label_name}{funvalue.list_html}'

content_create_template = f'{EduhubConfig.name}/{content_name}{funvalue.create_html}'
content_detail_template = f'{EduhubConfig.name}/{content_name}{funvalue.detail_html}'
content_delete_template = f'{EduhubConfig.name}/{content_name}{funvalue.delete_html}'
content_update_template = f'{EduhubConfig.name}/{content_name}{funvalue.update_html}'
content_list_template   = f'{EduhubConfig.name}/{content_name}{funvalue.list_html}'

funcontent_create_template = f'{EduhubConfig.name}/{funcontent_name}{funvalue.create_html}'
funcontent_detail_template = f'{EduhubConfig.name}/{funcontent_name}{funvalue.detail_html}'
funcontent_delete_template = f'{EduhubConfig.name}/{funcontent_name}{funvalue.delete_html}'
funcontent_update_template = f'{EduhubConfig.name}/{funcontent_name}{funvalue.update_html}'
funcontent_list_template   = f'{EduhubConfig.name}/{funcontent_name}{funvalue.list_html}'


class LabelCreateView( LoginRequiredMixin, CreateView ):
    model = Label
    form_class = LabelModelForm
    template_name = label_create_template
    success_url = reverse_lazy('eduhub:label_list')

    def form_valid(self, form):

        if not form.instance.cover.file:
            form.add_error('cover',  _('Cover image is required'))
            return render(self.request, label_create_template, context={'form': form})

        if not str(form.instance.cover.file.content_type).startswith('image/'):
            form.add_error('cover',  _('Image allowed only'))
            return render(self.request, label_create_template, context={'form': form})

        if form.instance.cover.file.size > max_cover_size:
            form.add_error('cover',  _(
                'The length of cover should be less than')+' '+filesize.size(max_cover_size))
            return render(self.request, label_create_template, context={'form': form})

        form.instance.author = self.request.user

        return super().form_valid(form)


class LabelListView( ListView ):
    model = Label

    form_class = LabelModelForm
    template_name = label_list_template
    context_object_name = 'labels'
    ordering = ['-creating_date', ]
    paginate_by = 5
    paginate_orphans = 1

    def paginate_queryset(self, queryset, page_size):

        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(_("Page is not 'last', nor can it be converted to an int."))
        try:
            page = paginator.page(page_number)
            return (paginator, page, page.object_list, page.has_other_pages())
        except InvalidPage as e:
            page = paginator.page(1)
            return (paginator, page, page.object_list, page.has_other_pages())

    def get_queryset(self):
        if ( not self.request.user.is_authenticated )  or self.request.COOKIES.get('is_label_list_mine', False):
            return  Label.objects.filter( is_legal = True )
        else:
            return Label.objects.filter( is_legal = True,  author = self.request.user)  # super().get_queryset()

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response.set_cookie('page', self.request.GET.get('page', 1))
        return response

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs) 
        return context_data
    


class LabelDeleteView( LoginRequiredMixin, DeleteView ):
    model = Label
    form_class = LabelModelForm
    template_name = label_delete_template
    context_object_name = 'label'
    success_url = reverse_lazy('eduhub:label_list')

    def post(self, request, *args, **kwargs):

        if not Label.objects.filter(pk=kwargs['pk'], author=request.user).exists():
            raise Http404()

        return super().post(request, *args, **kwargs)


class LabelUpdateView( LoginRequiredMixin, UpdateView ):

    model = Label
    form_class = LabelModelForm
    template_name = label_update_template
    context_object_name = 'label'

    def get_success_url(self):
        return '/eduhub/label_list?page='+self.request.COOKIES.get( 'page' , 1 )

    def post(self, request, *args, **kwargs):
        if not Label.objects.filter(pk=kwargs['pk'], author=request.user).exists():
            raise Http404()

        return super().post(request, *args, **kwargs)


class ContentListView( ListView ):

    model = Content

    form_class = ContentModelForm
    template_name = content_list_template
    context_object_name = 'contents'
    ordering = ['-uploading_date', ]
    paginate_by = 5
    paginate_orphans = 1

    def get_queryset(self):
        return Content.objects.filter(label=self.kwargs['label'], is_legal=True).order_by('-uploading_date')

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response.set_cookie('page', self.request.GET.get('page', 1))
        return response

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['label'] = self.kwargs['label']
        context_data['is_author'] = Label.objects.get( pk = self.kwargs['label'] ).author == self.request.user
        return context_data


class ContentCreateView( LoginRequiredMixin,  CreateView ):
    model = Content
    form_class = ContentModelForm
    template_name = content_create_template

    def __init__(self):
        self.label_id = None
        super().__init__()

    def get_success_url(self):
        return reverse('eduhub:content_list', kwargs={'label': self.label_id})

    def get_initial(self):
        initial = super().get_initial()
        initial['label'] = self.kwargs['label']
        return initial

    def form_valid(self, form):
 
        headmost_five = Content.objects.filter( label__author = self.request.user ).order_by('-uploading_date')[:5]

        if len( headmost_five ) > 4 and (  datetime.now(pytz.timezone('UTC'))   - headmost_five[4].uploading_date ).total_seconds()/3600 < 2.8  :
            form.add_error('content_file',  _('Frequently request')+" !")
            return render(self.request, content_create_template, context={'form': form})

        if  not form.instance.content_file :
            form.add_error('content_file',  _('Content file is required')+" !")
            return render(self.request, content_create_template, context={'form': form})

        content_file = form.instance.content_file.file
        
        if not content_file:
            form.add_error('content_file',  _('Content file is required'))
            return render(self.request, content_create_template, context={'form': form})

        if str(content_file.content_type).startswith('video/') and content_file.size > max_video_content_file_size:
            form.add_error('content_file',  _(
                'The length of video file should be less than')+' '+filesize.size(max_video_content_file_size))
            return render(self.request, content_create_template, context={'form': form})

        if str(content_file.content_type).endswith('/pdf') and content_file.size > max_pdf_content_file_size:
            form.add_error('content_file',  _(
                'The length of pdf file should be less than')+' '+filesize.size(max_pdf_content_file_size))
            return render(self.request, content_create_template, context={'form': form})
        self.label_id = form.instance.label.id
        form.instance.author = self.request.user

        return super().form_valid(form)


class ContentDetailView( DetailView ):

    model = Content
    form_class = ContentModelForm
    template_name = content_detail_template

    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)
        file_path = os.path.join(settings.MEDIA_ROOT, str( context_data['object'].content_file.name ))
        context_data['is_video'] = str( magic.from_file( file_path ,mime=True) ).startswith('video/')
        return context_data

 
class ContentDeleteView( LoginRequiredMixin,  DeleteView ):

    model = Content
    form_class = ContentModelForm
    template_name = content_delete_template

    def __init__(self):
        self.label_id = None
        super().__init__()

    def post(self, request, *args, **kwargs):

        if not Content.objects.filter(pk=kwargs['pk'], label__author=request.user).exists():
            raise Http404()

        self.label_id = Content.objects.get(pk=kwargs['pk']).label.id
        return super().post(request, *args, **kwargs)
 
    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)
        file_path = os.path.join(settings.MEDIA_ROOT, str( context_data['object'].content_file.name ))
        context_data['is_video'] = str( magic.from_file( file_path ,mime=True) ).startswith('video/')
        return context_data

    def get_success_url(self):
        return reverse('eduhub:content_list', kwargs={'label': self.label_id})


class ContentUpdateView( LoginRequiredMixin,  UpdateView ):

    model = Content
    form_class = ContentModelForm
    template_name = content_update_template

    def __init__(self):
        self.label_id = None
        super().__init__()

    def post(self, request, *args, **kwargs):

        if not Content.objects.filter(pk=kwargs['pk'], label__author=request.user).exists():
            raise Http404()

        self.label_id = Content.objects.get(pk=kwargs['pk']).label.id
        return super().post(request, *args, **kwargs)
 

    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)
        file_path = os.path.join(settings.MEDIA_ROOT, str( context_data['object'].content_file.name ))
        context_data['is_video'] = str( magic.from_file( file_path ,mime=True) ).startswith('video/')
        return context_data

    def get_success_url(self):
        return reverse('eduhub:content_list', kwargs={'label': self.label_id})



#############


class FuncontentListView( ListView ):
    model = Funcontent
    form_class = FuncontentModelForm
    template_name = funcontent_list_template
    context_object_name = 'funcontents'
    ordering = ['-uploading_date', ]
    paginate_by = 5
    paginate_orphans = 1

    def get_queryset(self):
        return Funcontent.objects.filter(label=self.kwargs['label'], is_legal=True).order_by('-uploading_date')

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response.set_cookie('page', self.request.GET.get('page', 1))
        return response

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['label'] = self.kwargs['label']
        context_data['is_author'] = Label.objects.get( pk = self.kwargs['label'] ).author == self.request.user
        return context_data


class FuncontentCreateView( LoginRequiredMixin,  CreateView ):
    model = Funcontent
    form_class = FuncontentModelForm
    template_name = funcontent_create_template

    def __init__(self):
        self.label_id = None
        self.fields['classification'].queryset = Funclassification.objects.filter( level = 1 )
        super().__init__()

    def get_initial(self):
        initial = super().get_initial()
        initial['label'] = self.kwargs['label']
        return initial

    def form_valid(self, form):
 
        headmost_five = Content.objects.filter( label__author = self.request.user ).order_by('-uploading_date')[:5]

        if len( headmost_five ) > 4 and (  datetime.now(pytz.timezone('UTC'))   - headmost_five[4].uploading_date ).total_seconds()/3600 < 2.8  :
            form.add_error('content',  _('Frequently request')+" !")
            return render(self.request, content_create_template, context={'form': form})

        form.instance.content = default_bleach_clean( form.instance.content )
        self.label_id = form.instance.label.id
        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('eduhub:funcontent_list', kwargs={'label': self.label_id})


class FuncontentDetailView( DetailView ):

    model = Funcontent
    form_class = FuncontentModelForm
    template_name = funcontent_detail_template

 
class FuncontentDeleteView( LoginRequiredMixin,  DeleteView ):

    model = Funcontent
    form_class = FuncontentModelForm
    template_name = funcontent_delete_template

    def __init__(self):
        self.label_id = None
        super().__init__()

    def post(self, request, *args, **kwargs):

        if not Funcontent.objects.filter(pk=kwargs['pk'], label__author=request.user).exists():
            raise Http404()

        self.label_id = Funcontent.objects.get(pk=kwargs['pk']).label.id
        return super().post(request, *args, **kwargs)
 
    def get_success_url(self):
        return reverse('eduhub:content_list', kwargs={'label': self.label_id})


class FuncontentUpdateView( LoginRequiredMixin,  UpdateView ):

    model = Funcontent
    form_class = FuncontentModelForm
    template_name = funcontent_update_template

    def __init__(self):
        self.label_id = None
        super().__init__()

    def post(self, request, *args, **kwargs):

        if not Funcontent.objects.filter(pk=kwargs['pk'], label__author=request.user).exists():
            raise Http404()

        self.label_id = Funcontent.objects.get(pk=kwargs['pk']).label.id
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.content = default_bleach_clean( form.instance.content )
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('eduhub:funcontent_list', kwargs={'label': self.label_id})
