
from django.urls import path
from . import views
from .apps import EduhubConfig


urlpatterns = [
    path('label_create/', views.LabelCreateView.as_view(), name = 'label_create')
]