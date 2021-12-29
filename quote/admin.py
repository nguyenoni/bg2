from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models
from .models import BannerHome, ImagePackagingLevel2,ImagePackagingLevel1,ImageMaterial,ImageProduct,Category, Logo, Product, Volume, Material, PackagingLevel1, PackagingLevel2, Stamp, PackingWorker,Announced,FeeShipping
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","slug", "create_at", "status",]
    search_fields = ('name',)
    ordering = ('id',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price","category","create_at","update_at","status",]
    search_fields = ('name','category')
    ordering = ('id',)

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ["name","number_volume","type_volume","create_at","update_at","status",]
    search_fields = ('name',)
    list_filter = ('create_at', 'status')
    ordering = ('id',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    
    list_display = ["name", "price","product","create_at", "update_at","for_create_quote", "status",]
    list_filter = ('product', 'create_at', 'status')
    search_fields = ('name', 'product', 'volume',)
    ordering = ('id',)

@admin.register(PackagingLevel1)
class PackagingAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "volume", "create_at","update_at", "status",]
    list_filter = ('volume', 'create_at', 'status')
    filter_horizontal = ('product',)
    search_fields = ('name', 'product', 'volume',)
    ordering = ('id',)

@admin.register(PackagingLevel2)
class PackagingLevel2tAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "volume", "create_at", "update_at", "status",]
    list_filter = ('volume', 'create_at', 'status')
    filter_horizontal = ('product',)
    search_fields = ('name', 'product', 'volume',)
    ordering = ('id',)

@admin.register(Stamp)
class StampAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "product", "volume", "create_at", "update_at", "status",]
    list_filter = ('product', 'volume', 'create_at', 'status')
    search_field = ('name', 'product', 'volume',)
    ordering = ('id',)

@admin.register(PackingWorker)
class PackingWorkerAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "product", "volume", "note", "create_at", "update_at", "status",]
    list_filter = ('product', 'volume', 'create_at', 'status')
    search_field = ('name', 'product', 'volume',)
    ordering = ('id',)

@admin.register(Announced)
class AnnouncedAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "note", "create_at", "update_at", "status",]
    list_filter = ('create_at', 'status')
    search_field = ('name', 'product', 'volume',)
    ordering = ('id',)

@admin.register(FeeShipping)
class FeeShippingAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "note", "create_at", "update_at", "status",]
    list_filter = ('create_at', 'status',)
    search_field = ('name',)
    ordering = ('id',)
@admin.register(ImageProduct)
class ImageProductAdmin(admin.ModelAdmin):
    list_display = ["image", "product",]
    list_filter = ('product',)
    search_field = ('product', 'image',)
    ordering = ('id',)

@admin.register(ImageMaterial)
class ImageMaterialAdmin(admin.ModelAdmin):
    list_display = ["image", "material",]
    list_filter = ('material',)
    search_field = ('material', 'image',)
    ordering = ('id',)

@admin.register(ImagePackagingLevel1)
class ImagePackagingLevel1Admin(admin.ModelAdmin):
    list_display = ["image", "packaginglevel1",]
    list_filter = ('packaginglevel1',)
    search_field = ('packaginglevel1', 'image')
    ordering = ('id',)
@admin.register(ImagePackagingLevel2)
class ImagePackagingLevel2Admin(admin.ModelAdmin):
    list_display = ["image", "packaginglevel2",]
    list_filter = ('packaginglevel2',)
    search_field = ('packaginglevel2', 'image',)
    ordering = ('id',)

@admin.register(BannerHome)
class BannerHomeAdmin(admin.ModelAdmin):
    list_display = ['image', "create_at", "status",]
    list_filter = ['image', 'create_at', 'status',]
    search_field = ('image', 'create_at',)
    ordering = ('id',)

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ['image', "create_at",]
    list_filter = ["image", "create_at",]
    search_field = ("image",)
    ordering = ('id',)