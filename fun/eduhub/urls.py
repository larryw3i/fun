
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name = 'create'),
    path('list/', views.list.as_view(), name = 'list'),
    path('update/<uuid:pk>',views.update, name ='update'),
    path('detail/<uuid:pk>',views.detail.as_view(), name ='detail'),
    path('delete/<uuid:pk>',views.delete, name ='delete'),
    # path('get_file/<path:file_path>',views.get_file, name ='get_file'),
]