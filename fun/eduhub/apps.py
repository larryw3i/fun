from django.apps import AppConfig
from django.utils.translation import gettext as _t
import uuid
from django.core import validators
from django.core.exceptions import ValidationError
import magic

class EduhubConfig(AppConfig):
    name = 'eduhub'



