

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
        exclude = ['user', ]
        
        fieldsets = (
            ( _("avatar"), {'fields': ['avatar', ]}),
            ( _('Birth date'),  {'fields':['birth_date',    'is_birth_date_outward']}),
            ( _('Address'),     {'fields':['address',       'is_Address_outward']}),
            ( _('Hometown'),    {'fields':['hometown',      'is_hometown_date_outward']}),
            ( _('College'),     {'fields':['college',       'is_college_outward']}),
            ( _('Occupation'),  {'fields':['occupation',    'is_occupation_outward']}),
            ( _('Hobby'),       {'fields':['hobby',         'is_hobby_outward']}),
            ( _('Motto'),       {'fields':['motto',         'is_motto_outward']}), 
        )
 