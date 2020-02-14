from django.db import models
import uuid
from funfile.storage import upload_to
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingFormField, \
    RichTextUploadingField

# Create your models here.


homesticker_name = 'homesticker'
funhomesticker_name = 'funhomesticker'


class Homesticker(models.Model):

    class Meta:
        verbose_name = _('Home sticker')
        verbose_name_plural = _('Home sticker')

    def __str__(self):
        return self.title

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,)
    title = models.CharField(max_length=32,  verbose_name=_('Sticker title'))
    subtitle = models.TextField(
        max_length=64, verbose_name=_('Sticker subtitle'))
    cover = models.ImageField(
        upload_to=upload_to, verbose_name=_('Sticker cover'))
    promulgator = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        verbose_name=_('Sticker promulgator'))
    content_file = models.FileField(
        upload_to=upload_to, verbose_name=_('Sticker content file'))
    promulgating_date = models.DateTimeField(
        auto_now_add=True,  verbose_name=_('Sticker promulgating date'))
    comment = models.TextField(
        max_length=128, verbose_name=_('Sticker comment'))
    is_hidden = models.BooleanField(
        default=False, verbose_name=_('Hidden')+" ?")


class Funhomesticker(models.Model):

    class Meta:
        verbose_name = _('Home sticker')+f'({_("NEW")})'
        verbose_name_plural = _('Home stickers')+f'({_("NEW")})'

    def __str__(self):
        return self.title

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,)
    title = models.CharField(max_length=32,
                             verbose_name=_('Sticker title'))
    subtitle = models.TextField(
        max_length=64, verbose_name=_('Sticker subtitle'))
    cover = models.ImageField(
        upload_to=upload_to, verbose_name=_('Sticker cover'))
    promulgator = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        verbose_name=_('Sticker promulgator'))
    content = RichTextUploadingField()
    promulgating_date = models.DateTimeField(
        auto_now_add=True,  verbose_name=_('Sticker promulgating date'))
    comment = models.TextField(
        max_length=128, verbose_name=_('Sticker comment'))
    is_hidden = models.BooleanField(
        default=False, verbose_name=_('Hidden')+" ?")
