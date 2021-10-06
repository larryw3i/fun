# Generated by Django 3.2.7 on 2021-10-06 15:52

import funfile.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduhub', '0025_rename_asharinggroup_asharinggroupmember_agroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='asharinggroup',
            name='cover',
            field=models.ImageField(
                blank=True,
                upload_to=funfile.storage.upload_to,
                verbose_name='Group cover'),
        ),
    ]
