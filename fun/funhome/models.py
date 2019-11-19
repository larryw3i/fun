from django.db import models
import uuid
from funfile.storage import upload_to
from django.contrib.auth.models import User

# Create your models here.


class Homesticker(models.Model):

    id = models.UUIDField( primary_key=True, default= uuid.uuid4, editable=False, )
    title = models.CharField( max_length = 64 )
    cover = models.ImageField( upload_to = upload_to )
    promulgator = models.ForeignKey(  to = User, on_delete=models.CASCADE, )    
    content = models.FileField( upload_to = upload_to )
    promulgating_date = models.DateTimeField(   auto_now_add = True,)
