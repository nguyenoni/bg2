from datetime import datetime
from json.encoder import JSONEncoder
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, resolve_url
from django.http import HttpResponse, request
from django.views import View
from .models import Announced, BannerHome, Category, FeeShipping, ImageMaterial, ImagePackagingLevel1, ImagePackagingLevel2, ImageProduct, Material, PackagingLevel1, PackingWorker, Product, Stamp, Volume, PackagingLevel2, Param
from django.views.generic.detail import DetailView
from . import libs
from django.core.mail import EmailMessage
from django.conf import settings
# import unicodecsv as csv 
from django.template.loader import get_template, render_to_string
# from xhtml2pdf import pisa

# import pdfkit
# from pdfkit.api import configuration
# wkhtml_path = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")  #by using configuration you can add path value.
# from weasyprint import HTML
# Create your views here.


def homepage(request):
    temp = "quote/home.html"
    dt = {
        "active_menu": libs.HOME,
        "error": False,
    }
    try:
        obj_banner = BannerHome.objects.get(id=1)
        obj_product = Product.objects.all().order_by('-id')[:12]
        obj_material = Material.objects.all().order_by('-id')[:12]
        obj_packaging_level1 = PackagingLevel1.objects.all().order_by('-id')[:12]
        obj_packaging_level2 = PackagingLevel2.objects.all().order_by('-id')[:12]

        dt.update({
            "banner_home": obj_banner,
            "data_product": obj_product,
            "data_material": obj_material,
            "data_packaging_level_1": obj_packaging_level1,
            "data_packaging_level_2": obj_packaging_level2
        })
    except ValueError:
        dt.update({
            "error": True,
            "message": "Lỗi hệ thống!"
        })
    return render(request,temp, dt)

# Tạo báo giá từ url sản phẩm
def create_quote_from_product(request, unique_product):
    tmp = "quote/create-quote.html"
    dt = {
        "error": False,
        "message": "",
        "active_menu": libs.CREATE_QUOTE
    }
    if(unique_product):
        try:
            obj_product = Product.objects.get(unique_product = unique_product)
            obj_volume = Volume.objects.all()
            obj_product_list = Product.objects.all()
            dt.update({
                "data": obj_product_list,
                "product_selected": obj_product,
                "volume": obj_volume

            })
        except ValueError:
            dt.update({
                "error": True,
                "message": ValueError.__str__()
            })
    return render(request, tmp, dt)

def crete_quote(request):
    tmp = "quote/create-quote.html"
    
    # obj_category = Category.objects.filter(slug=slug)[0]
    obj_product = Product.objects.all()

    return render(request, tmp, {"data": obj_product, "active_menu": libs.CREATE_QUOTE})

# Export to pdf
def export_to_pdf(request, quote):
    obj_param = Param.objects.get(md5=quote)
    url = obj_param.url
    arr = url.split("-")
    product = arr[0]
    volume = arr[1] 
    material = int(arr[2])
    packaging_level1 = int(arr[3])
    packaging_level2 = int(arr[4])
    stamp = int(arr[5])
    packing_worker = int(arr[6])
    announced = int(arr[7])
    feeship = int(arr[8])
    quantity = int(arr[9])
    name_create = str(arr[10])
    tmp = "quote/export_pdf.html"
    dt = {
        "total": 0,
    }
    if(product and volume and material and quantity and name_create):
        # Gia de tinh tong tien
        p_pklv1 = 0
        p_pklv2 = 0
        p_st = 0
        p_fs = 0
        p_packw = 0
        p_ann = 0
        # Thành tiền
        tt_material = 0
        tt_packaging_level_1 = 0
        tt_packaging_level_2 = 0
        tt_stamp = 0
        tt_packing_worker = 0

        if(packaging_level1 != 0):
            obj_packaging_level1 = PackagingLevel1.objects.get(id=packaging_level1)
            dt.update({
                "packaging_level1": obj_packaging_level1,
            })
            p_pklv1 = obj_packaging_level1.price
            tt_packaging_level_1 = obj_packaging_level1.price *quantity
        if(packaging_level2 != 0):
            obj_packaging_level2 = PackagingLevel2.objects.get(id=packaging_level2)
            dt.update({
                "packaging_level2": obj_packaging_level2,
            })
            p_pklv2 = obj_packaging_level2.price
            tt_packaging_level_2 = obj_packaging_level2.price * quantity
        if(stamp != 0):
            obj_stamp = Stamp.objects.get(id=stamp)
            dt.update({
                "stamp": obj_stamp,
            })
            p_st = obj_stamp.price
            tt_stamp = obj_stamp.price*quantity
        if(packing_worker !=0):
            obj_packing_worker = PackingWorker.objects.get(id=packing_worker)
            dt.update({
                "packing_worker": obj_packing_worker
            })
            p_packw = obj_packing_worker.price
            tt_packing_worker = obj_packing_worker.price*quantity
             
        if(announced != 0):
            obj_announced = Announced.objects.get(id=announced)
            dt.update({
                "announced": obj_announced
            })
            p_ann = obj_announced.price
            
        if(feeship != 0):
            obj_feeship = FeeShipping.objects.get(id=feeship)
            dt.update({
                "feeship": obj_feeship, 
            })
            p_fs = obj_feeship.price
        else:
            pass

        obj_product = Product.objects.filter(unique_product = product)[0]
        price_product = obj_product.price * quantity
        obj_volume = Volume.objects.filter(unique_volume = volume)[0]
        obj_material = Material.objects.get(id=material)

        # Tính giá theo ml hoặc gram người dùng chọn ở phí client
        if(obj_volume.type_volume == 'ml'):       
            obj_material.price = obj_material.price_per_ml * float(quantity*int(obj_volume.number_volume))
        else:
            # 30g x price /1000 (1kg)
            obj_material.price =((float(obj_volume.number_volume)*obj_material.price)/1000.0)*float(quantity)

        tt_material = obj_material.price*quantity
        

        total = (obj_product.price*quantity) + (obj_material.price*quantity) + (p_pklv1*quantity) + (p_pklv2*quantity) + (p_st*quantity) + (p_packw*quantity) + p_ann + p_fs
        dt.update({"product": obj_product, "price_product": price_product,"quantity": quantity, "volume": obj_volume, "material": obj_material, 
         "total": total, "time": str(datetime.now()),
         "tt_material": tt_material,
         "tt_packaging_level_1": tt_packaging_level_1,
         "tt_packaging_level_2": tt_packaging_level_2,
         "tt_stamp": tt_stamp,
         "tt_packing_worker": tt_packing_worker,
         "name_create": name_create,
         })

    return render(request, tmp, dt)

