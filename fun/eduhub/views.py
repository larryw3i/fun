
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import (Http404, HttpResponseRedirect, redirect, render,
                              reverse)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from hurry import filesize

from .apps import EduhubConfig
from .modelforms import LabelModelForm
from .models import Label
from django.core import paginator

# Create your views here.

max_cover_size = 500*1024

label_create_template = f'{EduhubConfig.name}/label_create.html'
label_detail_template = f'{EduhubConfig.name}/label_detail.html'
label_delete_template = f'{EduhubConfig.name}/label_delete.html'
label_update_template = f'{EduhubConfig.name}/label_update.html'
label_list_template =   f'{EduhubConfig.name}/label_list.html'


class LabelCreateView( CreateView, LoginRequiredMixin ):
    model = Label
    form_class = LabelModelForm
    template_name = label_create_template
    success_url = reverse_lazy('eduhub:label_list')


    def form_valid(self, form):
        
        if not str(form.instance.cover.file.content_type).startswith('image/') :
            form.add_error('cover',  _('Image allowed only') )
            return render(self.request, label_create_template, context={ 'form': form })

        
        if form.instance.cover.file.size > max_cover_size :
            form.add_error('cover',  _('The length of cover should be less than')+' '+filesize.size(max_cover_size) )
            return render(self.request, label_create_template, context={ 'form': form })

        form.instance.author = self.request.user
        return super().form_valid(form)



class LabelListView( ListView ):
    model = Label

    form_class = LabelModelForm
    template_name = label_list_template
    context_object_name = 'labels'
    ordering =  ('-creating_date', )
    paginate_by = 1
    paginate_orphans= 1

    def get(self, request, *args, **kwargs):
        request.COOKIES['page'] = request.GET.get('page')
        return super().get(request, *args, **kwargs)
    def  render_to_response(self, context, **response_kwargs):
        response =  super().render_to_response(context, **response_kwargs)
        response.set_cookie('page', self.request.GET.get('page', 1) )
        return response
 
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['max_left_item_count'] = 2
        return context_data


class LabelDeleteView( DeleteView,  LoginRequiredMixin ):
    model = Label
    form_class = LabelModelForm
    template_name =label_delete_template
    context_object_name = 'label'
    success_url = reverse_lazy('eduhub:label_list')
    
    def get_object(self, queryset=None):
        label = super().get_object(queryset=queryset)

        if self.request.user != label.author:
            return Http404()

        return label
        

class LabelUpdateView( UpdateView, LoginRequiredMixin ):

    model = Label
    form_class = LabelModelForm
    template_name = label_update_template
    context_object_name = 'label' 

    def get_success_url(self):
        return '/eduhub/label_list?page='+self.request.COOKIES['page']

    def get_object(self, queryset=None):
        label = super().get_object(queryset=queryset)
        if self.request.user != label.author:
            return Http404()

        return label
        

'''end_generic_view'''
