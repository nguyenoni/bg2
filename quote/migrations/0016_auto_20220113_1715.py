# Generated by Django 3.2.8 on 2022-01-13 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0015_packaginglevel2_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]