# # export to excell
def export_to_csv(request, product, volume, material, packaging_level1, packaging_level2, stamp, packing_worker, announced, feeship):
  
    
    # if(product and volume and material and packaging_level1 and packaging_level2 and stamp and packing_worker and announced and feeship):
    #     res = HttpResponse(content_type = 'text/csv')
    #     res['Content-Disposition'] = 'attachment; filename=bao-gia-'+str(datetime.now())+'.csv'
    #     res.write(u'\ufeff'.encode('utf8'))
    #     writer = csv.writer(res)
    #     writer.writerow(["STT", " ","Tên", "Số lượng", "Đơn giá", "Thành tiền"])

    #     obj_product = Product.objects.filter(unique_product = product)[0]
    #     obj_volume = Volume.objects.filter(unique_volume = volume)[0]
    #     obj_material = Material.objects.get(id=material)
    #     obj_packaging_level1 = PackagingLevel1.objects.get(id=packaging_level1)
    #     obj_packaging_level2 = PackagingLevel2.objects.get(id=packaging_level2)
    #     obj_stamp = Stamp.objects.get(id=stamp)
    #     obj_packing_worker = PackingWorker.objects.get(id=packing_worker)
    #     obj_announced = Announced.objects.get(id=announced)
    #     obj_feeship = FeeShipping.objects.get(id=feeship)

    #     writer.writerow([1, obj_product.name, "Sản phẩm", 1, obj_product.price, obj_product.price])
    #     writer.writerow([2, obj_volume.name, "Dung tích", 1, obj_volume.name, ""])
    #     writer.writerow([3, obj_material.name, "Nguyên liệu", 1, obj_material.price, obj_material.price])
    #     writer.writerow([4, obj_packaging_level1.name, "Bao bì cấp 1", 1, obj_packaging_level1.price, obj_packaging_level1.price])
    #     writer.writerow([5, obj_packaging_level2.name, "Bao bì cấp 2", 1, obj_packaging_level2.price, obj_packaging_level2.price])
    #     writer.writerow([6, obj_stamp.name, "Tem nhãn", 1, obj_stamp.price, obj_stamp.price])
    #     writer.writerow([7, obj_packing_worker.name, "Nhân công đóng gói", 1, obj_packing_worker.price, obj_packing_worker.price])
    #     writer.writerow([8, obj_feeship.name, "Vận chuyển", 1, obj_feeship.price, obj_feeship.price])
        

    #     return res
    pass

# API get param
def api_get_param(request):
    dt = {
        "error": False
    }
    if(request.method == "POST"):
        slug = request.POST.get('slug', '')
        try:
            if(Param.objects.filter(url = slug).count()== 0):
                # URL chưa có
                obj_param = Param.objects.create(url = slug, md5 = libs.get_md5_sign_key([slug]))
                dt.update({
                    "data": obj_param.to_dict()
                })
            else:
                obj_param = Param.objects.get(url = slug)
                dt.update({
                    "data": obj_param.to_dict()
                })
        except ValueError:
            dt.update({
                "error": True,
                "message": "Hệ thống không thể xử lý yêu cầu, vui lòng thử lại!"
            })
    return JsonResponse(dt)
# API get volume with UID product
def load_volume_product(request):
    contex={
        "status": 200,
        "message": "",
    }
    if(request.method == "POST" and request.POST.get('unique_product')):
        unique_product = request.POST.get('unique_product')
        try:
            obj_product = Product.objects.get(unique_product = unique_product)
            obj_volume = Volume.objects.filter(type_volume = obj_product.type_product)
            contex.update({
                "data": libs.serializable(obj_volume),
                "message": "Load dung tích thành công!"
            })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__(),
            })
        
        
    return JsonResponse({"data": contex})
