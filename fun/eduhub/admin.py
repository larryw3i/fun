from django.contrib import admin

from django.shortcuts import (Http404, HttpResponseRedirect, redirect, render,
                              reverse)
from django.core.exceptions import ValidationError
# Register your models here.
from .models import Content, Label, Funclassification, Eduhubhomesticker

from django import forms
from fun.fundef import default_bleach_clean

@admin.register( Content )
class HomestickerAdmin(admin.ModelAdmin):
    fields = ['title','label' ,'content_file','comment', 'is_legal' ,  ] 
    list_display = ( 'title',  'label__name',  'uploading_date' , 'is_legal' )
    list_per_page = 10

    ordering = ('-uploading_date',)
    
    def label__name(self, obj):
        return obj.label.name
    
@admin.register( Label )
class HomestickerAdmin(admin.ModelAdmin):
    fields = ['name','comment','cover', 'is_legal'  ] 
    list_display = ( 'name','author','comment', 'creating_date' , 'is_legal' , )
    list_per_page = 10
    
    ordering = ('-creating_date',)
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)


@admin.register( Funclassification )
class FunclassificationAdmin( admin.ModelAdmin ):
    fields = ['name','level' ,'parent' , 'is_disabled'] 
    list_display = ( 'name','level', 'creating_date' , 'creating_user' ,'is_disabled', )
    list_per_page = 10
    
    ordering = ('-creating_date',)
    search_fields = ['name','level']
    
    list_filter = [ 'level' ]
    raw_id_fields = ( 'parent' , )

    def save_model(self, request, obj, form, change):
        obj.creating_user = request.user
        return super().save_model(request, obj, form, change)

@admin.register( Eduhubhomesticker )
class EduhubhomestickerAdmin(admin.ModelAdmin):
    fields = ['title','subtitle', 'cover' ,'content', 'comment', 'is_hidden' ] 
    list_display = ( 'title',  'promulgator', 'promulgating_date', 'is_hidden' )
    list_per_page = 10
    ordering = ('-promulgating_date',)
    formfield_overrides = {
        Eduhubhomesticker.title: { 'widget': forms.TextInput( attrs= { 'autocomplete': 'off' } ) },
    }
    
    def save_model(self, request, obj, form, change):
        obj.content = default_bleach_clean( obj.content )
        obj.promulgator = request.user
        return super().save_model(request, obj, form, change)