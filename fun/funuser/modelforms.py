

import math

from django import forms
from django.forms import ImageField, ModelForm
from django.utils.translation import gettext_lazy as _
from djangovalidators.validators import FileSizeValidator
from hurry import filesize

from .models import Funuser


class FunuserModelForm(ModelForm):
    class Meta:
        model = Funuser
        exclude = ['user', ]

        widgets = {
            'avatar': forms.FileInput( attrs={ 'class': 'form-control-file' } ) , 
            'birth_date': forms.FileInput( attrs={ 'class': 'form-control' } ) , 
            'address': forms.FileInput( attrs={ 'class': 'form-control' } ) , 
            'hometown': forms.FileInput( attrs={ 'class': 'form-control' } ) , 
            'college': forms.FileInput( attrs={ 'class': 'form-control' } ) , 
            'occupation': forms.FileInput( attrs={ 'class': 'form-control' } ) , 
            'hobby': forms.FileInput( attrs={ 'class': 'form-control' } ) , 
            'motto': forms.FileInput( attrs={ 'class': 'form-control' } ) , 
            'is_birth_date_outward': forms.FileInput( attrs={ 'class': 'custom-control-input', 'type': 'checkbox' ,} ) , 
            'is_address_outward': forms.FileInput( attrs={ 'class': 'custom-control-input', 'type': 'checkbox' , } ) , 
            'is_hometown_outward': forms.FileInput( attrs={ 'class': 'custom-control-input', 'type': 'checkbox' , } ) , 
            'is_college_outward': forms.FileInput( attrs={ 'class': 'custom-control-input', 'type': 'checkbox' , } ) , 
            'is_occupation_outward': forms.FileInput( attrs={ 'class': 'custom-control-input', 'type': 'checkbox' , } ) , 
            'is_hobby_outward': forms.FileInput( attrs={ 'class': 'custom-control-input' , 'type': 'checkbox' ,} ) , 
            'is_motto_outward': forms.FileInput( attrs={ 'class': 'custom-control-input' , 'type': 'checkbox' ,} ) , 
        }

'''
    user = models.ForeignKey( to= User,  on_delete=models.CASCADE,  verbose_name = _('User') )

    avatar = models.ImageField( upload_to = upload_to ,  verbose_name = _('Avatar') )
    
    birth_date  = models.DateField( blank = True ,  verbose_name = _('Brith date'))
    is_birth_date_outward = models.BooleanField( default = False ,  verbose_name = _('Is outward')+' ?' )
    
    address  = models.CharField( blank = True, max_length = 64 ,  verbose_name = _('Address')  )
    is_address_outward = models.BooleanField( default = False ,  verbose_name = _('Is outward')+' ?')
    
    hometown  = models.CharField( blank = True , max_length = 64 ,  verbose_name = _('Hometown') )
    is_hometown_outward = models.BooleanField( default = False ,  verbose_name = _('Is outward')+' ?')
    
    college  = models.CharField( blank = True , max_length = 64 ,  verbose_name = _('College') )
    is_college_outward = models.BooleanField( default = False ,  verbose_name = _('Is outward')+' ?')

    occupation  = models.CharField( blank = True , max_length = 64,  verbose_name = _('Occupation')  )
    is_occupation_outward = models.BooleanField( default = False ,  verbose_name = _('Is outward')+' ?')

    hobby  = models.CharField( blank = True , max_length = 64 ,  verbose_name = _('Hobby') )
    is_hobby_outward = models.BooleanField( default = False ,  verbose_name = _('Is outward')+' ?' )
    
    motto  = models.CharField( blank = True , max_length = 64 ,  verbose_name = _('Motto') )
    is_motto_outward = models.BooleanField( default = False ,  verbose_name = _('Is outward')+' ?' )

    creating_date =  models.DateTimeField(   auto_now_add = True,  verbose_name =_('Funuser creating date') )

    

'''