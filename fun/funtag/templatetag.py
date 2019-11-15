
import os
from urllib.parse import unquote

from django import template

from fun import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def get_cookies(context, name, unquote_result=False):
    request = context['request']
    return unquote(request.COOKIES.get(name, '')) if unquote_result else request.COOKIES.get(name, '')



@register.simple_tag(takes_context=True)
def get_current_theme(context):
    return context['request'].COOKIES.get('theme', 'cerulean')

