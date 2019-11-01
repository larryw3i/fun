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

from fun import settings
from .apps import EduhubConfig

import os
from django.http import FileResponse
from django.forms import ModelForm
from .modelform import *
from django.views.decorators.csrf import csrf_protect

eduhub_document_file_dir ='eduhub_document_files'


class ArticleListView( ListView ):
    model = Article
    context_object_name = 'Articles'   
    template_name = EduhubConfig.name + '/list.html'    
    paginate_by = 5

    def get_queryset(self):
        query_set = Article.objects.filter(is_forbade = False)
        return query_set


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

    template_name = EduhubConfig.name + '/detail.html'
    
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        file_path = os.path.join(settings.MEDIA_ROOT, Article.objects.get(pk =  self.kwargs['pk'] ).media_file.file.name)
        
        file_type = magic.from_file( file_path ,mime=True)

        context['is_video']=1 if file_type.startswith('video/') else 0

        print(context)
        return context
    

class ArticleCreateView( CreateView ):
    model = Article
    template_name =EduhubConfig.name + '/create.html'
    fields = ['title', 'media_file',]
    success_url ='/'+ EduhubConfig.name + '/list'   
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super(ArticleCreateView, self).form_valid(form)



def create(request):
        if request.method == 'POST': 
            article = ArticleModelForm(request.POST,  request.FILES) 
            
            if article.is_valid(): 
                article.instance.author = request.user
                article.save()
                return redirect(reverse( 'list') )
                
            return render(request , EduhubConfig.name + "/create.html", context={ 'article':article })

        else:
            article = ArticleModelForm
            return render(request , EduhubConfig.name + "/create.html", context={ 'article':article })

        


def update(request, pk=''):
        if request.method == 'POST': 
            article = ArticleModelForm(request.POST,  request.FILES) 
            
            if article.is_valid(): 
                article.instance.author = request.user
                article.save()
                return redirect(reverse( 'list') )
                
            return render(request , EduhubConfig.name + "/create.html", context={ 'article':article })

        else:
            article = ArticleModelForm(Article.objects.get(id = pk))
            return render(request , EduhubConfig.name + "/create.html", context={ 'article':article })

        

def get_file(request,file_path): 
    file_path = os.path.join(settings.MEDIA_ROOT,  file_path)  
    is_article_forbade = Article.objects.filter( media_file = file_path, is_forbade = True ).exists()
    if(os.path.exists( file_path ) and not is_article_forbade ):
        return FileResponse(open(file_path, 'rb'))
    else:
        return Http404()
