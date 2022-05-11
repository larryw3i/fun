# Generated by Django 3.2.7 on 2021-10-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eduhub", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eduhubhomesticker",
            name="is_hidden",
            field=models.BooleanField(default=False, verbose_name="Hidden ?"),
        ),
        migrations.AlterField(
            model_name="label",
            name="is_legal",
            field=models.BooleanField(
                default=True, verbose_name="Is label legal ?"
            ),
        ),
    ]
