# Generated by Django 3.2.8 on 2021-12-28 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0028_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announced',
            name='product',
        ),
        migrations.RemoveField(
            model_name='announced',
            name='volume',
        ),
    ]
