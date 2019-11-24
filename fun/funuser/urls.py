
from django.urls import path
from . import views
from .apps import FunuserConfig

app_name = FunuserConfig.name

urlpatterns = [  
    path( f'{app_name}_update/', views.FunuserUpdateView.as_view(), name = f'{app_name}_update'),
    path( f'{app_name}_detail/<int:user>', views.FunuserDetailView.as_view(), name = f'{app_name}_detail'),
]