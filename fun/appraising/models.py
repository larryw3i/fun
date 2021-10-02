from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import (RichTextUploadingField,
                                      RichTextUploadingFormField)
from django.core.validators import *
from django.db import models


# Create your models here.
def default_classification():
    return Classification(
        id='00000000-0000-0000-0000-000000000000',
        name='default')

def default_secondary_classification():
    return SecondaryClassification(
        id='00000000-0000-0000-0000-000000000000',
        name='default'
    )


class Classification(models.Model):
    class Meta:
        verbose_name = _('Appraising Classification')
        verbose_name_plural = _('Appraising Classifications')

    def __str__(self):
        return self.name

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(
        max_length=64, blank=False,
        verbose_name=_('Classification name'))
    comment = models.CharField(
        max_length=64, verbose_name=_('Classification comment'))


class SecondaryClassification(models.Model):
    class Meta:
        verbose_name = _('Secondary Classification')
        verbose_name_plural = _('Secondary Classifications')

    def __str__(self):
        return self.name

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    classification = models.ForeignKey(
        to=Classification, on_delete=models.SET_DEFAULT,
        default=default_classification,
        verbose_name=_('Classification'))
    name = models.CharField(
        max_length=64, blank=False,
        verbose_name=_('Secondary classification name'))
    comment = models.CharField(
        max_length=64, verbose_name=_('Secondary classification comment'))


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
    secondary_classification = models.ManyToManyField(
        to=SecondaryClassification,
        verbose_name=_('Secondary classification'))

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
        to=Content, on_delete=models.CASCADE
        verbose_name=_('Content'))
    point = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)])
    comment = models.CharField(
        max_length=64, verbose_name=_('Comment'))