# API load Material with volume, product id
def load_material(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")
        quantity = int(request.POST.get("quantity", 0))


        try:
            obj_product = Product.objects.get(unique_product=valp)
            obj_volume = Volume.objects.get(unique_volume = valv)
            obj_material = Material.objects.filter(product = obj_product, for_create_quote = True).distinct()
      
            # volume_multi_quantiy = quantity *int(obj_volume.name)
            # print(volume_multi_quantiy)

          
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializer_material(obj_material, quantity, obj_volume),
                "title": "Chọn nguyên liệu"
            })
            if(obj_material.count() == 0):
                contex.update({
                    "data": libs.MESSAGE_NO_DATA,
                })
            return JsonResponse({"data": contex})
        except ValueError:
            contex.update({
                "status": 400,
                "message": "Lỗi hệ thống"
            })
        
    return JsonResponse({"data": contex})

# API load packaging level 1
def load_packaging_level1(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_packaging_level1 = PackagingLevel1.objects.filter(product = obj_product, volume = obj_volume).distinct()
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_packaging_level1),
                "title": "Chọn bao bì cấp 1"
            })
            if(obj_packaging_level1.count() == 0):
                contex.update({
                    "data": libs.MESSAGE_NO_DATA,
                })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})
        
# API load packaging level 2
def load_packaging_level2(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_packaging_level2 = PackagingLevel2.objects.filter(product = obj_product, volume = obj_volume).distinct()
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_packaging_level2),
                "title": "Chọn bao bì cấp 2"
            })
            if(obj_packaging_level2.count() == 0):
                contex.update({
                    "data": libs.MESSAGE_NO_DATA,
                })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})

# API load stamp
def load_stamp(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_stamp = Stamp.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_stamp),
                "title": "Chọn gói tem nhãn"
            })
            if(obj_stamp.count() == 0):
                contex.update({
                    "data": libs.MESSAGE_NO_DATA,
                })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})

# API load Nhân công đóng gói
def load_packing_worker(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_packing_worker = PackingWorker.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_packing_worker),
                "title": "Chọn gói nhân công đóng gói"
            })
            if(obj_packing_worker.count() == 0):
                contex.update({
                    "data": libs.MESSAGE_NO_DATA,
                })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})

# API load load_announced
def load_announced(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST"):
        # valp = request.POST.get("valp","")
        # valv = request.POST.get("valv","")

        try:
            # obj_product = Product.objects.filter(unique_product=valp)[0]
            # obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_announced = Announced.objects.all().distinct()
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_announced),
                "title": "Chọn gói công bố"
            })
            if(obj_announced.count() == 0):
                contex.update({
                    "data": libs.MESSAGE_NO_DATA,
                })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        

    return JsonResponse({"data": contex})

# API load FeeShip
def load_feeship(request):
    contex = {
        "status": 200,
        "message": ""
    }

    if(request.method == "POST"):
        # valp = request.POST.get("valp","")
        # valv = request.POST.get("valv","")

        try:
            # obj_product = Product.objects.filter(unique_product=valp)[0]
            # obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_feeship = FeeShipping.objects.all()
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_feeship),
                "title": "Chọn gói vận chuyển"
            })
            if(obj_feeship.count()==0):
                contex.update({
                    "data": libs.MESSAGE_NO_DATA,
                })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        


    return JsonResponse({"data": contex})

# API load quantity product
def load_quantity_product(request):
    if(request.method == "POST"):
        dt = {
            "error": False,
            "message": "",
        }
        try:
            unique_product = request.POST.get("product", "")
            quantity = request.POST.get("quantity","")
            obj_product = Product.objects.get(unique_product = unique_product)

            if(obj_product):
                dt.update({
                    "data": obj_product.price * float(quantity),
                })

        except ValueError:
            dt.update({
                "error": True,
                "message": ValueError.__str__()
            })
        return JsonResponse(dt)

# Show product
def load_product_list(request):
    tmp = "quote/index.html"
    dt ={
        "error": False,
        "message": "",
        "active_menu": libs.PRODUCT,
        "has_page": False,
        "no_data": False,
        }
    if(request.method == "POST"):
        # load category from select box
        cat = request.POST.get("cateogry", "")
    
        obj_category = Category.objects.get(slug = cat)
        
        total_data = Product.objects.filter(category = obj_category).count()
        obj_product = Product.objects.filter(category = obj_category).order_by('-id')[:libs.LIMIT_PAGE]
        tmp = "quote/includes/product_list.html"
        if(obj_product.count() == 0):
            dt.update({
                "no_data": True,
                "message": libs.MESSAGE_NO_DATA,
            })
        if total_data > obj_product.count():
    
            dt.update({
                "has_page": True,
            })
        temp = render_to_string(tmp,{"data":obj_product, "offset": 0, "has_page": True,} )    
        # obj_category_list = Category.objects.all()
        dt.update({
            "data": temp,
            # "category": obj_category_list,
            "total_data": total_data,
            "limit_page": libs.LIMIT_PAGE
        })

        return JsonResponse(dt)

    else:
        try:
            total_data = Product.objects.count()
            obj_product = Product.objects.all().order_by('-id')[:libs.LIMIT_PAGE]
            if total_data > obj_product.count():
                dt.update({
                    "has_page": True,
                })
            
            obj_category = Category.objects.all()
            dt.update({
                "data": obj_product,
                "category": obj_category,
                "total_data": total_data,
                "limit_page": libs.LIMIT_PAGE
            })
            return render(request, tmp, dt)
        except ValueError:
            dt.update({
                "ERROR": True,
                "message": ValueError.__str__()
            })
        
            return render(request, tmp, dt)


