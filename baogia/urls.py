"""baogia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf import urls as conf_urls
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from quote import views
from quote.sitemaps import MaterialSitemap, PackagingLevel1Sitemap, PackagingLevel2Sitemap, ProductSitemap

sitemaps = {
    'product':ProductSitemap,
    'material':MaterialSitemap,
    'packaginglevel1': PackagingLevel1Sitemap,
    'packaginglevel2': PackagingLevel2Sitemap,
}

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path("robots.txt", TemplateView.as_view(template_name="quote/robots.txt", content_type="text/plain"),),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('quote.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
handler404 = views.handler404
handler500 = views.handler500