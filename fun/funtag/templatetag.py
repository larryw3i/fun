
import os
from urllib.parse import unquote

from django import template
from django.utils.translation import gettext_lazy as _

from fun import settings
import pytz
from django.utils import timezone
from datetime import datetime
from fun.funvalue import subjects_top

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


register = template.Library()


def bootswatch_css_url(
    theme): return f'bootswatch/dist/{theme}/bootstrap.min.css'


bootstrap_css_url = 'bootstrap/dist/css/bootstrap.min.css'


@register.simple_tag(takes_context=True)
def get_cookies(context, name, unquote_result=False):
    request = context['request']
    return (unquote(request.COOKIES.get(name, '')) if unquote_result
            else request.COOKIES.get(name, ''))


@register.simple_tag(takes_context=True)
def get_current_theme_url(context):
    theme = context['request'].COOKIES.get('theme', 'default')
    return ('/static/node_modules/' + (bootstrap_css_url if theme == 'default'
                                       else bootswatch_css_url(theme)))


@register.simple_tag(takes_context=True)
def get_current_theme_name(context):
    return _(context['request'].COOKIES.get('theme', 'default'))


@register.simple_tag()
def get_beian_url():
    return os.environ.get('BEIAN_URL', '')


@register.simple_tag()
def get_beian_text():
    return os.environ.get('BEIAN_TEXT', '')


@register.simple_tag(takes_context=True)
def get_current_eduhub_top_filter(context):
    request = context['request']
    eduhub_top_filter = request.COOKIES.get('eduhub_top_filter', '')
    return _(subjects_top[eduhub_top_filter] if len(eduhub_top_filter) > 0
             else 'All')
