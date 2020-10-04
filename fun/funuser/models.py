from django.db import models
import uuid
from django.contrib.auth.models import User
from funfile.storage import upload_to

from django.utils.translation import gettext_lazy as _

from imagekit.models import ImageSpecField
import os
from fun import settings

# Create your models here.


funuser_mame = 'funuser'


class Funuser( models.Model ):

    class Meta:
        verbose_name = _('User information')
        verbose_name_plural = _('User informations')

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(
        to=User,  on_delete=models.CASCADE,  verbose_name=_('User'))

    avatar = models.ImageField(
        upload_to=upload_to, blank=True,  verbose_name=_('Avatar'), )

    full_name = models.CharField(
        blank=True, max_length=64,  verbose_name=_('Full name'))

    birth_date = models.DateField(
        blank=True,  null=True,  verbose_name=_('Brith date'))
    is_birth_date_outward = models.BooleanField(
        default=False,  verbose_name=_('Is outward')+' ?')

    address = models.CharField(
        blank=True, max_length=64,  verbose_name=_('Address'))
    is_address_outward = models.BooleanField(
        default=False,  verbose_name=_('Is outward')+' ?')

    hometown = models.CharField(
        blank=True, max_length=64,  verbose_name=_('Hometown'))
    is_hometown_outward = models.BooleanField(
        default=False,  verbose_name=_('Is outward')+' ?')

    college = models.CharField(
        blank=True, max_length=64,  verbose_name=_('College'))
    is_college_outward = models.BooleanField(
        default=False,  verbose_name=_('Is outward')+' ?')

    occupation = models.CharField(
        blank=True, max_length=64,  verbose_name=_('Occupation'))
    is_occupation_outward = models.BooleanField(
        default=False,  verbose_name=_('Is outward')+' ?')

    hobby = models.CharField(blank=True, max_length=64,
                             verbose_name=_('Hobby'))
    is_hobby_outward = models.BooleanField(
        default=False,  verbose_name=_('Is outward')+' ?')

    motto = models.CharField(blank=True, max_length=64,
                             verbose_name=_('Motto'))
    is_motto_outward = models.BooleanField(
        default=False,  verbose_name=_('Is outward')+' ?')

    creating_date = models.DateTimeField(
        auto_now_add=True,  verbose_name=_('Funuser creating date'))
