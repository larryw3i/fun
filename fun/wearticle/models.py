
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
import uuid

class Wearticle(models.Model):
	class Meta:
		ordering = ['uploaded_time']

	id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
	title = models.CharField( max_length = 64 , unique = True, help_text = 'title')
	uploaded_time = models.DateTimeField( auto_now_add = True, help_text = 'uploaded time')
	author = models.ForeignKey( to = User, to_field= 'id', on_delete= models.CASCADE, help_text = 'author')
	
	def __str__(self):
	 	return '%s : %s' % (self.id, self.title[0:20])
	

class Comment(models.Model):
	class Meta:
		ordering = ['date_time']
	
	id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
	wearticle = models.ForeignKey(to = Wearticle, to_field= 'id', on_delete = models.CASCADE, help_text = 'article')
	
	user = models.ForeignKey( to = User, to_field= 'id', on_delete= models.CASCADE, help_text = 'user')

	content = models.TextField( max_length = 128,  help_text = 'content')
	like = models.IntegerField( default = 0, help_text = 'like')
	dislike  = models.IntegerField(default = 0, help_text = 'dislike')
	date_time = models.DateTimeField( auto_now_add = True, help_text = 'time')

	def __str__(self):
	 	return '%s : %s' % (self.id, self.content[0:20])

