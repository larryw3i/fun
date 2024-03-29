# Generated by Django 3.2.4 on 2021-06-12 14:05

import uuid

import ckeditor_uploader.fields
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
            name="Homesticker",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=32, verbose_name="Sticker title"
                    ),
                ),
                (
                    "subtitle",
                    models.TextField(
                        max_length=64, verbose_name="Sticker subtitle"
                    ),
                ),
                (
                    "cover",
                    models.ImageField(
                        upload_to=funfile.storage.upload_to,
                        verbose_name="Sticker cover",
                    ),
                ),
                (
                    "content_file",
                    models.FileField(
                        upload_to=funfile.storage.upload_to,
                        verbose_name="Sticker content file",
                    ),
                ),
                (
                    "promulgating_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Sticker promulgating date",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        max_length=128, verbose_name="Sticker comment"
                    ),
                ),
                (
                    "is_hidden",
                    models.BooleanField(
                        default=False, verbose_name="隐藏(不贴) ?"
                    ),
                ),
                (
                    "promulgator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Sticker promulgator",
                    ),
                ),
            ],
            options={
                "verbose_name": "Home sticker(deprecation)",
                "verbose_name_plural": "Home sticker(deprecation)",
            },
        ),
        migrations.CreateModel(
            name="Funhomesticker",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=32, verbose_name="Sticker title"
                    ),
                ),
                (
                    "subtitle",
                    models.TextField(
                        max_length=64, verbose_name="Sticker subtitle"
                    ),
                ),
                (
                    "cover",
                    models.ImageField(
                        upload_to=funfile.storage.upload_to,
                        verbose_name="Sticker cover",
                    ),
                ),
                ("content", ckeditor_uploader.fields.RichTextUploadingField()),
                (
                    "promulgating_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Sticker promulgating date",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        max_length=128, verbose_name="Sticker comment"
                    ),
                ),
                (
                    "is_hidden",
                    models.BooleanField(
                        default=False, verbose_name="隐藏(不贴) ?"
                    ),
                ),
                (
                    "promulgator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Sticker promulgator",
                    ),
                ),
            ],
            options={
                "verbose_name": "主页贴纸(NEW)",
                "verbose_name_plural": "主页贴纸(NEW)",
            },
        ),
        migrations.CreateModel(
            name="Appreciation",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "invitee",
                    models.CharField(max_length=8, verbose_name="invitee"),
                ),
                (
                    "invitee_title",
                    models.CharField(
                        max_length=8, verbose_name="invitee title"
                    ),
                ),
                (
                    "brief_comment",
                    models.CharField(
                        max_length=16, verbose_name="brief comment"
                    ),
                ),
                (
                    "illustration",
                    models.ImageField(
                        upload_to=funfile.storage.upload_to,
                        verbose_name="illustration",
                    ),
                ),
                (
                    "home_comment",
                    models.TextField(
                        max_length=128, verbose_name="home comment"
                    ),
                ),
                (
                    "content",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        max_length=4096, verbose_name="appreciation content"
                    ),
                ),
                (
                    "submitting_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Submitting date"
                    ),
                ),
                (
                    "submitter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Submitter",
                    ),
                ),
            ],
            options={
                "verbose_name": "Appreciation",
                "verbose_name_plural": "Appreciation",
            },
        ),
    ]
