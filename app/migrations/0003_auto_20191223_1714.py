# Generated by Django 3.0.1 on 2019-12-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_subject_query_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='id',
        ),
        migrations.AlterField(
            model_name='subject',
            name='query_string',
            field=models.CharField(max_length=13, primary_key=True, serialize=False),
        ),
    ]