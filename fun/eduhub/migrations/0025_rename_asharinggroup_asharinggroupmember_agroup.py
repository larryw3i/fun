# Generated by Django 3.2.7 on 2021-10-06 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduhub', '0024_asharingcontent_agroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asharinggroupmember',
            old_name='asharinggroup',
            new_name='agroup',
        ),
    ]