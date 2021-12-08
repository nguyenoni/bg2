from django.contrib import admin
from django.db import models
from .models import Category, Product, Volume, Material, PackagingLevel1, PackagingLevel2, Stamp, PackingWorker,Announced,FeeShipping
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
    list_display = ["name","product","create_at","update_at","status",]
    search_fields = ('name','product',)
    list_filter = ('product', 'create_at', 'status')
    ordering = ('id',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["name", "price","product", "volume","create_at", "update_at", "status",]
    list_filter = ('product', 'volume', 'create_at', 'status')
    search_fields = ('name', 'product', 'volume',)
    ordering = ('id',)

@admin.register(PackagingLevel1)
class PackagingAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "product", "volume", "create_at","update_at", "status",]
    list_filter = ('product', 'volume', 'create_at', 'status')
    search_fields = ('name', 'product', 'volume',)
    ordering = ('id',)

@admin.register(PackagingLevel2)
class PackagingLevel2tAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "product", "volume", "create_at", "update_at", "status",]
    list_filter = ('product', 'volume', 'create_at', 'status')
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
    list_display = ["name", "price", "product", "volume", "note", "create_at", "update_at", "status",]
    list_filter = ('product', 'volume', 'create_at', 'status')
    search_field = ('name', 'product', 'volume',)
    ordering = ('id',)

@admin.register(FeeShipping)
class FeeShippingAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "product", "volume", "note", "create_at", "update_at", "status",]
    list_filter = ('product', 'volume', 'create_at', 'status')
    search_field = ('name', 'product', 'volume',)
    ordering = ('id',)