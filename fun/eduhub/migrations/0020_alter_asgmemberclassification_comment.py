# Generated by Django 3.2.7 on 2021-10-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "eduhub",
            "0019_asgmemberclassification_asharinggroup_asharinggroupmember",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="asgmemberclassification",
            name="comment",
            field=models.CharField(
                blank=True,
                max_length=64,
                null=True,
                verbose_name="Classification Comment",
            ),
        ),
    ]
