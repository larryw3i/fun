

import math
from hurry import filesize
from .models import Funuser
from django import forms
from django.forms import ModelForm, ImageField
from django.utils.translation import gettext_lazy as _
from djangovalidators.validators import FileSizeValidator

class FunuserModelForm(ModelForm):
    class Meta:
        model = Funuser