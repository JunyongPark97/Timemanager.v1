# Generated by Django 2.1.1 on 2018-12-11 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20181210_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestinfo',
            name='reason',
            field=models.TextField(null=True),
        ),
    ]