# Generated by Django 3.2.7 on 2021-10-05 21:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("eduhub", "0017_auto_20211006_0009"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AppraisingContent",
            new_name="ASharingContent",
        ),
    ]
