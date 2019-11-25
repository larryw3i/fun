
# Create your views here.

import math
import os

import magic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import paginator
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import (Http404, HttpResponseRedirect, redirect, render,
                              reverse)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from hurry import filesize

from fun import settings, funvalue
from .models import Funuser, funuser_mame
from .modelforms import FunuserModelForm
from .apps import FunuserConfig

from django.core.files import File


funuser_create_template   = f'{FunuserConfig.name}/{funuser_mame}{funvalue.create_html}'
funuser_detail_template   = f'{FunuserConfig.name}/{funuser_mame}{funvalue.detail_html}'
funuser_delete_template   = f'{FunuserConfig.name}/{funuser_mame}{funvalue.delete_html}'
funuser_update_template   = f'{FunuserConfig.name}/{funuser_mame}{funvalue.update_html}'
funuser_list_template     = f'{FunuserConfig.name}/{funuser_mame}{funvalue.list_html}'


class FunuserUpdateView( LoginRequiredMixin, UpdateView ):
 
    model = Funuser
    form_class = FunuserModelForm
    template_name = funuser_update_template
    success_url = reverse_lazy('funuser:funuser_update' )
    

    def get_object(self, queryset=None):    
        default_avatar_file_path = os.path.join(  settings.STATIC_ROOT, 'images', 'x_dove.webp' )  
        is_funuser_created =  Funuser.objects.filter( user = self.request.user ).exists()
        return Funuser.objects.get( user = self.request.user  ) if is_funuser_created  else Funuser(  )  # super().get_object(queryset=queryset)
     
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class FunuserDetailView( LoginRequiredMixin, DetailView ):
    
    model = Funuser
    form_class = FunuserModelForm
    template_name = funuser_update_template
    