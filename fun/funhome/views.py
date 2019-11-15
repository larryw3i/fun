import os

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from fun import settings

from .apps import FunhomeConfig


class HomeView(TemplateView):
    template_name = FunhomeConfig.name + '/home.html'


def get_all_bootswatch_themes(request):
    if request.method == 'GET':
        return JsonResponse(os.listdir(os.path.join(settings.BASE_DIR,  'static', 'libs', 'bootswatch', 'dist')), safe=False)
