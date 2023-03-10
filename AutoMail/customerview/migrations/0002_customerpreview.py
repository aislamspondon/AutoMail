# Generated by Django 4.1.5 on 2023-02-24 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=100)),
                ('transaction', models.CharField(max_length=100)),
                ('initial_amount', models.CharField(max_length=100)),
                ('total_charges', models.CharField(max_length=100)),
                ('payment_reference', models.CharField(max_length=100)),
            ],
        ),
    ]
