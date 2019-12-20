import os
from datetime import datetime

import magic
from django.contrib.auth.models import User
from django.core import serializers
from django.core.files import File
from django.http import (FileResponse, Http404, HttpResponse,
                         HttpResponseBadRequest, HttpResponseForbidden,
                         JsonResponse)
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.utils import translation
from django.utils.translation import gettext_lazy as _
# Create your views here.
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from fun import funvalue, settings
from funfile.models import Checkup

from .apps import FunhomeConfig
from .modelforms import HomestickerModelForm , FunhomestickerModelForm
from .models import Homesticker, homesticker_name, funhomesticker_name , Funhomesticker
import pytz

home_template =  FunhomeConfig.name + '/home.html'
homesticker_create_template = f'{FunhomeConfig.name}/{homesticker_name}{funvalue.create_html}'
homesticker_detail_template = f'{FunhomeConfig.name}/{homesticker_name}{funvalue.detail_html}'
homesticker_delete_template = f'{FunhomeConfig.name}/{homesticker_name}{funvalue.delete_html}'
homesticker_update_template = f'{FunhomeConfig.name}/{homesticker_name}{funvalue.update_html}'
homesticker_list_template   = f'{FunhomeConfig.name}/{homesticker_name}{funvalue.list_html}'


funhomesticker_create_template = f'{FunhomeConfig.name}/{funhomesticker_name}{funvalue.create_html}'
funhomesticker_detail_template = f'{FunhomeConfig.name}/{funhomesticker_name}{funvalue.detail_html}'
funhomesticker_delete_template = f'{FunhomeConfig.name}/{funhomesticker_name}{funvalue.delete_html}'
funhomesticker_update_template = f'{FunhomeConfig.name}/{funhomesticker_name}{funvalue.update_html}'
funhomesticker_list_template   = f'{FunhomeConfig.name}/{funhomesticker_name}{funvalue.list_html}'




class HomestickerListView( ListView ):  
    model = Homesticker
    form_class = HomestickerModelForm
    template_name = homesticker_list_template

    ordering = ['-promulgating_date', ]

    paginate_by = 8
    paginate_orphans = 1
    context_object_name = 'homestickers'

    def get_queryset(self):
        queryset = Homesticker.objects.filter( is_hidden = False ).order_by('-promulgating_date')
        return queryset


class HomestickerDetailView( DetailView ):  
    model = Homesticker
    form_class = HomestickerModelForm
    template_name = homesticker_detail_template

    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)
        file_path = os.path.join(settings.MEDIA_ROOT, str( context_data['object'].content_file.name ))
        context_data['is_video'] = str( magic.from_file( file_path ,mime=True) ).startswith('video/')
        return context_data

class FunhomestickerListView( ListView ):  
    model = Funhomesticker
    form_class = FunhomestickerModelForm
    template_name = funhomesticker_list_template

    ordering = ['-promulgating_date', ]

    paginate_by = 8
    paginate_orphans = 1
    context_object_name = 'funhomestickers'

    def get_queryset(self):
        queryset = Funhomesticker.objects.filter( is_hidden = False ).order_by('-promulgating_date')
        return queryset


class FunhomestickerDetailView( DetailView ):  
    model = Funhomesticker
    form_class = FunhomestickerModelForm
    template_name = funhomesticker_detail_template


class HomeView( TemplateView ):
    template_name = home_template

    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)
        funhomestickers = Funhomesticker.objects.filter( is_hidden = False ).order_by('-promulgating_date')[:8]
        if funhomestickers.count() < 1:
            funhomestickers = [  get_default_funhomesticker()  ]
            context_data['is_funhomestickers_null']  = True 
        context_data['funhomestickers'] = funhomestickers
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
        raise Http404()


def get_default_homesticker():
    default_carousel_image_path = os.path.join(  settings.STATIC_ROOT, 'images', 'default_carousel_image.webp' ) 
    default_carousel_content_file_path = os.path.join(  settings.STATIC_ROOT, 'media', 'default_carousel_content_file.pdf' ) 
    return Homesticker( 
        title = _('X-DOVE'),  
        subtitle = _('Larry`s sharing'), 
        cover = File( open( default_carousel_image_path ) ) ,
        promulgator =  User.objects.get(is_superuser=True) ,
        content_file = File( open( default_carousel_content_file_path )), 
        promulgating_date=  datetime(2005, 7, 14, 12, 30),
        comment = _('larry') )

def get_default_funhomesticker():
    default_carousel_image_path = os.path.join(  settings.STATIC_ROOT, 'images', 'default_carousel_image.webp' ) 
    default_carousel_content_file_path = os.path.join(  settings.STATIC_ROOT, 'media', 'default_carousel_content_file.pdf' ) 
    return Funhomesticker( 
        title = _('X-DOVE'),  
        subtitle = _('Larry`s sharing'), 
        cover = File( open( default_carousel_image_path ) ) ,
        promulgator =  User.objects.get(is_superuser=True) ,
        content = '', # File( open( default_carousel_content_file_path )), 
        promulgating_date=  datetime(2005, 7, 14, 12, 30),
        comment = _('larry') )
