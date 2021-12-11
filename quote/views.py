from datetime import datetime
from json.encoder import JSONEncoder
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View
from .models import Announced, Category, FeeShipping, Material, PackagingLevel1, PackingWorker, Product, Stamp, Volume, PackagingLevel2
from django.views.generic.detail import DetailView
from . import libs
# import unicodecsv as csv 
from django.template.loader import get_template, render_to_string
# from xhtml2pdf import pisa

# import pdfkit
# from pdfkit.api import configuration
# wkhtml_path = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")  #by using configuration you can add path value.
# from weasyprint import HTML
# Create your views here.

class list_category(View):

    def get(self, request):
        tmp = "quote/category.html"
        obj_category = Category.objects.all()
        if(obj_category):
            return render(request, tmp, {"data": obj_category, "active_menu":libs.LIST_PRODUCT_PROCESSING})


def detail_category(request, slug):
    tmp = "quote/create-quote.html"
    if(slug and Category.objects.filter(slug = slug)[0]):
        obj_category = Category.objects.filter(slug=slug)[0]
        obj_product = Product.objects.filter(category = obj_category)

    return render(request, tmp, {"data": obj_product, "active_menu": libs.LIST_PRODUCT_PROCESSING})

# Export to pdf
def export_to_pdf(request, product, volume, material, packaging_level1, packaging_level2, stamp, packing_worker, announced, feeship):
    tmp = "quote/export_pdf.html"
    
    if(product and volume and material and packaging_level1 and packaging_level2 and stamp and packing_worker and announced and feeship):
    
        obj_product = Product.objects.filter(unique_product = product)[0]
        # obj_volume = Volume.objects.filter(unique_volume = volume)[0]
        obj_material = Material.objects.get(id=material)
        obj_packaging_level1 = PackagingLevel1.objects.get(id=packaging_level1)
        obj_packaging_level2 = PackagingLevel2.objects.get(id=packaging_level2)
        obj_stamp = Stamp.objects.get(id=stamp)
        obj_packing_worker = PackingWorker.objects.get(id=packing_worker)
        obj_announced = Announced.objects.get(id=announced)
        obj_feeship = FeeShipping.objects.get(id=feeship)
        tmp = "quote/export_pdf.html"

        return render(request, tmp, {"product": obj_product, "material": obj_material, "packaging_level1": obj_packaging_level1, "packaging_level2": obj_packaging_level2, 
        "stamp": obj_stamp, "packing_worker": obj_packing_worker, "announced": obj_announced, "feeship": obj_feeship})
# export to excell
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


# API get volume with UID product
def load_volume_product(request):
    contex={
        "status": 200,
        "message": "",
    }
    if(request.method == "POST" and request.POST.get('unique_product')):
        unique_product = request.POST.get('unique_product')
        try:
            obj_product = Product.objects.filter(unique_product = unique_product)[0]
            obj_volume = Volume.objects.filter(product = obj_product)
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

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_material = Material.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_material),
                "title": "Chọn nguyên liệu"
            })
            return JsonResponse({"data": contex})
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
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
            obj_packaging_level1 = PackagingLevel1.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_packaging_level1),
                "title": "Chọn bao bì cấp 1"
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
            obj_packaging_level2 = PackagingLevel2.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_packaging_level2),
                "title": "Chọn bao bì cấp 2"
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

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_announced = Announced.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_announced),
                "title": "Chọn gói công bố"
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

    if(request.method == "POST" and request.POST.get("valp") and request.POST.get("valv")):
        valp = request.POST.get("valp","")
        valv = request.POST.get("valv","")

        try:
            obj_product = Product.objects.filter(unique_product=valp)[0]
            obj_volume = Volume.objects.filter(unique_volume = valv)[0]
            obj_feeship = FeeShipping.objects.filter(product = obj_product, volume = obj_volume)
            contex.update({
                "message": "Load dữ liệu thành công!",
                "data": libs.serializable(obj_feeship),
                "title": "Chọn gói vận chuyển"
            })
        except ValueError:
            contex.update({
                "status": 400,
                "message": ValueError.__str__()
            })
        


    return JsonResponse({"data": contex})

# Show product
def load_product_list(request):
    tmp = "quote/product.html"
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
                "message": "Không có dữ liệu hiển thị!"
            })
        if total_data > obj_product.count():
    
            dt.update({
                "has_page": True,
            })
        temp = render_to_string(tmp,{"data":obj_product, "offset": 0, "has_page": True,} )    
        obj_category_list = Category.objects.all()
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
            

            return JsonResponse(dt)
        except ValueError:
            dt.update({
                "error": True, "status": 400, "message": ValueError.__str__()
            })
            return JsonResponse(dt)

#API get detail product
def get_detail_product(request):

    dt = {
        "error": False,
        "message": "",
    }
    if(request.method == "GET"):
        tmp = "quote/includes/detail_product.html"
        slug = request.GET.get("slug", "")
        try:
            obj_product = Product.objects.get(slug = slug)
            temp = render_to_string(tmp, {"data": obj_product})
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

# HTTP Error 400
def bad_request(request):
    return render(request, 'quote/layout/400.html', {})


# HTTP Error 403
def permission_denied(request):
    return render(request, 'quote/layout/403.html', {})


# HTTP Error 404
def page_not_found(request, exception, template_name="quote/layout/404.html"):
    return render(request, template_name, {})


# HTTP Error 500
def server_error(request):
    return render(request, 'quote/layout/500.html', {})