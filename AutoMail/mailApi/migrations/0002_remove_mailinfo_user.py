# Generated by Django 4.1.5 on 2023-02-23 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailinfo',
            name='user',
        ),
    ]