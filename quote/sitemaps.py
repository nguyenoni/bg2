from django.contrib.sitemaps import Sitemap
from .models import Product, Material, PackagingLevel1, PackagingLevel2
from django.urls import reverse

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.update_at
        
    def location(self,obj):
        return '/san-pham/%s' % (obj.slug)

class MaterialSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Material.objects.all()

    def lastmod(self, obj):
        return obj.update_at
        
    def location(self,obj):
        return '/nguyen-lieu/%s' % (obj.id)

class PackagingLevel1Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return PackagingLevel1.objects.all()

    def lastmod(self, obj):
        return obj.update_at
        
    def location(self,obj):
        return '/bao-bi/%s' % (obj.id)

class PackagingLevel2Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return PackagingLevel2.objects.all()

    def lastmod(self, obj):
        return obj.update_at
        
    def location(self,obj):
        return '/bao-bi-cap-2/%s' % (obj.id)
