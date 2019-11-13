
from django import template
from urllib.parse import unquote

register = template.Library()
body_themes = {
    'dark': 'text-light bg-dark',
    'care': 'text-primary bg-secondary',
    'light': '',
}

navbar_themes = {
    'dark': 'navbar-dark bg-dark',
    'care': 'navbar-dark bg-dark',
    'light': '',
}

@register.simple_tag(takes_context = True)
def get_cookies(context, name, unquote_result= False):
    request = context['request']
    return  unquote( request.COOKIES.get( name, '') ) if unquote_result else  request.COOKIES.get( name, '')

@register.simple_tag(takes_context = True)
def get_body_theme(context):
    theme = context['request'].COOKIES.get( 'theme', '') 
    return  body_themes.get( theme, body_themes['light'] )
@register.simple_tag(takes_context = True)
def get_navbar_theme(context):
    theme = context['request'].COOKIES.get( 'theme', '') 
    return  navbar_themes.get( theme, navbar_themes['light'] )