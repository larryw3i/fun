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
from django.shortcuts import render_to_response, get_object_or_404

import hashlib


eduhub_document_file_dir ='eduhub_document_files'


class list( ListView ):
    model = Article
    context_object_name = 'Articles'   
    template_name = EduhubConfig.name + '/list.html'    
    paginate_by = 5

    def get_queryset(self):
        query_set = Article.objects.filter(is_forbade = False).order_by('-uploaded_time')
        return query_set


class _update( UpdateView ):
    model = Article
    template_name =EduhubConfig.name + '/update.html'
    fields = ['title', 'media_file',]
    
    
    def form_valid(self, form):
        if form.instance.author != self.request.user:
            return Http404('nice try')
        return super(update, self).form_valid(form)



class _delete( DeleteView ):
    model = Article
    template_name =EduhubConfig.name + '/delete.html'
    fields = ['title', 'media_file',]
    success_url ='/'+ EduhubConfig.name + '/list'   

class detail( DetailView ):
    model = Article

    template_name = EduhubConfig.name + '/detail.html'
    
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        file_path = os.path.join(settings.MEDIA_ROOT, str(Article.objects.get(pk =  self.kwargs['pk'] ).id))
        
        file_type = magic.from_file( file_path ,mime=True)

        context['is_video']= file_type.startswith('video/') 

        print(context)
        return context
    

class _create( CreateView ):
    model = Article
    template_name =EduhubConfig.name + '/create.html'
    fields = ['title', 'media_file',]
    success_url ='/'+ EduhubConfig.name + '/list'   
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super(_create, self).form_valid(form)



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

        


def update(request, pk):

        article_object =  get_object_or_404(Article, pk=pk)

        if(article_object.author != request.user):
            return Http404()

        
        file_type = magic.from_file(  os.path.join( settings.MEDIA_ROOT, str(pk) )  ,mime=True)

        is_video = file_type.startswith('video/') 

        if request.method == 'POST': 
            article = ArticleModelForm(request.POST,  request.FILES, instance=article_object) 

            print(request.FILES.get('media_file'))
            
            if article.is_valid(): 
                handle_post_file(request.FILES['media_file'], pk)
                article.save()
                return redirect(reverse( 'list') )
                
            return render(request , EduhubConfig.name + "/update.html", context={ 'article':article, 'is_video':is_video, 'article_id':pk })

        else:

            article = ArticleModelForm(instance=article_object)

            return render(request , EduhubConfig.name + "/update.html", context={ 'article':article, 'is_video':is_video, 'article_id':pk })

def delete(request, pk):
    article_object =  Article.objects.get( id=pk )
    
    if(article_object.author != request.user):
        return Http404()

    print(article_object)

    if  article_object is None:
        return Http404()

    file_path = os.path.join( settings.MEDIA_ROOT, str(pk) )
    
    file_type = magic.from_file( file_path ,mime=True)

    is_video = file_type.startswith('video/') 

    if request.method == 'POST':
        article_object.delete()
        return redirect(reverse( 'list') )
                
    else:

        return render(request , EduhubConfig.name + "/delete.html", context={ 'article':article_object, 'is_video':is_video, 'article_id':pk })

    

def get_file(request,file_path): 
    file_path = os.path.join(settings.MEDIA_ROOT,  file_path)  
    is_article_forbade = Article.objects.filter( media_file = file_path, is_forbade = True ).exists()
    if(os.path.exists( file_path ) and not is_article_forbade ):
        return FileResponse(open(file_path, 'rb'))
    else:
        return Http404()


def handle_post_file(post_file,pk):
    with open( os.path.join( settings.MEDIA_ROOT, str(pk) ) , 'wb+') as destination:
        for chunk in post_file.chunks():
            destination.write(chunk)