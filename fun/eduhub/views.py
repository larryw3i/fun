
from django.shortcuts import render, reverse
from .modelforms import LabelModelForm
from .apps import EduhubConfig
from .models import Label
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.shortcuts import render, reverse, redirect
from django.utils.translation import gettext_lazy as _
from hurry import filesize
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.http import Http404

# Create your views here.

max_cover_size = 500*1024

label_create_template = f'{EduhubConfig.name}/label_create.html'
label_delete_template = f'{EduhubConfig.name}/label_delete.html'
label_update_template = f'{EduhubConfig.name}/label_update.html'
label_list_template =   f'{EduhubConfig.name}/label_list.html'

'''generic_view'''

class LabelCreateView( CreateView, LoginRequiredMixin ):
    model = Label
    form_class = LabelModelForm
    template_name = label_create_template
    # fields = ['name', 'cover', 'comment']
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
    # fields = ['name', 'cover', 'comment']
    success_url = reverse_lazy('eduhub:label_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        print(form)
        return form

    def get_object(self, queryset=None):
        label = super().get_object(queryset=queryset)
        if self.request.user != label.author:
            return Http404()

        return label
        

'''end_generic_view'''


def label_list(self, request):
    pass

def label_create( request):
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        labelform = LabelModelForm()
        return render(request, label_create_template, context= {'labelform':labelform})
        
    pass

def label_update(self, request, pk):
    pass

def label_delete(self, request, pk):
    pass