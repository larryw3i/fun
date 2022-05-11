# Generated by Django 3.2.4 on 2021-06-12 14:06

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Checkup",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("file_id", models.UUIDField(help_text="file uuid")),
                (
                    "is_legal",
                    models.BooleanField(default=True, help_text="is legal"),
                ),
                ("comment", models.TextField(help_text="comment")),
            ],
        ),
    ]
