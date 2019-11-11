import os
import uuid
import hashlib
from django import forms
from django.core import validators
from django.db import models
from functools import partial
from funfile.models import upload_to
from django.contrib.auth.models import User
from hurry import filesize
from django.utils.translation import gettext_lazy as _

# Create your models here.



class Label(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField( _('Label name'), max_length = 64, blank = False, )
    comment = models.CharField( _('Comment'),  max_length  = 64, )
    cover = models.ImageField( _('Conver image'),  upload_to= upload_to, )
    creating_date = models.DateTimeField( _('Creating date'),  auto_now_add = True,)
    author = models.ForeignKey( to = User, on_delete=models.CASCADE, help_text = _('Author') )
    is_legal = models.BooleanField( _('Is legal'),  default = True,  )


class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField( _('Title'), max_length = 64,  )
    content_file = models.FileField( _('Content file'), upload_to = upload_to, help_text = _('Content file') )
    uploading_date = models.DateTimeField( _('Creating date'),  auto_now_add = True,)
    comment = models.CharField( _('Comment'),  max_length  = 64, )
    is_legal = models.BooleanField( _('Is legal'),  default = True,  )
    
