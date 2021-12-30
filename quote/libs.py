import uuid 
from datetime import date
from django.utils.html import strip_tags
import hashlib

HOME = "HOME"
QUOTE = "QUOTE"
PRODUCT = "PRODUCT"
MATERIAL = "MATERIAL"
PACKAGING_LEVEL1 = "PACKAGING_LEVEL1"
PACKAGING_LEVEL2 = "PACKAGING_LEVEL2"
CREATE_QUOTE = "CREATE_QUOTE"
CONTACT = "CONTACT"
PACKAGING = "PACKAGING"
EMAIL_ADMIN = 'songmv.oni@gmail.com'
LIMIT_PAGE = 12
# Message
MESSAGE_NO_DATA = "<p>Không có dữ liệu hiển thị!</p>"

# Generate unique uid
def generate_uid(tp):
    if(tp=="Volume"):
        return "V"+ uuid.uuid4().hex[:6].upper()+"P"
    else:
        return "P"+ uuid.uuid4().hex[:6].upper()+"V"

def get_upload_to_folder(type):
    return 'media/upload/{0}/{1}/{2}'.format(type,date.today().year, date.today().month)

def serializable(objs):
    arr_result = []
    for obj in objs:
        arr_result.append(obj.to_dict())

    return arr_result

# serializer material
def serializer_material(objs, quantity, obj_volume):
    arr_result = []
    if(obj_volume.type_volume == 'ml'):
        for item in objs:
            item.price = item.price_per_ml * float(quantity*int(obj_volume.number_volume))
            arr_result.append(item.to_dict())
        return arr_result
    else:
        for item in objs:
            item.price = ((float(obj_volume.number_volume)*item.price)/1000.0)*float(quantity)
            arr_result.append(item.to_dict())
        return arr_result

def removed_tags(strs):
    if strs is not None:
        strs.strip()
        return strip_tags(strs)
    return []

def get_md5_sign_key(data=[]):
    hash_md5 = hashlib.md5()
    my_str = ""
    for item in data:
        my_str+=item
    hash_md5.update(my_str.encode('utf-8'))
    return hash_md5.hexdigest()

def get_type_packaging():
    return {
        "Hộp": "Hộp",
        "Chai": "Chai",
        "Lọ": "Lọ"
    }
            