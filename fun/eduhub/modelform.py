from django.shortcuts import render

# Create your views here.

from django import forms

from django.views.generic import *

from .models import *

from .apps import EduhubConfig

from django.contrib.auth.mixins import LoginRequiredMixin 

from django.shortcuts import *

from django.core.paginator import Paginator
from django.db.models import *
import magic 
from django.utils.translation import gettext as _t

from django.core import validators
from django.core.exceptions import ValidationError

from fun import settings
from .apps import EduhubConfig

import os
from django.http import FileResponse
from django.forms import ModelForm

from django.forms import widgets


class ArticleModelForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'media_file']
        widgets = {
            'media_file': widgets.FileInput( attrs={'accept':'.pdf,video/*', 'class':'preview'}),
        }
        
