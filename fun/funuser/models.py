from django.db import models
import uuid
from django.contrib.auth.models import User
from funfile.storage import upload_to

# Create your models here.

class Funuser(models.Model):
    id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False, unique=True )
    user_id = models.ForeignKey( to= User,  on_delete=models.CASCADE, )

    avatar = models.ImageField( upload_to = upload_to )
    
    birth_date  = models.DateField( blank = True )
    is_birth_date_outward = models.BooleanField( default = False )
    
    address  = models.CharField( blank = True, max_length = 64 )
    is_address_outward = models.BooleanField( default = False )
    
    hometown  = models.CharField( blank = True , max_length = 64 )
    is_hometown_date_outward = models.BooleanField( default = False )
    
    college  = models.CharField( blank = True , max_length = 64 )
    is_college_outward = models.BooleanField( default = False )

    occupation  = models.CharField( blank = True , max_length = 64 )
    is_occupation_outward = models.BooleanField( default = False )

    hobby  = models.CharField( blank = True , max_length = 64 )
    is_hobby_outward = models.BooleanField( default = False )
    
    motto  = models.CharField( blank = True , max_length = 64 )
    is_motto_outward = models.BooleanField( default = False )
    
