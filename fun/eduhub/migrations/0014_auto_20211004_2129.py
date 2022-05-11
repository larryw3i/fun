# Generated by Django 3.2.7 on 2021-10-04 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eduhub", "0013_auto_20211004_2127"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="label",
            name="classification",
        ),
        migrations.AddField(
            model_name="funcontent",
            name="classification",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="eduhub.classification",
                verbose_name="Content classification",
            ),
        ),
    ]
