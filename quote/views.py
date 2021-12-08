from datetime import datetime
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View
from .models import Announced, Category, FeeShipping, Material, PackagingLevel1, PackingWorker, Product, Stamp, Volume, PackagingLevel2
from django.views.generic.detail import DetailView
from . import libs
import unicodecsv as csv

from django.template.loader import get_template
from xhtml2pdf import pisa


# from weasyprint import HTML
# Create your views here.

class list_category(View):

    def get(self, request):
        tmp = "quote/category.html"
        obj_category = Category.objects.all()
        if(obj_category):
            return render(request, tmp, {"data": obj_category})


def detail_category(request, slug):
    tmp = "quote/create-quote.html"
    if(slug and Category.objects.filter(slug = slug)[0]):
        obj_category = Category.objects.filter(slug=slug)[0]
        obj_product = Product.objects.filter(category = obj_category)

    return render(request, tmp, {"data": obj_product})

# Export to pdf
def export_to_pdf(request, product, volume, material, packaging_level1, packaging_level2, stamp, packing_worker, announced, feeship):
    tmp = "quote/export_pdf.html"
    
    if(product and volume and material and packaging_level1 and packaging_level2 and stamp and packing_worker and announced and feeship):
    
        # obj_product = Product.objects.filter(unique_product = product)[0]
        # obj_volume = Volume.objects.filter(unique_volume = volume)[0]
        # obj_material = Material.objects.get(id=material)
        # obj_packaging_level1 = PackagingLevel1.objects.get(id=packaging_level1)
        # obj_packaging_level2 = PackagingLevel2.objects.get(id=packaging_level2)
        # obj_stamp = Stamp.objects.get(id=stamp)
        # obj_packing_worker = PackingWorker.objects.get(id=packing_worker)
        # obj_announced = Announced.objects.get(id=announced)
        # obj_feeship = FeeShipping.objects.get(id=feeship)

            template_path = 'quote/export_pdf.html'
            context = {'myvar': 'this is your template context'}
            # Create a Django response object, and specify content_type as pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=bao-gia-'+ str(datetime.now())+'.pdf'
            # find the template and render it.
            template = get_template(template_path)
            html = template.render(context)

            # create a pdf
            pisa_status = pisa.CreatePDF(html.encode('utf-8'), dest=response, encoding = 'utf-8')
            # if error then show some funy view
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
            # where is_export is being used?
       
        

        # return response

    return render(request, tmp, {})
# export to excell
def export_to_csv(request, product, volume, material, packaging_level1, packaging_level2, stamp, packing_worker, announced, feeship):
  
    
    if(product and volume and material and packaging_level1 and packaging_level2 and stamp and packing_worker and announced and feeship):
        res = HttpResponse(content_type = 'text/csv')
        res['Content-Disposition'] = 'attachment; filename=bao-gia-'+str(datetime.now())+'.csv'
        res.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(res)
        writer.writerow(["STT", " ","Tên", "Số lượng", "Đơn giá", "Thành tiền"])

        obj_product = Product.objects.filter(unique_product = product)[0]
        obj_volume = Volume.objects.filter(unique_volume = volume)[0]
        obj_material = Material.objects.get(id=material)
        obj_packaging_level1 = PackagingLevel1.objects.get(id=packaging_level1)
        obj_packaging_level2 = PackagingLevel2.objects.get(id=packaging_level2)
        obj_stamp = Stamp.objects.get(id=stamp)
        obj_packing_worker = PackingWorker.objects.get(id=packing_worker)
        obj_announced = Announced.objects.get(id=announced)
        obj_feeship = FeeShipping.objects.get(id=feeship)

        writer.writerow([1, obj_product.name, "Sản phẩm", 1, obj_product.price, obj_product.price])
        writer.writerow([2, obj_volume.name, "Dung tích", 1, obj_volume.name, ""])
        writer.writerow([3, obj_material.name, "Nguyên liệu", 1, obj_material.price, obj_material.price])
        writer.writerow([4, obj_packaging_level1.name, "Bao bì cấp 1", 1, obj_packaging_level1.price, obj_packaging_level1.price])
        writer.writerow([5, obj_packaging_level2.name, "Bao bì cấp 2", 1, obj_packaging_level2.price, obj_packaging_level2.price])
        writer.writerow([6, obj_stamp.name, "Tem nhãn", 1, obj_stamp.price, obj_stamp.price])
        writer.writerow([7, obj_packing_worker.name, "Nhân công đóng gói", 1, obj_packing_worker.price, obj_packing_worker.price])
        writer.writerow([8, obj_feeship.name, "Vận chuyển", 1, obj_feeship.price, obj_feeship.price])
        

        return res


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
