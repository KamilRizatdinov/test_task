# Generated by Django 3.0.1 on 2019-12-23 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20191223_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='cityname',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='citytype',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='description',
        ),
    ]
