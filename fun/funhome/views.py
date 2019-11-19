import os

import magic
from django.core import serializers
from django.http import FileResponse, Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils import translation
# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from fun import settings
from funfile.models import Checkup

from .apps import FunhomeConfig


class HomeView(TemplateView):
    template_name = FunhomeConfig.name + '/home.html'


def get_all_bootswatch_themes(request):
    if request.method == 'GET':
        return JsonResponse(os.listdir(os.path.join(settings.BASE_DIR,  'static', 'libs', 'bootswatch', 'dist')), safe=False)

def get_favicon_ico( request ):

    file_path = os.path.join(settings.STATIC_ROOT, 'images' , 'x_dove.webp') 

    if os.path.exists(file_path) :
        content_type = magic.from_file( file_path ,mime=True)
        return FileResponse(open(file_path, 'rb'),content_type = content_type)
    else:
        return Http404()

def change_language( request ):
    LANGUAGE_CODE = request.COOKIES.get('language')
    
    cur_language = translation.get_language()
    try:
        translation.activate(LANGUAGE_CODE) 
    finally:
        translation.activate(cur_language)
    
    return HttpResponse('OK')