from django.db.models import Q
def load_material_list(request):
    tmp = "quote/material.html"
    dt ={
        "error": False,
        "message": "",
        "active_menu": libs.MATERIAL,
        "has_page": False,
        "no_data": False,
        }
    if(request.method == "POST"):
        # load category from select box
        slug = request.POST.get("slug", "")
        obj_category = Category.objects.get(slug = slug)
        obj_product = Product.objects.filter(category = obj_category)
        obj_material = Material.objects.filter(product__in = obj_product, for_create_quote = False).order_by('-id')[:libs.LIMIT_PAGE]
        # obj_material = get_data_from_product(obj_product)
        total_data = Material.objects.filter(product__in = obj_product, for_create_quote = False).count()
        # obj_material = Material.objects.filter(volume = obj_volume).order_by('-id')[:libs.LIMIT_PAGE]
        
        tmp = "quote/includes/material_list.html"
        if(obj_material.count() == 0):
            dt.update({
                "no_data": True,
                "message": "Không có dữ liệu hiển thị!"
            })
        if total_data > obj_material.count():
    
            dt.update({
                "has_page": True,
            })
        temp = render_to_string(tmp,{"data":obj_material, "offset": 0, "has_page": True,} )    
        # obj_volume_list = Volume.objects.all()
        dt.update({
            "data": temp,
            # "volume": obj_volume_list,
            "total_data": total_data,
            "limit_page": libs.LIMIT_PAGE
        })

        return JsonResponse(dt)

    else:
        try:
            total_data = Material.objects.filter(for_create_quote = False).count()
            obj_material = Material.objects.filter(for_create_quote = False).order_by('-id')[:libs.LIMIT_PAGE]
            if total_data > obj_material.count():
                dt.update({
                    "has_page": True,
                })
            
            obj_volume = Volume.objects.all()
            obj_category = Category.objects.all()
            dt.update({
                "data": obj_material,
                "category": obj_category,
                "volume": obj_volume,
                "total_data": total_data,
                "limit_page": libs.LIMIT_PAGE
            })
            return render(request, tmp, dt)
        except ValueError:
            dt.update({
                "ERROR": True,
                "message": ValueError.__str__()
            })
        
            return render(request, tmp, dt)  

# load more Product API
def load_more_product(request):

    if request.method == "GET":
        dt = {
            "has_page": False,
        }

        try:
            tmp = "quote/includes/product_list.html"
            offset = int(request.GET.get("offset", 0))
            limit = int(request.GET.get("limit", 0))
            data = Product.objects.all().order_by('-id')[offset:offset+limit]
            total_data = Product.objects.count()
            temp = render_to_string(tmp,{"data":data, "offset": int(offset), "has_page": True,} )
            dt.update({
                "data": temp,
                "error": False,
            })
            if total_data > (offset+limit):
                dt.update({
                    "has_page": True,
                })
        except ValueError:
            dt.update({
                "error": True, "status": 400, "message": ValueError.__str__()
            })
        return JsonResponse(dt)
    else:
        dt = {
            "has_page": False,
        }
        try:
            tmp = "quote/includes/product_list.html"
            offset = int(request.POST.get("offset", 0))
            limit = int(request.POST.get("limit", 0))
            cat = request.POST.get("category","")
    
            obj_category = Category.objects.get(slug = cat)
            data = Product.objects.filter(category = obj_category).order_by('-id')[offset:offset+limit]
            total_data = Product.objects.filter(category = obj_category).count()
            
            temp = render_to_string(tmp,{"data":data, "offset": int(offset), "has_page": True,} )
            dt.update({
                "data": temp,
                "error": False,
            })
            if total_data > (offset+limit):
                dt.update({
                    "has_page": True,
                })
            
        except ValueError:
            dt.update({
                "error": True, "status": 400, "message": ValueError.__str__()
            })
        return JsonResponse(dt)

# Load more Material on page material.html
def load_more_material(request):
        if request.method == "GET":
            dt = {
                "has_page": False,
            }
            try:
                tmp = "quote/includes/material_list.html"
                offset = int(request.GET.get("offset", 0))
                limit = int(request.GET.get("limit", 0))
                data = Material.objects.filter(for_create_quote=False).order_by('-id')[offset:offset+limit]
                total_data = Material.objects.filter(for_create_quote=False).count()
                temp = render_to_string(tmp,{"data":data, "offset": int(offset), "has_page": True,} )
                dt.update({
                    "data": temp,
                    "error": False,
                })
                if total_data > (offset+limit):
                    dt.update({
                        "has_page": True,
                    })
                
               
            except ValueError:
                dt.update({
                    "error": True, "status": 400, "message": ValueError.__str__()
                })

            return JsonResponse(dt)
        else:
            dt = {
                "has_page": False,
            }
            try:
                tmp = "quote/includes/material_list.html"
                offset = int(request.POST.get("offset", 0))
                limit = int(request.POST.get("limit", 0))
                # Slug of category
                slug  = request.POST.get("slug", "")
                obj_category = Category.objects.get(slug = slug)
                obj_product = Product.objects.filter(category = obj_category)

                data = Material.objects.filter(product__in = obj_product, for_create_quote=False).order_by('-id')[offset:offset+limit]
                # print(data)
                total_data = Material.objects.filter(product__in = obj_product, for_create_quote = False).count()

                temp = render_to_string(tmp,{"data":data, "offset": int(offset), "has_page": True,} )
                dt.update({
                    "data": temp,
                    "error": False,
                })
                if total_data > (offset+limit):
                    dt.update({
                        "has_page": True,
                    })
                
            except ValueError:
                dt.update({
                    "error": True, "status": 400, "message": "Lỗi hệ thống"
                })

            return JsonResponse(dt)

