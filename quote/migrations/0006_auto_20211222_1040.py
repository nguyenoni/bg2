# Generated by Django 3.2.9 on 2021-12-22 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0005_remove_volume_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='packaginglevel2',
            name='image',
            field=models.ImageField(blank=True, max_length=512, upload_to='media/upload/images/2021/12', verbose_name='Image'),
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=512, upload_to='media/upload/products/2021/12', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_media', to='quote.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Hình ảnh sản phẩm',
                'verbose_name_plural': 'Hình ảnh sản phẩm',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ImagePackagingLevel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=512, upload_to='media/upload/packaginglevel1/2021/12', verbose_name='Image')),
                ('packaginglevel2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_media', to='quote.packaginglevel2', verbose_name='PackagingLevel2')),
            ],
            options={
                'verbose_name': 'Hình ảnh Bao bì cấp 2',
                'verbose_name_plural': 'Hình ảnh Bao bì cấp 2',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ImagePackagingLevel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=512, upload_to='media/upload/packaginglevel1/2021/12', verbose_name='Image')),
                ('packaginglevel1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_media', to='quote.packaginglevel1', verbose_name='PackagingLevel1')),
            ],
            options={
                'verbose_name': 'Hình ảnh Bao bì cấp 1',
                'verbose_name_plural': 'Hình ảnh Bao bì cấp 1',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ImageMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=512, upload_to='media/upload/materials/2021/12', verbose_name='Image')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_media', to='quote.material', verbose_name='Material')),
            ],
            options={
                'verbose_name': 'Hình ảnh Nguyên liệu',
                'verbose_name_plural': 'Hình ảnh Nguyên liệu',
                'ordering': ['id'],
            },
        ),
    ]