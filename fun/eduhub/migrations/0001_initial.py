# Generated by Django 3.0.3 on 2020-03-03 07:48

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import funfile.storage
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=64, verbose_name='Label name')),
                ('comment', models.CharField(max_length=64, verbose_name='Label comment')),
                ('cover', models.ImageField(blank=True, upload_to=funfile.storage.upload_to, verbose_name='Label cover')),
                ('creating_date', models.DateTimeField(auto_now_add=True, verbose_name='Label creating date')),
                ('is_legal', models.BooleanField(default=True, verbose_name='Is label legal ?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Label author')),
            ],
            options={
                'verbose_name': 'Eduhub label',
                'verbose_name_plural': 'Eduhub  labels',
            },
        ),
        migrations.CreateModel(
            name='Funcontent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=64, verbose_name='Content title')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('classification', models.CharField(blank=True, max_length=64, null=True, verbose_name='Content classification')),
                ('uploading_date', models.DateTimeField(auto_now_add=True, verbose_name='Content uploading date')),
                ('comment', models.TextField(max_length=64, verbose_name='Content comment')),
                ('is_legal', models.BooleanField(default=True, verbose_name='Is content legal')),
                ('label', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eduhub.Label', verbose_name='Content label')),
            ],
            options={
                'verbose_name': 'Eduhub content (NEW)',
                'verbose_name_plural': 'Eduhub contents (NEW)',
            },
        ),
        migrations.CreateModel(
            name='Funclassification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=64, verbose_name='Classification name')),
                ('level', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Classification level')),
                ('creating_date', models.DateTimeField(auto_now_add=True, verbose_name='Classification creating date')),
                ('is_disabled', models.BooleanField(default=False, verbose_name='Is classification disabled')),
                ('creating_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Classification creating user')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='eduhub.Funclassification', verbose_name='Parent classification')),
            ],
            options={
                'verbose_name': 'Eduhub classification',
                'verbose_name_plural': 'Eduhub classifications',
            },
        ),
        migrations.CreateModel(
            name='Eduhubhomesticker',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='Eduhub homepage sticker title')),
                ('subtitle', models.TextField(max_length=64, verbose_name='Eduhub homepage sticker subtitle')),
                ('cover', models.ImageField(upload_to=funfile.storage.upload_to, verbose_name='Eduhub homepage sicker cover')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('promulgating_date', models.DateTimeField(auto_now_add=True, verbose_name='Eduhub homepage sticker promulgating date')),
                ('comment', models.TextField(max_length=128, verbose_name='Eduhub homepage sticker comment')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='Hidden ?')),
                ('promulgator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Eduhub homepage sticker promulgator')),
            ],
            options={
                'verbose_name': 'Eduhub homepage sticker',
                'verbose_name_plural': 'Eduhub homepage stickers',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=64, verbose_name='Content title')),
                ('content_file', models.FileField(blank=True, upload_to=funfile.storage.upload_to, verbose_name='Content file')),
                ('uploading_date', models.DateTimeField(auto_now_add=True, verbose_name='Content uploading date')),
                ('comment', models.TextField(max_length=64, verbose_name='Content comment')),
                ('is_legal', models.BooleanField(default=True, verbose_name='Is content legal')),
                ('label', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eduhub.Label', verbose_name='Content label')),
            ],
            options={
                'verbose_name': 'Eduhub content',
                'verbose_name_plural': 'Eduhub contents',
            },
        ),
    ]
