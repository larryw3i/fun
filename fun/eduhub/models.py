from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.utils.translation import gettext as _t
import uuid


class Article( models.Model ):


    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)

    title = models.CharField( max_length = 64 , unique = True, help_text = _t('title') )

    document_file = models.FileField(upload_to = 'eduhub_document_files', help_text = _t('document file') )

    uploaded_time = models.DateTimeField( auto_now_add = True, help_text = _t( 'uploaded time') )

    author = models.ForeignKey( to = User, to_field= 'id', on_delete= models.CASCADE, help_text = _t('author') )

