# Generated by Django 3.0.1 on 2019-12-23 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='query_type',
        ),
    ]
