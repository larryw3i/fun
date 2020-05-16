
import os
from urllib.parse import unquote

from django import template
from django.utils.translation import gettext_lazy as _

from fun import settings
import pytz
from django.utils import timezone
from datetime import datetime
from fun.funvalue import subjects_top

from funuser.models import Funuser
from django.shortcuts import get_object_or_404
from django.urls import reverse

from fun.settings import STATIC_URL, app_env

import yaml


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
    return app_env['beian']['url']


@register.simple_tag()
def get_beian_text():
    return app_env['beian']['text']


@register.simple_tag(takes_context=True)
def get_current_eduhub_top_filter(context):
    request = context['request']
    eduhub_top_filter = request.COOKIES.get('eduhub_top_filter', '')
    return _(subjects_top[eduhub_top_filter] if len(eduhub_top_filter) > 0
             else 'All')


@register.simple_tag(takes_context=True)
def get_funuser_name(context, user):
    funuser = Funuser.objects.filter(user=user).first()
    return funuser.full_name if (funuser and len(funuser.full_name) > 0) \
        else user.username


@register.simple_tag(takes_context=True)
def get_funuser_avatar_url(context, user):
    funuser = Funuser.objects.filter(user=user).first()
    return \
        reverse(
            'funfile:get_file',
            kwargs={"file_id": funuser.avatar.name}
        ) \
        if (funuser and len(funuser.avatar.name) > 0) \
        else (STATIC_URL + 'images/x_dove.webp')


@register.simple_tag()
def get_pdf_view_url():
    return STATIC_URL + "libs/pdfjs-2.2.228-dist/web/viewer.min.html" +\
        "?file=funfile/get_file/"  # combine a funfile name


@register.simple_tag()
def get_classification_issue_url():
    return 'https://github.com/larryw3i/fun/blob/master/fun/templates/'\
        + 'eduhub/how_to_classification.html'


@register.simple_tag(takes_context=True)
def get_file_url(context, file_id):
    return \
        reverse(
            'funfile:get_file',
            kwargs={"file_id": file_id}
        )
