import os
import uuid
import hashlib
from django.db import models
from functools import partial
from django.utils.translation import gettext_lazy as _
from fun import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import  time, random
from urllib.parse import urljoin
from django.conf import settings
from django.core.exceptions import SuspiciousFileOperation
from django.core.files import File, locks
from django.core.files.move import file_move_safe
from django.core.signals import setting_changed
from django.utils import timezone
from django.utils._os import safe_join
from django.utils.crypto import get_random_string
from django.utils.deconstruct import deconstructible
from django.utils.encoding import filepath_to_uri
from django.utils.functional import LazyObject, cached_property
from django.utils.module_loading import import_string
from django.utils.text import get_valid_filename


# Create your models here.

def upload_to(
    instance, 
    filename):
    return  os.path.join( settings.MEDIA_ROOT , filename )

class FunFileStorage(FileSystemStorage):
    def _save(self, name, content):
        sha256 = hashlib.sha256()
        for chunk in content.chunks():
            sha256.update(chunk)
        name =  sha256.hexdigest() 

        full_path = super().path(name)

        if( os.path.exists( full_path )):
            return name

        return super()._save(name, content)
    

class Checkup(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    file_id = models.UUIDField(help_text='file uuid')
    is_legal = models.BooleanField(default= True , help_text='is legal')
    comment = models.TextField(help_text='comment')
