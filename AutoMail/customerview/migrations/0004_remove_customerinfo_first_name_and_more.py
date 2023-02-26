# Generated by Django 4.1.5 on 2023-02-26 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customerview', '0003_customerinfo_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinfo',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customerinfo',
            name='last_name',
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=170),
            preserve_default=False,
        ),
    ]