#API get detail product
def get_detail_product(request, slug):

    dt = {
        "error": False,
        "message": "",
        "active_menu": libs.PRODUCT,
    }
    tmp = "quote/detail_product.html"

    try:
        obj_product = Product.objects.get(slug = slug)
        obj_images = ImageProduct.objects.filter(product = obj_product)
        # temp = render_to_string(tmp, {"data": obj_product})
        dt.update({
            "data": obj_product,
            'images': obj_images
        })

    except ValueError:
        dt.update({
            "error": True,
            "message": ValueError.__str__()
        })
    # return JsonResponse(dt)
    return render(request, tmp, dt)

# Detail material
def detail_material(request, pk):
    dt = {
        "error": False,
        "message": "",
        "active_menu": libs.MATERIAL,
    }
    tmp = "quote/detail_material.html"

    try:
        obj_material = Material.objects.get(id = pk)
        obj_images = ImageMaterial.objects.filter(material = obj_material)
        # temp = render_to_string(tmp, {"data": obj_product})
        dt.update({
            "data": obj_material,
            'images': obj_images
        })

    except ValueError:
        dt.update({
            "error": True,
            "message": ValueError.__str__()
        })
    # return JsonResponse(dt)
    return render(request, tmp, dt)
# get detail packaging level
def detail_packaging_level1(request, pk):
    tmp = "quote/detail_packaging_level1.html"
    dt = {
        "error": False,
        "message": "",
        "active_menu": libs.PACKAGING_LEVEL1
    }
    try:
        obj_packaging_level1 = PackagingLevel1.objects.get(id = pk)
        obj_image = ImagePackagingLevel1.objects.filter(packaginglevel1 = obj_packaging_level1)
        dt.update({
            "data": obj_packaging_level1,
            "images": obj_image
        })

    except ValueError:
        dt.update({
            "error": True,
            "message": ValueError.__str__()
        })

    return render(request, tmp, dt)

# List list_packaging_level_2
def list_packaging_level2(request):
    tmp = "quote/packaging_level2.html"
    dt ={
        "error": False,
        "message": "",
        "active_menu": libs.PACKAGING_LEVEL2,
        "has_page": False,
        "no_data": False,
        }
    if(request.method == "POST"):
        # load category from select box
        unique_v = request.POST.get("volume", "")
        slug_category = request.POST.get("category", "")
        total_data = 0
        obj_packaging = ""

        if(slug_category !='' and unique_v!= ''):
            obj_volume = Volume.objects.get(unique_volume = unique_v)
            obj_category = Category.objects.get(slug = slug_category)
            obj_product = Product.objects.filter(category = obj_category)
            total_data = PackagingLevel2.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().count()
            obj_packaging = PackagingLevel2.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().order_by('-id')[:libs.LIMIT_PAGE]
        elif(slug_category != '' and unique_v ==''):
            obj_category = Category.objects.get(slug = slug_category)
            obj_product = Product.objects.filter(category = obj_category)
            total_data = PackagingLevel2.objects.filter(product__in = obj_product ).distinct().count()
            obj_packaging = PackagingLevel2.objects.filter(product__in = obj_product).distinct().order_by('-id')[:libs.LIMIT_PAGE]
        elif(slug_category =='' and unique_v != ''):
            obj_volume = Volume.objects.get(unique_volume = unique_v)
            total_data = PackagingLevel2.objects.filter(volume = obj_volume).distinct().count()
            obj_packaging = PackagingLevel2.objects.filter(volume = obj_volume).distinct().order_by('-id')[:libs.LIMIT_PAGE]

        tmp = "quote/includes/packaging_level2_list.html"
        if(obj_packaging.count() == 0):
            dt.update({
                "no_data": True,
                "message": "Không có dữ liệu hiển thị!"
            })
        if total_data > obj_packaging.count():
    
            dt.update({
                "has_page": True,
            })
        temp = render_to_string(tmp,{"data":obj_packaging, "offset": 0, "has_page": True,} )    
        # obj_volume_list = Volume.objects.all()
        dt.update({
            "data": temp,
            # "volume": obj_volume_list,
            "total_data": total_data,
            "limit_page": libs.LIMIT_PAGE
        })

        return JsonResponse(dt)

    else:
        try:
            total_data = PackagingLevel2.objects.all().distinct().count()
            obj_packaging = PackagingLevel2.objects.all().distinct().order_by('-id')[:libs.LIMIT_PAGE]
            if total_data > obj_packaging.count():
                dt.update({
                    "has_page": True,
                })
            
            obj_volume = Volume.objects.all()
            obj_category = Category.objects.all()
            dt.update({
                "data": obj_packaging,
                "category": obj_category,
                "volume": obj_volume,
                "total_data": total_data,
                "limit_page": libs.LIMIT_PAGE
            })
            return render(request, tmp, dt)
        except ValueError:
            dt.update({
                "ERROR": True,
                "message": ValueError.__str__()
            })
        
            return render(request, tmp, dt)  

    return render(request, tmp, dt)

