from django.contrib import admin

# Register your models here.
from .models import Content, Label

@admin.register( Content )
class HomestickerAdmin(admin.ModelAdmin):
    fields = ['title','label' ,'content_file','comment', 'is_legal' ,  ] 
    list_display = ( 'title',  'label__name',  'uploading_date' , 'is_legal' )
    list_per_page = 10

    def label__name(self, obj):
        return obj.label.name
    
@admin.register( Label )
class HomestickerAdmin(admin.ModelAdmin):
    fields = ['name','comment','cover', 'is_legal'  ] 
    list_display = ( 'name','author','comment', 'creating_date' , 'is_legal' , )
    list_per_page = 10
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)