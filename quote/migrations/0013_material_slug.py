# Generated by Django 3.2.8 on 2022-01-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0012_auto_20220113_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True, verbose_name='URL'),
        ),
    ]
