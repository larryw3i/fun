
import math
from hurry import filesize
from .models import Label
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from djangovalidators.validators import FileSizeValidator

class LabelModelForm(ModelForm):
    class Meta:
        model = Label
        help_texts = {
            'cover': _('cover image'),
            'name': _('name'),
        }
        fields = ['name', 'cover']

    def clean(self):
        cleaned_data = self.cleaned_data

        cover_file = cleaned_data['cover']

        cover_file_max_size = 500* 1024
        
        if  cover_file.content_type.endswith()('/pdf') and  cover_file.size > cover_file_max_size:
            raise forms.ValidationError( _('conver size should be less than')+' '+filesize.size( cover_file_max_size ) , code='invalid')

        return cleaned_data