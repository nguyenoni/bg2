# Generated by Django 3.2.8 on 2022-01-14 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0016_auto_20220113_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=500, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='material',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=500, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='packaginglevel1',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=500, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='packaginglevel2',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=500, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=500, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unique_product',
            field=models.CharField(blank=True, editable=False, max_length=20, unique=True, verbose_name='UID sản phẩm'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='unique_volume',
            field=models.CharField(blank=True, editable=False, max_length=20, unique=True, verbose_name='UID Dung tích'),
        ),
    ]
