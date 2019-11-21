from django.contrib import admin

# Register your models here.

from .modelforms import HomestickerModelForm
from .models import Homesticker


@admin.register( Homesticker )
class HomestickerAdmin(admin.ModelAdmin):
    fields = ['title','subtitle', 'cover' ,'content_file', 'comment', 'is_hidden' ] 
    list_display = ( 'title',  'promulgator', 'comment', 'is_hidden' )
    list_per_page = 10
    
    def save_model(self, request, obj, form, change):
        obj.promulgator = request.user
        return super().save_model(request, obj, form, change)