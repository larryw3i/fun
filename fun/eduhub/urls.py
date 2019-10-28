
from django.urls import path
from . import views

urlpatterns = [
    path('article_create/', views.article_create, name = 'article_create'),
    path('article_list/', views.article_list, name = 'article_list'),
    path('classification_create/', views.classification_create, name = 'classification_create')
]