# Generated by Django 3.2.7 on 2021-10-04 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("eduhub", "0003_classification"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="funclassification",
            name="creating_user",
        ),
        migrations.RemoveField(
            model_name="funclassification",
            name="parent",
        ),
        migrations.DeleteModel(
            name="Content",
        ),
        migrations.DeleteModel(
            name="Funclassification",
        ),
    ]
