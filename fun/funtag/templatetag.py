
import os
from urllib.parse import unquote

from django import template
from django.utils.translation import gettext_lazy as _

from fun import settings
import pytz
from django.utils import timezone
from datetime import datetime

from dotenv import find_dotenv,load_dotenv 
load_dotenv( find_dotenv() )


register = template.Library()
bootswatch_css_url =lambda theme: f'node_modules/bootswatch/dist/{theme}/bootstrap.min.css'
bootstrap_css_url ='node_modules/bootstrap/dist/css/bootstrap.min.css'

@register.simple_tag(takes_context=True)
def get_cookies(context, name, unquote_result=False):
    request = context['request']
    return unquote(request.COOKIES.get(name, '')) if unquote_result else request.COOKIES.get(name, '')


@register.simple_tag(takes_context=True)
def get_current_theme_url(context):
    theme = context['request'].COOKIES.get('theme', 'default') 
    return bootstrap_css_url if theme == 'default' else bootswatch_css_url( theme )


@register.simple_tag(takes_context=True)
def get_current_theme_name(context):
    return _(context['request'].COOKIES.get('theme', 'default') )


@register.simple_tag( )
def get_beian_url():
    return os.environ.get('BEIAN_URL','')

@register.simple_tag( )
def get_beian_text():
    return os.environ.get('BEIAN_TEXT','')

