# Generated by Django 3.2.7 on 2021-10-05 15:49

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eduhub', '0015_alter_funcontent_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppraisingContent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('acontent', ckeditor_uploader.fields.RichTextUploadingField(max_length=2048, verbose_name='Content')),
                ('DOC', models.DateTimeField(auto_now_add=True, verbose_name='Date of appraising content creating')),
                ('comment', models.TextField(max_length=128, verbose_name='Eduhub homepage sticker comment')),
                ('cfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Content from')),
                ('classification', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eduhub.classification', verbose_name='Classification')),
            ],
            options={
                'verbose_name': 'Appraising content',
                'verbose_name_plural': 'Appraising contents',
            },
        ),
        migrations.CreateModel(
            name='Appraising',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('point', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('DOA', models.DateTimeField(auto_now_add=True, verbose_name='Date of Appraising')),
                ('comment', models.CharField(max_length=64, verbose_name='Comment')),
                ('afrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Appraisings from')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduhub.appraisingcontent', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Appraising',
                'verbose_name_plural': 'Appraisings',
            },
        ),
    ]
