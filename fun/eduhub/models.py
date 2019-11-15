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



class Label(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(  max_length = 64, blank = False, )
    comment = models.CharField(   max_length  = 64, )
    cover = models.ImageField(   upload_to= upload_to, blank = True )
    creating_date = models.DateTimeField(  auto_now_add = True,)
    author = models.ForeignKey( to = User, on_delete=models.CASCADE,  )
    is_legal = models.BooleanField( default = True,  )


class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    label = models.ForeignKey( to = Label, on_delete= models.CASCADE , null=True )
    title = models.CharField(  max_length = 64, blank = False )
    content_file = models.FileField(  upload_to = upload_to, blank = True)
    uploading_date = models.DateTimeField(   auto_now_add = True,)
    comment = models.TextField(   max_length  = 64, )
    is_legal = models.BooleanField(   default = True,  )
    
