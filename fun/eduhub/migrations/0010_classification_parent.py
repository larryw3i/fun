# Generated by Django 3.2.7 on 2021-10-04 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eduhub', '0009_remove_classification_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eduhub.classification', verbose_name='Parent classification ID'),
        ),
    ]
