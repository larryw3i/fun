
import math
from hurry import filesize
from .models import Label, Content, Funcontent, Funclassification, Eduhubhomesticker
from django import forms
from django.forms import ModelForm, ImageField
from django.utils.translation import gettext_lazy as _
from djangovalidators.validators import FileSizeValidator
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingFormField, RichTextUploadingField
from django.contrib.admin.widgets import ForeignKeyRawIdWidget


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
            'title':forms.TextInput( attrs = { 'autocomplete':'off' }),
            'comment': forms.Textarea( attrs={ 'rows': '5' } ), 
            'label': forms.HiddenInput()
        }



class FuncontentModelForm( ModelForm ):

    
    class Meta:
        
        model = Funcontent
        fields = ['title', 'content' ,'comment', 'label' ,'classification'] 

        
        labels = {
            'title': '',
            'label': _('Label'),
            'content': _('Content'),
            'comment': _('Comment'),
            'classification':_('Content classification'),
        }


        widgets = {
            'title':forms.TextInput( attrs = { 'autocomplete':'off',  'placeholder': _('Content title') ,'class':'text-center' }),
            'comment': forms.Textarea( attrs={ 'rows': '5' } ), 
            'label':forms.HiddenInput(),
            'classification': forms.TextInput( attrs= {  'placeholder': _('classification : college/grade/semester/course') , 'class':'text-center' } ),
        }

    

class EduhubhomestickerModelForm(ModelForm):
    
    class Meta:
        
        model = Eduhubhomesticker
        fields = ['title', 'cover' ,'content', 'comment'] 
        
        labels = {
            'title': _('Sticker title'),
            'cover': _('Sticker Cover'),
            'content': _('Sticker content'),
            'comment': _('Sticker Comment'),
        }


        widgets = {
            'comment': forms.Textarea( attrs={ 'rows': '5' } ), 
        }

    
 
