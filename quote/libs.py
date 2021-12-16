import uuid 
from datetime import date
from django.utils.html import strip_tags

import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes #only for AES CBC mode

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

def removed_tags(strs):
    if strs is not None:
        strs.strip()
        return strip_tags(strs)
    return []


key = 'AAAAAAAAAAAAAAAA' #Must Be 16 char for AES128

iv =  'BBBBBBBBBBBBBBBB'.encode('utf-8') #16 char for AES128

def encrypt(data,key,iv):
        data= pad(data.encode(),16)
        cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC,iv)
        return base64.b64encode(cipher.encrypt(data))

def decrypt(enc,key,iv):
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc),16)

def get_decrypt(el):
    decrypted = decrypt(el,key,iv)
    return decrypted.decode("utf-8", "ignore")
# encrypted = encrypt(data)
# print('encrypted ECB Base64:',encrypted.decode("utf-8", "ignore"))

# decrypted = decrypt(encrypted)
# print('data: ',decrypted.decode("utf-8", "ignore"))