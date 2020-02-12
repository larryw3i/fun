import os
import uuid
import hashlib
from django import forms
from django.core import validators
from django.db import models
from functools import partial
from funfile.storage import upload_to
from django.contrib.auth.models import User
from hurry import filesize
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingFormField, RichTextUploadingField

# Create your models here.

label_name = 'label'
content_name = 'content'
funcontent_name = 'funcontent'
eduhubhomesticker_name = 'eduhubhomesticker'

class Label(models.Model):

    class Meta:
        verbose_name = _('Eduhub label') 
        verbose_name_plural = _('Eduhub  labels')

    def __str__(self):
        return self.name

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(  max_length = 64, blank = False,  verbose_name =_('Label name') )
    comment = models.CharField(   max_length  = 64,   verbose_name =_('Label comment') )
    cover = models.ImageField(   upload_to= upload_to, blank = True,   verbose_name =_('Label cover') )
    creating_date = models.DateTimeField(  auto_now_add = True,   verbose_name =_('Label creating date') )
    author = models.ForeignKey( to = User, on_delete=models.CASCADE,   verbose_name =_('Label author') )
    is_legal = models.BooleanField( default = True,    verbose_name =_('Is label legal')+" ?")


class Content(models.Model):

    class Meta:
        verbose_name = _('Eduhub content')
        verbose_name_plural = _('Eduhub contents')

    def __str__(self):
        return self.title

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    label = models.ForeignKey( to = Label, on_delete= models.CASCADE , null=True,  verbose_name =_('Content label')  )
    title = models.CharField(  max_length = 64, blank = False ,  verbose_name =_('Content title') )
    content_file =  models.FileField(  upload_to = upload_to, blank = True,  verbose_name =_('Content file') )
    uploading_date = models.DateTimeField(   auto_now_add = True,  verbose_name =_('Content uploading date') )
    comment = models.TextField(   max_length  = 64,  verbose_name =_('Content comment') )
    is_legal = models.BooleanField(   default = True,   verbose_name =_('Is content legal') )
    

class Funcontent(models.Model):

    class Meta:
        verbose_name = _('Eduhub content (NEW)')
        verbose_name_plural = _('Eduhub contents (NEW)')

    def __str__(self):
        return self.title

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    label = models.ForeignKey( to = Label, on_delete= models.CASCADE , null=True,  verbose_name =_('Content label')  )
    title = models.CharField(  max_length = 64, blank = False ,  verbose_name =_('Content title') )
    content = RichTextUploadingField()
    classification = models.CharField( max_length = 64, blank = True , null = True,  verbose_name =_('Content classification') ) 
    uploading_date = models.DateTimeField(   auto_now_add = True,  verbose_name =_('Content uploading date') )
    comment = models.TextField(   max_length  = 64,  verbose_name =_('Content comment') )
    is_legal = models.BooleanField(   default = True,   verbose_name =_('Is content legal') )
    
class Eduhubhomesticker( models.Model ):
    class Meta:
        verbose_name = _('Eduhub homepage sticker')
        verbose_name_plural = _('Eduhub homepage stickers')
    
    def __str__(self):
        return self.title
        
    id = models.UUIDField( primary_key=True, default= uuid.uuid4, editable=False,  )
    title = models.CharField( max_length = 32 ,  verbose_name = _('Eduhub homepage sticker title'))
    subtitle = models.TextField( max_length = 64, verbose_name = _('Eduhub homepage sticker subtitle') )
    cover = models.ImageField( upload_to = upload_to , verbose_name = _('Eduhub homepage sicker cover') )
    promulgator = models.ForeignKey(  to = User, on_delete=models.CASCADE, verbose_name = _('Eduhub homepage sticker promulgator') )    
    description = RichTextUploadingField( )
    content = RichTextUploadingField( )
    promulgating_date = models.DateTimeField(   auto_now_add = True,  verbose_name = _('Eduhub homepage sticker promulgating date'))
    comment = models.TextField( max_length = 128 , verbose_name = _('Eduhub homepage sticker comment') )
    is_hidden = models.BooleanField( default= False , verbose_name = _('Hidden')+" ?" )




#  deprecated
class Funclassification( models.Model ):

    class Meta:
        verbose_name = _('Eduhub classification')
        verbose_name_plural = _('Eduhub classifications')

    def __str__(self):
        return self.name

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    parent = models.ForeignKey( 'self' , on_delete = models.SET_DEFAULT, default = None, null = True, blank = True , verbose_name = _('Parent classification') )
    name = models.CharField(  max_length = 64, blank = False ,  verbose_name =_('Classification name') )
    level = models.IntegerField( validators = [ validators.MinValueValidator(1), validators.MaxValueValidator(10) ], default = 1,  verbose_name =_('Classification level') )
    creating_date = models.DateTimeField(   auto_now_add = True,  verbose_name =_('Classification creating date') )
    creating_user = models.ForeignKey( to = User, on_delete=models.CASCADE,   verbose_name =_('Classification creating user') )
    is_disabled = models.BooleanField(   default = False,   verbose_name =_('Is classification disabled') )
