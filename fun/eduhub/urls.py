
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name = 'create'),
    path('list/', views.ArticleListView.as_view(), name = 'list'),
    path('update/',views.ArticleUpdateView.as_view(), name ='update'),
    path('detail/<uuid:pk>',views.ArticleDetailView.as_view(), name ='detail'),
    path('delete/<uuid:pk>',views.ArticleDeleteView.as_view(), name ='delete'),
    path('get_file/<path:file_path>',views.get_file, name ='get_file'),
]