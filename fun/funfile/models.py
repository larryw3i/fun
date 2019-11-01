import uuid

from django.db import models


# Create your models here.

class Checkup(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    file_id = models.UUIDField(help_text='file uuid')
    is_legal = models.BooleanField(default= True , help_text='is legal')
    comment = models.TextField(help_text='comment')
