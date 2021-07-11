
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

import urllib

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
def get_first_filter(context):
    request = context['request']
    eduhub_first_filter = urllib.parse.unquote( \
        request.COOKIES.get('eduhub_first_filter', '' ) )
    return _( eduhub_first_filter ) if len( eduhub_first_filter ) > 0 else ''

@register.simple_tag(takes_context=True)
def get_filter_split(context):
    request = context['request']
    eduhub_first_filter = urllib.parse.unquote( \
        request.COOKIES.get('eduhub_first_filter', '' ) )
    return '/' if len( eduhub_first_filter ) > 0 else ''

@register.simple_tag(takes_context=True)
def get_second_filter(context):
    request = context['request']
    eduhub_second_filter = urllib.parse.unquote( 
        request.COOKIES.get('eduhub_second_filter', _('ALL')) )
    return _( eduhub_second_filter ) 

    # if '/' not in eduhub_filter:
    #     return eduhub_filter
    # eduhub_filter_split = eduhub_filter.split('/')
    # return f'{_(eduhub_filter_split[0])}/{_(eduhub_filter_split[1] )}'


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

@register.simple_tag(takes_context=True)
def get_top_filter_path( context ):
    language_code = context['request'].LANGUAGE_CODE
    top_filter_html = 'eduhub/_top_filters/_eduhub_base_top_filter.' \
        +f'{ language_code }.html'
    if os.path.exists( settings.BASE_DIR + '/templates/' + top_filter_html ):

        return top_filter_html

    return 'eduhub/_top_filters/_eduhub_base_top_filter.html'

@register.simple_tag
def get_site_gray():
    return settings.site_gray

@register.simple_tag
def get_allow_registration():
    return settings.allow_registration

