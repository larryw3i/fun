from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.shortcuts import (Http404, HttpResponseRedirect, redirect, render,
                              reverse)
from django.utils.translation import gettext_lazy as _

from fun import bleach_clean

from .modelforms import ClassificationModelForm
# Register your models here.
from .models import Classification, Eduhubhomesticker, Funcontent, Label


@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):

    list_display = (
        '__str__',
        'comment', )
    form = ClassificationModelForm

    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.name = bleach_clean(obj.name)
        return super().save_model(request, obj, form, change)


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'comment',
        'is_legal']

    readonly_fields = [
        'name',
        'comment', ]

    list_display = (
        'name',
        'author',
        'comment',
        'creating_date',
        'is_legal', )

    list_per_page = 10

    ordering = ('-creating_date',)


@admin.register(Eduhubhomesticker)
class EduhubhomestickerAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subtitle',
        'cover',
        'content',
        'description',
        'comment',
        'is_hidden']

    list_display = (
        'title',
        'promulgator',
        'promulgating_date',
        'is_hidden')

    list_per_page = 10
    ordering = ('-promulgating_date',)
    formfield_overrides = {
        Eduhubhomesticker.title: {
            'widget': forms.TextInput(
                attrs={'autocomplete': 'off'})},
    }

    def save_model(self, request, obj, form, change):
        obj.content = bleach_clean(obj.content)
        obj.promulgator = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Funcontent)
class FuncontentAdmin(admin.ModelAdmin):
    readonly_fields = [
        'title',
        'label__name',
        'content',
        'classification',
        'comment',
        'uploading_date']

    fields = [
        'title',
        'label__name',
        'content',
        'classification',
        'comment',
        'uploading_date',
        'is_legal']

    list_display = (
        'title',
        'label__name',
        'content',
        'comment',
        'uploading_date',
        'classification',
        'is_legal')

    list_per_page = 10

    ordering = ('-uploading_date',)

    def label__name(self, obj):
        return _('None') if obj.label is None else obj.label.name
