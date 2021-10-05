# Generated by Django 3.2.7 on 2021-10-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduhub', '0016_appraising_appraisingcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='appraisingcontent',
            name='DOU',
            field=models.DateTimeField(auto_now=True, verbose_name='Date of appraising content updating'),
        ),
        migrations.AddField(
            model_name='appraisingcontent',
            name='is_legal',
            field=models.BooleanField(default=True, verbose_name='Is content legal'),
        ),
    ]
