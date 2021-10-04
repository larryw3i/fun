import hashlib
import os
import uuid
from functools import partial

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import (RichTextUploadingField,
                                      RichTextUploadingFormField)
from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _
from funfile.storage import upload_to
from django.core.exceptions import ValidationError

# Create your models here.

label_name = 'label'
funtest_name = 'funtest'
content_name = 'content'
funcontent_name = 'funcontent'
eduhubhomesticker_name = 'eduhubhomesticker'
classification_name = 'classification'


class Label(models.Model):

    class Meta:
        verbose_name = _('Eduhub label')
        verbose_name_plural = _('Eduhub  labels')

    def __str__(self):
        return self.name

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(
        max_length=64, blank=False,
        verbose_name=_('Label name'))
    comment = models.CharField(
        max_length=64, verbose_name=_('Label comment'))
    cover = models.ImageField(
        upload_to=upload_to, blank=True, verbose_name=_('Label cover'))
    creating_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Label creating date'))
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name=_('Label author'))
    is_legal = models.BooleanField(
        default=True, verbose_name=_('Is label legal') + " ?")


class Funcontent(models.Model):

    class Meta:
        verbose_name = _('Eduhub content (NEW)')
        verbose_name_plural = _('Eduhub contents (NEW)')

    def __str__(self):
        return self.title

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True)

    label = models.ForeignKey(
        to=Label, on_delete=models.CASCADE, null=True,
        verbose_name=_('Content label'))

    title = models.CharField(max_length=64, blank=False,
                             verbose_name=_('Content title'))

    content = RichTextUploadingField(max_length=2048,
                                     verbose_name=_('Content'))

    classification = models.CharField(
        max_length=64, blank=True, null=True,
        verbose_name=_('Content classification'))

    uploading_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Content uploading date'))
    comment = models.TextField(
        max_length=64, verbose_name=_('Content comment'))
    is_legal = models.BooleanField(
        default=True, verbose_name=_('Is content legal'))


class Eduhubhomesticker(models.Model):
    class Meta:
        verbose_name = _('Eduhub homepage sticker')
        verbose_name_plural = _('Eduhub homepage stickers')

    def __str__(self):
        return self.title

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,)
    title = models.CharField(
        max_length=32,
        verbose_name=_('Eduhub homepage sticker title'))

    subtitle = models.TextField(
        max_length=64,
        verbose_name=_('Eduhub homepage sticker subtitle'))

    cover = models.ImageField(
        upload_to=upload_to,
        verbose_name=_('Eduhub homepage sicker cover'))

    promulgator = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        verbose_name=_('Eduhub homepage sticker promulgator'))

    description = RichTextUploadingField()

    content = RichTextUploadingField()

    promulgating_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Eduhub homepage sticker promulgating date'))

    comment = models.TextField(max_length=128, verbose_name=_(
        'Eduhub homepage sticker comment'))

    is_hidden = models.BooleanField(
        default=False, verbose_name=_('Hidden') + " ?")


class Funtest(models.Model):

    class Meta:
        verbose_name = _('Eduhub Test')
        verbose_name_plural = _('Eduhub Tests')

    def __str__(self):
        return self.name

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4,
        editable=False, unique=True)

    test_title = models.CharField(
        max_length=64, blank=True, null=True,
        verbose_name=_('Test commit'))

    test_owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        verbose_name=_('Test owner'))

    test_text = models.TextField(max_length=12288,
                                 verbose_name=_('Template text'))

    submitting_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Test submitting date'))

    last_modifying_date = models.DateTimeField(
        blank=True, null=True,
        verbose_name=_('Last modifying date'))

    test_commit = models.CharField(
        max_length=64, blank=True, null=True,
        verbose_name=_('Test commit'))


class Classification(models.Model):
    class Meta:
        verbose_name = _('Classification')
        verbose_name_plural = _('Classifications')

    def __str__(self):
        return (self.parent is None and '/' or f'{str(self.parent)}/') + \
        self.name

    def clean(self):
        if '/' in self.name:
            raise ValidationError({
                'name':_("name includes '/' is not allowed")})

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    parent = models.ForeignKey(
        to='self', null=True, blank=True, on_delete=models.CASCADE,
        verbose_name=_('Parent classification'))

    name = models.CharField(
        max_length=64, blank=False,
        verbose_name=_("Classification name('/' cannot be included)"))

    comment = models.CharField(
        null=True, blank=True,
        max_length=64, verbose_name=_('Classification comment'))
