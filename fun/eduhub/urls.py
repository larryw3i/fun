
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ArticleCreateView.as_view(), name = 'create'),
    path('list/', views.ArticleListView.as_view(), name = 'list'),
    path('update/',views.ArticleUpdateView.as_view(), name ='update'),
    path('detail/<uuid:id>',views.ArticleDetailView.as_view(), name ='detail'),
    path('delete/<uuid:id>',views.ArticleDeleteView.as_view(), name ='delete')
]