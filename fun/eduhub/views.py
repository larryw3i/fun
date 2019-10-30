from django.shortcuts import render

# Create your views here.

from django import forms

from django.views.generic import *

from .models import *

from .apps import EduhubConfig

from django.contrib.auth.mixins import LoginRequiredMixin 

from django.shortcuts import *

from django.core.paginator import Paginator
from django.db.models import *
import magic 
from django.utils.translation import gettext as _t

from django.core import validators
from django.core.exceptions import ValidationError


class ArticleListView( ListView ):
    model = Article
    context_object_name = 'Articles'   
    template_name = EduhubConfig.name + '/list.html'    
    paginate_by = 5



class ArticleCreateView( CreateView ):
    model = Article
    template_name =EduhubConfig.name + '/create.html'
    fields = ['title', 'media_file',]
    success_url ='/'+ EduhubConfig.name + '/list'   

    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super(ArticleCreateView, self).form_valid(form)



class ArticleUpdateView( UpdateView ):
    model = Article
    template_name =EduhubConfig.name + '/update.html'
    fields = ['title', 'media_file',]
    
    def form_valid(self, form):
        if form.instance.author != self.request.user:
            return Http404('nice try')
        return super(ArticleCreateView, self).form_valid(form)



class ArticleDeleteView( DeleteView ):
    model = Article
    template_name =EduhubConfig.name + '/delete.html'
    fields = ['title', 'media_file',]
    success_url ='/'+ EduhubConfig.name + '/list'   

class ArticleDetailView( DetailView ):
    model = Article

    template_name =EduhubConfig.name + '/detail.html'
    fields = ['title', 'media_file',]
    pk_url_kwarg = 'id'
        


