# Generated by Django 2.1.1 on 2018-12-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_requestinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choicestatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '대기중'), (1, '수락'), (2, '거절')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='requestinfo',
            name='breaktime',
            field=models.IntegerField(default=0),
        ),
    ]
