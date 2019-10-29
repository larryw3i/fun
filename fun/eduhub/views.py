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


class ArticleListView( ListView ):
    model = Article
    context_object_name = 'Articles'   
    template_name = EduhubConfig.name + '/list.html'    
    paginate_by = 5



class ArticleCreateView(CreateView):
    model = Article
    template_name =EduhubConfig.name + '/create.html'
    fields = ['title', 'document_file',]
    success_url ='/'+ EduhubConfig.name + '/list'   
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)



class ArticleUpdateView(UpdateView):
    model = Article
    template_name =EduhubConfig.name + '/update.html'
    fields = ['title', 'document_file',]

    def form_valid(self, form):
        form.author = self.request.user
        return super(ArticleUpdateView, self).form_valid(form)