from django.urls import path
from django.urls.conf import path
from . import views
urlpatterns = [
    # Tạo báo giá
    path('export-pdf/<str:quote>', views.export_to_pdf, name='export_to_pdf'),
    # path('export-csv/<str:product>/<str:volume>/<int:material>/<int:packaging_level1>/<int:packaging_level2>/<int:stamp>/<int:packing_worker>/<int:announced>/<int:feeship>/', views.export_to_csv, name='export_to_pdf'),
    path('tao-bao-gia', views.crete_quote, name="form-quote"),
    path('tao-bao-gia/<str:unique_product>', views.create_quote_from_product, name="create_quote_from_product"),

    #Sản phẩm 
    path('san-pham', views.load_product_list, name="load_product_list"),
    path('san-pham/<slug:slug>', views.get_detail_product, name="detail_product"),
    # path('san-pham/<slug:slug>', views.load_product_category_list, name="load_product_category_list"),

    # Nguyên liệu
    path('nguyen-lieu', views.load_material_list, name='load_material_list'),
    path('nguyen-lieu/<slug:slug>', views.detail_material, name="detail_material"),

    # Bao bì
    path('bao-bi', views.load_packaging_level, name="load_packaging_level"),
    path('bao-bi/<slug:slug>', views.detail_packaging_level1, name="detail_packaging_level1" ),
    path('bao-bi-cap-2', views.list_packaging_level2, name="list_packaging_level2"),
    path('bao-bi-cap-2/<slug:slug>', views.detail_packaging_level2, name="detail_packaging_level2"),

    # API load more data
    path('api/load-more-product/', views.load_more_product, name="load_more_product"),
    # path('api/detail-product/', views.get_detail_product, name = "get_detail_product"),
    path('api/load-more-material/', views.load_more_material, name = "load_more_material"),
    path('api/load-more-packaging/', views.load_more_packaging, name = "load_more_packaging"),
    path('api/load-more-packaging-level2/', views.load_more_packaging_level2, name = "load_more_packaging_level2"),
    # path('api/detail-material/', views.get_detail_material, name = "get_detail_material"),
    # path('api/detail-packaging/', views.get_detail_packaging, name="get_detail_packaging"),

    # API Tạo báo giá tự động
    path('api/load-volume-product/', views.load_volume_product, name="load_volume_product"),
    path('api/load-material/', views.load_material, name="load_material"),
    path('api/load-packaging-level1/', views.load_packaging_level1, name="load_packaging_level1"),
    path('api/load-packaging-level2/', views.load_packaging_level2, name="load_packaging_level2"),
    path('api/load-stamp/', views.load_stamp, name="load_stamp"),
    path('api/load-packing-worker/', views.load_packing_worker, name="load_stamp"),
    path('api/load-announced/', views.load_announced, name="load_announced"),
    path('api/load-feeship/', views.load_feeship, name="load_feeship"),
    path('api/load-quantity-product/', views.load_quantity_product, name="load_quantity_product"),
    path('api/get-param/', views.api_get_param, name="api_get_param"),

    # Khác
    path('lien-he', views.contact, name="contact"),
    path('', views.homepage, name='list_category'),

]
