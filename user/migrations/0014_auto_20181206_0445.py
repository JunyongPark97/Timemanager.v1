# Generated by Django 2.1.1 on 2018-12-06 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_timelog_half_day_off'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelog',
            name='half_day_off',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
