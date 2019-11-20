from django.contrib import admin

# Register your models here.
from .models import Content, Label

admin.site.register( Content )

admin.site.register( Label )