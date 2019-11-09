import os
import uuid
import hashlib
from django.db import models
from functools import partial
from django.utils.translation import gettext_lazy as _
from fun import settings


# Create your models here.

def upload_to(
    instance, 
    filename:str):

    block_size=65535
    hasher = hashlib.sha256()
    for buf in iter(partial(instance.file.read, block_size), b''):
        hasher.update(buf)

    return  os.path.join( settings.MEDIA_ROOT , hasher.hexdigest() )


class Checkup(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    file_id = models.UUIDField(help_text='file uuid')
    is_legal = models.BooleanField(default= True , help_text='is legal')
    comment = models.TextField(help_text='comment')
