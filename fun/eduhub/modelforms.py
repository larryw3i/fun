
import math
from hurry import filesize
from .models import Label
from django import forms
from django.forms import ModelForm, ImageField
from django.utils.translation import gettext_lazy as _
from djangovalidators.validators import FileSizeValidator

class LabelModelForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name', 'cover' ,'comment']
        
        labels = {
            'name': _('Label name'),
            'cover': _('Cover image'),
            'comment': _('Comment'),
        }
        
        widgets = {
            'cover': forms.FileInput( attrs={ 'class': 'preview-image' } )
        }

        
        
