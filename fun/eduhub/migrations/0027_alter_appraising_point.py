# Generated by Django 3.2.7 on 2021-10-23 16:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eduhub", "0026_asharinggroup_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appraising",
            name="point",
            field=models.SmallIntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
    ]
