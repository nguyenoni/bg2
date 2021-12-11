from django.urls import path
from django.urls.conf import path, re_path
from .views import list_category
from . import views
urlpatterns = [
    
    path('export-pdf/<str:product>/<str:volume>/<int:material>/<int:packaging_level1>/<int:packaging_level2>/<int:stamp>/<int:packing_worker>/<int:announced>/<int:feeship>/', views.export_to_pdf, name='export_to_pdf'),
    path('export-csv/<str:product>/<str:volume>/<int:material>/<int:packaging_level1>/<int:packaging_level2>/<int:stamp>/<int:packing_worker>/<int:announced>/<int:feeship>/', views.export_to_csv, name='export_to_pdf'),
    
    path('san-pham', views.load_product_list, name="load_product_list"),
    path('san-pham/<slug:slug>', views.load_product_category_list, name="load_product_category_list"),
    # API load more data
    path('api/load-more-product/', views.load_more_product, name="load_more_product"),
    path('api/detail-product/', views.get_detail_product, name = "get_detail_product"),
    # API
    path('api/load-volume-product/', views.load_volume_product, name="load_volume_product"),
    path('api/load-material/', views.load_material, name="load_material"),
    path('api/load-packaging-level1/', views.load_packaging_level1, name="load_packaging_level1"),
    path('api/load-packaging-level2/', views.load_packaging_level2, name="load_packaging_level2"),
    path('api/load-stamp/', views.load_stamp, name="load_stamp"),
    path('api/load-packing-worker/', views.load_packing_worker, name="load_stamp"),
    path('api/load-announced/', views.load_announced, name="load_announced"),
    path('api/load-feeship/', views.load_feeship, name="load_feeship"),

    path('', list_category.as_view(), name='list_category'),
    path('<slug:slug>', views.detail_category, name='detail_category'),



    
]