# Detail packaging level 2
def detail_packaging_level2(request, pk):
    tmp = "quote/detail_packaging_level2.html"
    dt = {
        "error": False,
        "message": "",
        "active_menu": libs.PACKAGING_LEVEL2
    }
    try:
        obj_packaging_level2 = PackagingLevel2.objects.get(id = pk)
        obj_image = ImagePackagingLevel2.objects.filter(packaginglevel2 = obj_packaging_level2)
        dt.update({
            "data": obj_packaging_level2,
            "images": obj_image
        })

    except ValueError:
        dt.update({
            "error": True,
            "message": ValueError.__str__()
        })

    return render(request, tmp, dt)

# get detail material
def get_detail_material(request):
    dt = {
        "error": False,
        "message": ""
    }
    if(request.method == "GET"):
        tmp = "quote/includes/detail_material.html"
        key = int(request.GET.get("key", 0))
        try:
            obj_material = Material.objects.get(id=key)
            temp = render_to_string(tmp, {"data": obj_material})
            dt.update({
                "data": temp
            })
      
        except ValueError:
            dt.update({
                "error": True,
                "message": ValueError.__str__()
            })
        return JsonResponse(dt)
    

# load_product_category_list
def load_product_category_list(request, slug):
    tmp = "quote/product.html"
    dt = {
        "error": False,
        "message": "",
        "active_menu": libs.PRODUCT,
        "has_page": False,
        "category_selected": ""
    }
    
    try:

        total_data = Product.objects.count()
        obj_category = Category.objects.filter(slug = slug)[0]
        obj_product = Product.objects.filter(category = obj_category)[:libs.LIMIT_PAGE]
        obj_category_list = Category.objects.all()

        if total_data > obj_product.count():
            dt.update({
                "has_page": True,
            })
        dt.update({
            "data": obj_product,
            "category_selected": obj_category,
            "category": obj_category_list,
        })

    except ValueError:
        dt = {
            "error": True,
            "message": ValueError.__str__()
        }
    return render(request, tmp, dt)



# HTTP Error 404
def handler404(request, exception):
    tmp = "quote/404.html"
    return render(request, tmp, status= 404)
def handler500(request):
    return render(request, 'quote/500.html', status=500)

# Contact
def contact(request):
    temp = "quote/contact.html"
    dt = {
        "active_menu": libs.CONTACT,
        "error": False
    }
    if(request.method == "POST"):
        email_request = request.POST.get("email", "")
        name = request.POST.get("name", "")
        phone = request.POST.get("phone","")
        content = request.POST.get("content", "")
        data_info = {
            "email": libs.strip_tags(email_request),
            "phone": libs.strip_tags(phone),
            "name": libs.strip_tags(name),
            "content": libs.strip_tags(content)
        }
        subject = "[THÔNG BÁO] Liên Hệ Mới!"
        email = libs.EMAIL_ADMIN
        tmp_str = "quote/email_template.html"
        body = render_to_string(tmp_str, {"data": data_info})
        dt.update({
            "message": "Chúng tôi đã nhận được liên hệ của bạn và sẽ phản hồi lại trong thời gian sớm nhất!",
        })
        mess = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [email])
        mess.content_subtype = 'html' # this is required because there is no plain text email message
        result_send_email = mess.send()
        # result_send_email = send_mail(subject,body,settings.EMAIL_HOST_USER,[email],fail_silently=True)
        
        if(result_send_email == 0):
            dt.update({
                "error": True,
                "message": "Lỗi! hệ thống đang tạm thời gián đoạn."
            })

        return JsonResponse(dt)
    else:
        return render(request, temp, dt)

