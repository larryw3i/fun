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
from django.core.exceptions import ValidationError
from django.core.validators import *
from django.db import models
from django.utils.translation import gettext_lazy as _
from funfile.storage import upload_to
from funuser.models import Funuser

# Create your models here.

label_name = 'label'
funtest_name = 'funtest'
content_name = 'content'
funcontent_name = 'funcontent'
eduhubhomesticker_name = 'eduhubhomesticker'
classification_name = 'classification'


class Classification(models.Model):
    class Meta:
        verbose_name = _('Classification')
        verbose_name_plural = _('Classifications')

    def __str__(self):
        return (
            '' if self.parent is None
            else str(self.parent) + '/'
        ) + _(self.name)

    def clean(self):
        if '/' in self.name:
            raise ValidationError({
                'name': _("name includes '/' is not allowed")})

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
        to=Funuser, on_delete=models.CASCADE, verbose_name=_('Label author'))
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
        to=Label, on_delete=models.SET_NULL, null=True,
        verbose_name=_('Content label'))

    classification = models.ForeignKey(
        to=Classification, blank=True, null=True, on_delete=models.SET_NULL,
        verbose_name=_('Content classification'))

    title = models.CharField(max_length=64, blank=False,
                             verbose_name=_('Content title'))

    content = RichTextUploadingField(max_length=2048,
                                     verbose_name=_('Content'))

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
        to=Funuser, on_delete=models.CASCADE,
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
        to=Funuser, on_delete=models.CASCADE,
        verbose_name=_('Test owner'))

    test_text = models.TextField(
        max_length=12288,
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


class ASharingContent(models.Model):
    class Meta:
        verbose_name = _('Appraising content')
        verbose_name_plural = _('Appraising contents')

    def __str__(self):
        return self.title

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    cfrom = models.ForeignKey(
        to=Funuser, on_delete=models.CASCADE, verbose_name=_('Content from'))

    title = models.CharField(max_length=64, blank=False,
                             verbose_name=_('Title'))

    acontent = RichTextUploadingField(
        max_length=2048,
        verbose_name=_('Content'))

    DOC = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date of appraising content creating'))

    DOU = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Date of appraising content updating'))

    classification = models.ForeignKey(
        to=Classification, on_delete=models.SET_NULL, null=True,
        verbose_name=_('Classification'))

    comment = models.TextField(max_length=128, verbose_name=_(
        'Eduhub homepage sticker comment'))

    is_legal = models.BooleanField(
        default=True, verbose_name=_('Is content legal'))


class Appraising(models.Model):
    class Meta:
        verbose_name = _('Appraising')
        verbose_name_plural = _('Appraisings')

    def __str__(self):
        return self.name

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    afrom = models.ForeignKey(
        to=Funuser,
        on_delete=models.CASCADE,
        verbose_name=_('Appraisings from'))
    content = models.ForeignKey(
        to=ASharingContent, on_delete=models.CASCADE,
        verbose_name=_('Content'))
    point = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)])
    DOA = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date of Appraising'))
    comment = models.CharField(
        max_length=64, verbose_name=_('Comment'))
