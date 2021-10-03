from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import (RichTextUploadingField,
                                      RichTextUploadingFormField)
from django.core.validators import *
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from eduhub.models import Classification


# Create your models here.

class Content(models.Model):
    class Meta:
        verbose_name = _('Content')
        verbose_name_plural = _('Contents')

    def __str__(self):
        return self.name

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(
        max_length=64, blank=False,
        verbose_name=_('Name'))

    title = models.CharField(max_length=64, blank=False,
                             verbose_name=_('Title'))

    classification = models.ForeignKey(
        to=Classification, on_delete=models.SET_NULL,null=True,
        verbose_name=_('Classification'))

    _content = RichTextUploadingField(
        max_length=2048,
        verbose_name=_('Content'))


class Appraising(models.Model):
    class Meta:
        verbose_name = _('Appraising')
        verbose_name_plural = _('Appraisings')

    def __str__(self):
        return self.name

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    content = models.ForeignKey(
        to=Content, on_delete=models.CASCADE,
        verbose_name=_('Content'))
    point = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)])
    comment = models.CharField(
        max_length=64, verbose_name=_('Comment'))
