import os
import urllib

from django import template
from django.utils.translation import gettext_lazy as _

from fun import settings
import uuid

from eduhub.models import Classification
register = template.Library()


@register.simple_tag(takes_context=True)
def get_first_filter(context):
    request = context['request']
    eduhub_first_filter = urllib.parse.unquote(
        request.COOKIES.get('eduhub_first_filter', ''))
    return _(eduhub_first_filter) if len(eduhub_first_filter) > 0 else ''


@register.simple_tag(takes_context=True)
def get_filter_split(context):
    request = context['request']
    eduhub_first_filter = urllib.parse.unquote(
        request.COOKIES.get('eduhub_first_filter', ''))
    return '/' if len(eduhub_first_filter) > 0 else ''


@register.simple_tag(takes_context=True)
def get_second_filter(context):
    request = context['request']
    eduhub_second_filter = urllib.parse.unquote(
        request.COOKIES.get('eduhub_second_filter', _('ALL')))
    return _(eduhub_second_filter)


@register.simple_tag()
def get_classification_issue_url():
    return 'https://github.com/larryw3i/fun/blob/master/fun/templates/'\
        + 'eduhub/how_to_classification.html'


@register.simple_tag(takes_context=True)
def get_top_filter_path(context):
    language_code = context['request'].LANGUAGE_CODE
    top_filter_html = 'eduhub/_top_filters/_eduhub_base_top_filter.' \
        + f'{ language_code }.html'
    if os.path.exists(settings.BASE_DIR + '/templates/' + top_filter_html):
        return top_filter_html
    return 'eduhub/_top_filters/_eduhub_base_top_filter.html'


@register.simple_tag(takes_context=True)
def curr_classification(context):
    request = context['request']
    classification = Classification.objects\
    .filter(id = request.COOKIES.get('classification', uuid.UUID(int=0)))\
    .first()
    return _('All') if classification is None else str(Classification)


@register.simple_tag(takes_context=True)
def get_classification(context):
    classifications = Classification.objects.all()
    classifications = sorted( classifications, key=lambda x: str(x) )
    _html = ''
    _len = 0
    for c in classifications:
        print(str(c))
        _len_ = str(c).count('/')
        if _len != _len_:
            _len = _len_
            _html += '<br/>'
        _html += f'<a style="text-indent:{2*_len}em" id="{c.id}">{c.name}</a>'
    return _html