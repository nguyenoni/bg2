# Generated by Django 3.2.8 on 2022-01-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0014_packaginglevel1_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='packaginglevel2',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True, verbose_name='URL'),
        ),
    ]
