
import os
from urllib.parse import unquote

from django import template

from fun import settings

register = template.Library()
bootswatch_css_url =lambda theme: f'/static/libs/bootswatch/dist/{theme}/bootstrap.min.css'
bootstrap_css_url ='/static/libs/bootstrap-4.3.1-dist/css/bootstrap.min.css'

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
    return context['request'].COOKIES.get('theme', 'default') 