# Load packaging level 1
def load_packaging_level(request):
    tmp = "quote/packaging_level.html"
    dt ={
        "error": False,
        "message": "",
        "active_menu": libs.PACKAGING_LEVEL1,
        "has_page": False,
        "no_data": False,
        }
    if(request.method == "POST"):
        # load category from select box
        unique_v = request.POST.get("volume", "")
        slug_category = request.POST.get("category", "")
        total_data = 0
        obj_packaging = ""

        if(slug_category !='' and unique_v!= ''):
            obj_volume = Volume.objects.get(unique_volume = unique_v)
            obj_category = Category.objects.get(slug = slug_category)
            obj_product = Product.objects.filter(category = obj_category)
            total_data = PackagingLevel1.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().count()
            obj_packaging = PackagingLevel1.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().order_by('-id')[:libs.LIMIT_PAGE]
        elif(slug_category != '' and unique_v ==''):
            obj_category = Category.objects.get(slug = slug_category)
            obj_product = Product.objects.filter(category = obj_category)
            total_data = PackagingLevel1.objects.filter(product__in = obj_product ).distinct().count()
            obj_packaging = PackagingLevel1.objects.filter(product__in = obj_product).distinct().order_by('-id')[:libs.LIMIT_PAGE]
        elif(slug_category =='' and unique_v != ''):
            obj_volume = Volume.objects.get(unique_volume = unique_v)
            total_data = PackagingLevel1.objects.filter(volume = obj_volume).distinct().count()
            obj_packaging = PackagingLevel1.objects.filter(volume = obj_volume).distinct().order_by('-id')[:libs.LIMIT_PAGE]

        tmp = "quote/includes/packaging_list.html"
        if(obj_packaging.count() == 0):
            dt.update({
                "no_data": True,
                "message": "Không có dữ liệu hiển thị!"
            })
        if total_data > obj_packaging.count():
    
            dt.update({
                "has_page": True,
            })
        temp = render_to_string(tmp,{"data":obj_packaging, "offset": 0, "has_page": True,} )    
        # obj_volume_list = Volume.objects.all()
        dt.update({
            "data": temp,
            # "volume": obj_volume_list,
            "total_data": total_data,
            "limit_page": libs.LIMIT_PAGE
        })

        return JsonResponse(dt)

    else:
        try:
            total_data = PackagingLevel1.objects.all().distinct().count()
            obj_packaging = PackagingLevel1.objects.all().distinct().order_by('-id')[:libs.LIMIT_PAGE]
            if total_data > obj_packaging.count():
                dt.update({
                    "has_page": True,
                })
            obj_category = Category.objects.all()
            obj_volume = Volume.objects.all()
            dt.update({
                "data": obj_packaging,
                "category": obj_category,
                "volume": obj_volume,
                "total_data": total_data,
                "limit_page": libs.LIMIT_PAGE
            })
            return render(request, tmp, dt)
        except ValueError:
            dt.update({
                "ERROR": True,
                "message": ValueError.__str__()
            })
        
            return render(request, tmp, dt)  

    return render(request, tmp, dt)

# API load detail packaging level
def get_detail_packaging(request):
    dt = {
        "error": False,
        "message": ""
    }
    if(request.method == "GET"):
        tmp = "quote/includes/detail_packaging.html"
        key = int(request.GET.get("key", 0))
        try:
            obj_packaging_level1 = PackagingLevel1.objects.get(id=key)
            temp = render_to_string(tmp, {"data": obj_packaging_level1})
            dt.update({
                "data": temp
            })
      
        except ValueError:
            dt.update({
                "error": True,
                "message": ValueError.__str__()
            })
        return JsonResponse(dt)

# Load more Packaging on page packaging.html
def load_more_packaging(request):
        if request.method == "GET":
            dt = {
                "has_page": False,
            }
            try:
                tmp = "quote/includes/packaging_list.html"
                offset = int(request.GET.get("offset", 0))
                limit = int(request.GET.get("limit", 0))
                slug_category = request.GET.get("category", "")
                unique_v = request.GET.get("volume", "")
                data = ""
                total_data = 0
                if(slug_category !='' and unique_v!= ''):
                    obj_volume = Volume.objects.get(unique_volume = unique_v)
                    obj_category = Category.objects.get(slug = slug_category)
                    obj_product = Product.objects.filter(category = obj_category)
                    total_data = PackagingLevel1.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().count()
                    data = PackagingLevel1.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().order_by('-id')[offset:offset+limit]
                elif(slug_category != '' and unique_v ==''):
                    obj_category = Category.objects.get(slug = slug_category)
                    obj_product = Product.objects.filter(category = obj_category)
                    total_data = PackagingLevel1.objects.filter(product__in = obj_product ).distinct().count()
                    data = PackagingLevel1.objects.filter(product__in = obj_product).distinct().order_by('-id')[offset:offset+limit]
                elif(slug_category =='' and unique_v != ''):
                    obj_volume = Volume.objects.get(unique_volume = unique_v)
                    total_data = PackagingLevel1.objects.filter(volume = obj_volume).distinct().count()
                    data = PackagingLevel1.objects.filter(volume = obj_volume).distinct().order_by('-id')[offset:offset+limit] 
                else:
                    data = PackagingLevel1.objects.all().distinct().order_by('-id')[offset:offset+limit]
                    total_data = PackagingLevel1.objects.all().distinct().count()
                temp = render_to_string(tmp,{"data":data, "offset": int(offset), "has_page": True,} )
                dt.update({
                    "data": temp,
                    "error": False,
                })
                if total_data > (offset+limit):
                    dt.update({
                        "has_page": True,
                    })
                
            except ValueError:
                dt.update({
                    "error": True, "status": 400, "message": ValueError.__str__()
                })

            return JsonResponse(dt)
        else:
            dt = {
                "has_page": False,
            }
            try:
                tmp = "quote/includes/packaging_list.html"
                offset = int(request.POST.get("offset", 0))
                limit = int(request.POST.get("limit", 0))
                slug_category = request.POST.get("category", "")
                unique_v = request.POST.get("volume", "")
                data = ""
                total_data = 0
                if(slug_category !='' and unique_v!= ''):
                    obj_volume = Volume.objects.get(unique_volume = unique_v)
                    obj_category = Category.objects.get(slug = slug_category)
                    obj_product = Product.objects.filter(category = obj_category)
                    total_data = PackagingLevel1.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().count()
                    data = PackagingLevel1.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().order_by('-id')[offset:offset+limit]
                elif(slug_category != '' and unique_v ==''):
                    obj_category = Category.objects.get(slug = slug_category)
                    obj_product = Product.objects.filter(category = obj_category)
                    total_data = PackagingLevel1.objects.filter(product__in = obj_product ).distinct().count()
                    data = PackagingLevel1.objects.filter(product__in = obj_product).distinct().order_by('-id')[offset:offset+limit]
                elif(slug_category =='' and unique_v != ''):
                    obj_volume = Volume.objects.get(unique_volume = unique_v)
                    total_data = PackagingLevel1.objects.filter(volume = obj_volume).distinct().count()
                    data = PackagingLevel1.objects.filter(volume = obj_volume).distinct().order_by('-id')[offset:offset+limit] 

                temp = render_to_string(tmp,{"data":data, "offset": int(offset), "has_page": True,} )
                dt.update({
                    "data": temp,
                    "error": False,
                })
                if total_data > (offset+limit):
                    dt.update({
                        "has_page": True,
                    })
                
               
            except ValueError:
                dt.update({
                    "error": True, "status": 400, "message": ValueError.__str__()
                })

            return JsonResponse(dt)

