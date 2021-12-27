# Generated by Django 3.2.8 on 2021-12-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0021_alter_bannerhome_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='convert_to_ml',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quy đổi 1kg sang ml'),
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
            name='type_volume',
            field=models.CharField(blank=True, choices=[('ml', 'mililit'), ('g', 'gram')], default='ml', max_length=20, verbose_name='Loại dung tích'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='name',
            field=models.IntegerField(default=0, verbose_name='Dung tích'),
        ),
    ]
