# Generated by Django 3.2.7 on 2021-10-06 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eduhub", "0020_alter_asgmemberclassification_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="asharinggroupmember",
            old_name="memberclassification",
            new_name="classification",
        ),
        migrations.AddField(
            model_name="asharinggroupmember",
            name="isjudge",
            field=models.BooleanField(
                default=False, verbose_name="Is judge ?"
            ),
        ),
        migrations.AlterField(
            model_name="asharinggroup",
            name="DOC",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Date of creating"
            ),
        ),
    ]
