# Generated by Django 3.0.3 on 2020-03-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funhome', '0003_auto_20200303_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appreciation',
            name='home_comment',
            field=models.TextField(max_length=64, verbose_name='comment'),
        ),
    ]