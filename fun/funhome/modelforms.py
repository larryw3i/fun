
import math
from hurry import filesize
from .models import Homesticker
from django import forms
from django.forms import ModelForm, ImageField
from django.utils.translation import gettext_lazy as _
from djangovalidators.validators import FileSizeValidator


class HomestickerModelForm(ModelForm):
    
    class Meta:
        
        model = Homesticker
        fields = ['title', 'cover' ,'content_file', 'comment'] 
        
        labels = {
            'title': _('Sticker title'),
            'cover': _('Sticker Cover'),
            'content_file': _('Sticker content file'),
            'comment': _('Sticker Comment'),
        }

        help_texts = {
            'content_file': _('content file, pdf and video file is allowed only')
        }

        widgets = {
            'content_file': forms.FileInput( attrs={ 'class': 'preview-pdf preview-video', 'accept':'video/*, .pdf' } ),
            'comment': forms.Textarea( attrs={ 'rows': '5' } ), 
        }

    
 
