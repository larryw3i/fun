
import os
from urllib.parse import unquote

from django import template

from fun import settings

register = template.Library()
body_themes = {
    'dark': 'text-light bg-dark',
    'care': 'text-light bg-secondary',
    'light': '',
}

navbar_themes = {
    'dark': 'navbar-dark bg-dark',
    'care': 'navbar-dark bg-dark',
    'light': '',
}


@register.simple_tag(takes_context=True)
def get_cookies(context, name, unquote_result=False):
    request = context['request']
    return unquote(request.COOKIES.get(name, '')) if unquote_result else request.COOKIES.get(name, '')



@register.simple_tag(takes_context=True)
def get_current_theme(context):
    return context['request'].COOKIES.get('theme', 'light')

