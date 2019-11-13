
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
def get_body_theme_class(context):
    theme = context['request'].COOKIES.get('theme', '')
    return body_themes.get(theme, body_themes['light'])


@register.simple_tag(takes_context=True)
def get_navbar_theme_class(context):
    theme = context['request'].COOKIES.get('theme', '')
    return navbar_themes.get(theme, navbar_themes['light'])


@register.simple_tag(takes_context=True)
def get_current_theme(context):
    return context['request'].COOKIES.get('theme', 'light')


@register.simple_tag()
def get_all_bootswatch_themes():
    print(os.listdir(os.path.join(settings.BASE_DIR,
                                  'static', 'libs', 'bootswatch', 'dist')))
    return os.listdir(os.path.join(settings.BASE_DIR,  'static', 'libs', 'bootswatch', 'dist'))
