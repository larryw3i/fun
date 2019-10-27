from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render
from .apps import FunhomeConfig
from django.views.generic import TemplateView


class HomeView( TemplateView ):
    template_name = FunhomeConfig.name + '/home.html'