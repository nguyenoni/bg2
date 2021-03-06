# Generated by Django 4.0 on 2021-12-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0008_bannerhome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeshipping',
            name='product',
        ),
        migrations.RemoveField(
            model_name='feeshipping',
            name='volume',
        ),
        migrations.AddField(
            model_name='material',
            name='convert_to_ml',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quy đổi 1kg sang ml'),
        ),
        migrations.AddField(
            model_name='material',
            name='for_create_quote',
            field=models.BooleanField(blank=True, default=False, verbose_name='Dành cho tạo bảng giá'),
        ),
        migrations.AddField(
            model_name='material',
            name='price_per_ml',
            field=models.FloatField(blank=True, default=0, verbose_name='Giá 1ml'),
        ),
        migrations.AddField(
            model_name='product',
            name='type_product',
            field=models.CharField(blank=True, choices=[('ml', 'mililit'), ('g', 'gram')], default='ml', max_length=20, verbose_name='Loại sản phẩm'),
        ),
        migrations.AddField(
            model_name='volume',
            name='number_volume',
            field=models.IntegerField(default=0, verbose_name='Dung tích'),
        ),
        migrations.AddField(
            model_name='volume',
            name='type_volume',
            field=models.CharField(blank=True, choices=[('ml', 'mililit'), ('g', 'gram')], default='ml', max_length=20, verbose_name='Loại dung tích'),
        ),
        migrations.RemoveField(
            model_name='packaginglevel1',
            name='product',
        ),
        migrations.AddField(
            model_name='packaginglevel1',
            name='product',
            field=models.ManyToManyField(blank=True, to='quote.Product', verbose_name='Sản phẩm'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='name',
            field=models.CharField(default='', max_length=20, verbose_name='Tên dung tích'),
        ),
    ]
