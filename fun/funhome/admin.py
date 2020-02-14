from django.contrib import admin

# Register your models here.

from .modelforms import HomestickerModelForm, FunhomestickerModelForm
from .models import Homesticker, Funhomesticker
from fun.fundef import default_bleach_clean

from django import forms


@admin.register(Homesticker)
class HomestickerAdmin(admin.ModelAdmin):
    fields = ['title', 'subtitle', 'cover', 'content_file',
              'comment', 'is_hidden']
    list_display = ('title',  'promulgator',
                    'promulgating_date', 'is_hidden')
    list_per_page = 10
    ordering = ('-promulgating_date',)

    def save_model(self, request, obj, form, change):
        obj.promulgator = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Funhomesticker)
class HomestickerAdmin(admin.ModelAdmin):
    fields = ['title', 'subtitle', 'cover', 'content', 'comment', 'is_hidden']
    list_display = ('title',  'promulgator',
                    'promulgating_date', 'is_hidden')
    list_per_page = 10
    ordering = ('-promulgating_date',)
    formfield_overrides = {
        Funhomesticker.title: {'widget': forms.TextInput(
            attrs={'autocomplete': 'off'})},
    }

    def save_model(self, request, obj, form, change):
        obj.content = default_bleach_clean(obj.content)
        obj.promulgator = request.user
        return super().save_model(request, obj, form, change)
