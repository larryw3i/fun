from django.shortcuts import render

# Create your views here.

from django import forms

from django.views.generic import CreateView, ListView

from .models import *

from .apps import EduhubConfig

from django.contrib.auth.mixins import LoginRequiredMixin 

from django.shortcuts import *

class ArticleCreateModelForm( LoginRequiredMixin, forms.ModelForm ):
    
    class Meta:
        
        model = Article
    
        fields = ('title', 'document_file', 'classifications')
    
    login_url = 'account_login' 

class ClassificationCreateModelForm( LoginRequiredMixin, forms.ModelForm ):
    
    class Meta:
        
        model = Classification
    
        fields = ('name',)
    
    login_url = 'account_login' 


def article_create( request ):
    if request.method == 'GET' :
        return render(
            request, 
            EduhubConfig.name+'/article/create.html',
            context={'form':ArticleCreateModelForm}
        )
    
    elif request.method == 'POST':
        article = ArticleCreateModelForm(request.POST)

        if article.is_valid():
            article.author = request.user
            article.save()
            return redirect(
                reverse("article_list")
            )
        else:
            return render(
                request, 
                EduhubConfig.name+'/article/create.html',
                context={'form':ArticleCreateModelForm}
            )

def classification_create( request ):
    if request.method == 'GET' :
        return render(
            request, 
            EduhubConfig.name+'/classification/create.html',
            context={'form':ClassificationCreateModelForm}
        )
    
    elif request.method == 'POST':
        classification = ClassificationCreateModelForm(request.POST)

        if classification.is_valid():
            classification.save()
            return redirect(
                reverse("classification_list")
            )
        else:
            return render(
                request, 
                EduhubConfig.name+'/classification/create.html',
                context={'form':ClassificationCreateModelForm}
            )


def article_list( ListView ):
    model = Article
    context_object_name = 'Articles'   
    Article = EduhubConfig.name+ '/article/list.html'

def classification_list( ListView ):
    model = Classification
    context_object_name = 'Classifications'   
    Article = EduhubConfig.name+ '/classification/list.html'