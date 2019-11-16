
import math
from hurry import filesize
from .models import Label, Content
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

        
        

class ContentModelForm(ModelForm):
    
    class Meta:
        
        model = Content
        fields = ['title', 'content_file' ,'comment', 'label'] 
        
        labels = {
            'title': _('Title name'),
            'label': _('Label'),
            'content_file': _('Content file'),
            'comment': _('Comment'),
        }

        help_texts = {
            'content_file': _('content file, pdf and video file is allowed only')
        }

        widgets = {
            'content_file': forms.FileInput( attrs={ 'class': 'preview-pdf preview-video', 'accept':'video/*, .pdf' } ),
            'comment': forms.Textarea( attrs={ 'rows': '5' } ), 
            'label': forms.HiddenInput()
        }

    

        
        
