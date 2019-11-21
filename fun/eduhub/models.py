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

# Create your models here.

label_name = 'label'
content_name = 'content'

class Label(models.Model):

    class Meta:
        verbose_name = _('Eduhub label') 
        verbose_name_plural = _('Eduhub  labels')

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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    label = models.ForeignKey( to = Label, on_delete= models.CASCADE , null=True,  verbose_name =_('Content label')  )
    title = models.CharField(  max_length = 64, blank = False ,  verbose_name =_('Content title') )
    content_file = models.FileField(  upload_to = upload_to, blank = True,  verbose_name =_('Content file') )
    uploading_date = models.DateTimeField(   auto_now_add = True,  verbose_name =_('Content uploading date') )
    comment = models.TextField(   max_length  = 64,  verbose_name =_('Content comment') )
    is_legal = models.BooleanField(   default = True,   verbose_name =_('Is content legal') )
    
