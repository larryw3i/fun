
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ArticleCreateView.as_view(), name = 'create'),
    path('list/', views.ArticleListView.as_view(), name = 'list')
]