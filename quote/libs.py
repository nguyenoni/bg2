import uuid 
from datetime import date
from django.utils.html import strip_tags

HOME = "HOME"
QUOTE = "QUOTE"
PRODUCT = "PRODUCT"
MATERIAL = "MATERIAL"
PACKAGING_LEVEL1 = "PACKAGING_LEVEL1"
PACKAGING_LEVEL2 = "PACKAGING_LEVEL2"
LIST_PRODUCT_PROCESSING = "LIST_PRODUCT_PROCESSING"
CONTACT = "CONTACT"
EMAIL_ADMIN = 'songmv.oni@gmail.com'
LIMIT_PAGE = 1

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

def removed_tags(strs):
    if strs is not None:
        strs.strip()
        return strip_tags(strs)
    return []
