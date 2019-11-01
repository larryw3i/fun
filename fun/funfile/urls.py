
from django.urls import path
from . import views
from .apps import FunfileConfig

app_name = FunfileConfig.name

urlpatterns = [
    path('get_file/<uuid:file_id>', views.get_file, name = 'get_file')
]