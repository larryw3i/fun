from django.contrib import admin

# Register your models here.

from .modelforms import HomestickerModelForm
from .models import Homesticker


admin.site.register( Homesticker )