# load_more_packaging_level2
def load_more_packaging_level2(request):
    if request.method == "GET":
        dt = {
            "has_page": False,
        }
        try:
            tmp = "quote/includes/packaging_level2_list.html"
            offset = int(request.GET.get("offset", 0))
            limit = int(request.GET.get("limit", 0))
            slug_category = request.GET.get("category","")
            unique_v = request.GET.get("volume", "")
            data = ""
            total_data = 0
            if(slug_category !='' and unique_v!= ''):
                obj_volume = Volume.objects.get(unique_volume = unique_v)
                obj_category = Category.objects.get(slug = slug_category)
                obj_product = Product.objects.filter(category = obj_category)
                total_data = PackagingLevel2.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().count()
                data = PackagingLevel2.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().order_by('-id')[offset:offset+limit]
            elif(slug_category != '' and unique_v ==''):
                obj_category = Category.objects.get(slug = slug_category)
                obj_product = Product.objects.filter(category = obj_category)
                total_data = PackagingLevel2.objects.filter(product__in = obj_product ).distinct().count()
                data = PackagingLevel2.objects.filter(product__in = obj_product).distinct().order_by('-id')[offset:offset+limit]
            elif(slug_category =='' and unique_v != ''):
                obj_volume = Volume.objects.get(unique_volume = unique_v)
                total_data = PackagingLevel2.objects.filter(volume = obj_volume).distinct().count()
                data = PackagingLevel2.objects.filter(volume = obj_volume).distinct().order_by('-id')[offset:offset+limit]
            else:
                data = PackagingLevel2.objects.all().distinct().order_by('-id')[offset:offset+limit]
                total_data = PackagingLevel2.objects.all().distinct().count()

            temp = render_to_string(tmp,{"data":data, "offset": int(offset), "has_page": True,} )
            dt.update({
                "data": temp,
                "error": False,
            })
            if total_data > (offset+limit):
                dt.update({
                    "has_page": True,
                })
            
        except ValueError:
            dt.update({
                "error": True, "status": 400, "message": ValueError.__str__()
            })

        return JsonResponse(dt)
    else:
        dt = {
            "has_page": False,
        }
        try:
            tmp = "quote/includes/packaging_level2_list.html"
            offset = int(request.POST.get("offset", 0))
            limit = int(request.POST.get("limit", 0))
            slug_category = request.POST.get("category","")
            unique_v = request.POST.get("volume", "")
            data = ""
            total_data = 0
            if(slug_category !='' and unique_v!= ''):
                obj_volume = Volume.objects.get(unique_volume = unique_v)
                obj_category = Category.objects.get(slug = slug_category)
                obj_product = Product.objects.filter(category = obj_category)
                total_data = PackagingLevel2.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().count()
                data = PackagingLevel2.objects.filter(product__in = obj_product ,volume = obj_volume).distinct().order_by('-id')[offset:offset+limit]
            elif(slug_category != '' and unique_v ==''):
                obj_category = Category.objects.get(slug = slug_category)
                obj_product = Product.objects.filter(category = obj_category)
                total_data = PackagingLevel2.objects.filter(product__in = obj_product ).distinct().count()
                data = PackagingLevel2.objects.filter(product__in = obj_product).distinct().order_by('-id')[offset:offset+limit]
            elif(slug_category =='' and unique_v != ''):
                obj_volume = Volume.objects.get(unique_volume = unique_v)
                total_data = PackagingLevel2.objects.filter(volume = obj_volume).distinct().count()

            temp = render_to_string(tmp,{"data":data, "offset": int(offset), "has_page": True,} )
            dt.update({
                "data": temp,
                "error": False,
            })
            if total_data > (offset+limit):
                dt.update({
                    "has_page": True,
                })
            
            
        except ValueError:
            dt.update({
                "error": True, "status": 400, "message": ValueError.__str__()
            })

        return JsonResponse(dt)


