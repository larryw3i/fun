# Generated by Django 3.2.4 on 2021-06-12 14:06

import uuid

import django.db.models.deletion
import funfile.storage
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Funuser",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        upload_to=funfile.storage.upload_to,
                        verbose_name="Avatar",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="Full name"
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Brith date"
                    ),
                ),
                (
                    "is_birth_date_outward",
                    models.BooleanField(default=False, verbose_name="公开 ?"),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="Address"
                    ),
                ),
                (
                    "is_address_outward",
                    models.BooleanField(default=False, verbose_name="公开 ?"),
                ),
                (
                    "hometown",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="Hometown"
                    ),
                ),
                (
                    "is_hometown_outward",
                    models.BooleanField(default=False, verbose_name="公开 ?"),
                ),
                (
                    "college",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="College"
                    ),
                ),
                (
                    "is_college_outward",
                    models.BooleanField(default=False, verbose_name="公开 ?"),
                ),
                (
                    "occupation",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="Occupation"
                    ),
                ),
                (
                    "is_occupation_outward",
                    models.BooleanField(default=False, verbose_name="公开 ?"),
                ),
                (
                    "hobby",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="Hobby"
                    ),
                ),
                (
                    "is_hobby_outward",
                    models.BooleanField(default=False, verbose_name="公开 ?"),
                ),
                (
                    "motto",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="Motto"
                    ),
                ),
                (
                    "is_motto_outward",
                    models.BooleanField(default=False, verbose_name="公开 ?"),
                ),
                (
                    "creating_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Funuser creating date"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "User information",
                "verbose_name_plural": "User informations",
            },
        ),
    ]
