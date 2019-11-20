import os

import magic
from django.core import serializers
from django.http import (FileResponse, Http404, HttpResponse,
                         HttpResponseBadRequest, HttpResponseForbidden,
                         JsonResponse)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import translation
# Create your views here.
from django.views import View
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from fun import funvalue, settings
from funfile.models import Checkup

from .apps import FunhomeConfig
from .modelforms import HomestickerModelForm
from .models import Homesticker, homesticker_name

homesticker_create_template = f'{FunhomeConfig.name}/{homesticker_name}{funvalue.create_html}'
homesticker_detail_template = f'{FunhomeConfig.name}/{homesticker_name}{funvalue.detail_html}'
homesticker_delete_template = f'{FunhomeConfig.name}/{homesticker_name}{funvalue.delete_html}'
homesticker_update_template = f'{FunhomeConfig.name}/{homesticker_name}{funvalue.update_html}'
homesticker_list_template   = f'{FunhomeConfig.name}/{homesticker_name}{funvalue.list_html}'



class HomeView( TemplateView ):
    template_name = FunhomeConfig.name + '/home.html'

    def get_context_data(self, **kwargs):
        homestickers = Homesticker.objects.all().order_by('-promulgating_date')[:8]
        context_data =  super().get_context_data(**kwargs)
        context_data['homestickers'] = homestickers
        return context_data
    


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
 