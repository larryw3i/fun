from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.utils.translation import gettext as _t
from django.utils.translation import gettext as _
import uuid
from django.core import validators
from django.core.exceptions import ValidationError
from math import pow
from djangovalidators.validators import *

from .validators import *
import os
from django import forms


media_file_help_text = _t('document file')+" ("+_t('.pdf, video/* only')+", "+_t("pdf size less than %d Mib, others size less than %d Mib")%(pdf_document_max_size/pow(1024,2), video_max_size/pow(1024,2) )+")"

eduhub_document_file_dir ='eduhub_document_files'

media_file_validators= [   validators.FileExtensionValidator(['pdf', 'mp4', 'mov', 'mkv' ,'webm',]) ]

def media_file_upload_to (instance, filename):
    return os.path.join( eduhub_document_file_dir, str(instance.id) + os.path.splitext( ( filename ) )[1] ) 


class Article( models.Model ):

    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)

    title = models.CharField( max_length = 64 , unique = True, help_text = _t('title') )

    uploaded_time = models.DateTimeField( auto_now_add = True, help_text = _t( 'uploaded time') )

    author = models.ForeignKey( to = User, to_field= 'id', on_delete= models.CASCADE, help_text = _t('author') )

    media_file = models.FileField( upload_to = media_file_upload_to,  validators= media_file_validators ,  help_text = media_file_help_text )

    is_forbade = models.BooleanField( default= False,  help_text = _('is forbade'))


