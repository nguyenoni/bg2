from django.db import models
from django.db.models.fields.files import ImageField
from .libs import generate_uid, get_upload_to_folder
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên danh mục")
    slug = models.SlugField(unique=True, blank=True, max_length=500,verbose_name="URL")
    create_at = models.DateField(auto_created=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Ngày cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    @staticmethod
    def custom_slugs(slug):
        if slug is not None:
            obj_slug = Category.objects.filter(slug=slug).first()
            if obj_slug:
                return slug + '-' + str(obj_slug.id)
        return slug

    def save(self, *arg, **kwarg):
        self.slug = self.custom_slugs(slugify(self.name))
        super(Category, self).save(*arg, **kwarg)

    class Meta:
        verbose_name = "Danh mục sản phẩm"
        verbose_name_plural = "Danh mục sản phẩm"
        ordering = ['name']


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên sản phẩm")
    unique_product = models.CharField(max_length=20, unique=True, blank=True, verbose_name="UID sản phẩm")
    cover_image = models.ImageField(upload_to=get_upload_to_folder("products"), max_length=512, blank=True, verbose_name="Image")
    slug = models.SlugField(max_length=500, unique=True, blank=True,verbose_name="URL")
    # des= models.TextField(default="", blank=True, verbose_name="Mô tả")
    des = RichTextUploadingField(blank=True, null = True ,verbose_name='Mô tả')
    price = models.FloatField(default=0, verbose_name="Giá")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="category")
    quantity = models.IntegerField(default=0, verbose_name="Số lượng")
    create_at = models.DateTimeField(auto_created=True, verbose_name="Ngày tạo")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")
    
    @staticmethod
    def custom_slugs(slug):
        if slug is not None:
            obj_slug = Category.objects.filter(slug=slug).first()
            if obj_slug:
                return slug + '-' + str(obj_slug.id)
        return slug

    def save(self, *arg, **kwarg):
        self.unique_product = generate_uid("Product")
        self.slug = self.custom_slugs(slugify(self.name))
        super(Product, self).save(*arg, **kwarg)

    class Meta:
        verbose_name = "Sản Phẩm"
        verbose_name_plural = "Sản Phẩm"
        ordering = ['name']

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "slug": self.price,
            "price": self.price,
            "quantity": self.quantity,
            "status": self.status
        }
# Dung tích
class Volume(models.Model):
    name = models.CharField(max_length=50, default= "", verbose_name="Tên dung tích")
    unique_volume = models.CharField(max_length=20, unique=True, blank=True, verbose_name="UID Dung tích")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")
    # product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="volume_product")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

    def save(self, *arg, **kwarg):
        self.unique_volume = generate_uid("Volume")
        super(Volume, self).save(*arg, **kwarg)
    
    class Meta:
        verbose_name = "Dung tích sản phẩm"
        verbose_name_plural = "Dung tích sản phẩm"
        ordering = ['name']

    def to_dict(self):
        return {
            "name": self.name,
            "unique_volume": self.unique_volume,
            "is_activate": self.status,
            "create_at": self.create_at,
            "update_at": self.update_at
        }
    def __str__(self):
        return self.name

# Nguyên liệu
class Material(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên nguyên liệu")
    cover_image = models.ImageField(upload_to=get_upload_to_folder("material"), max_length=512, blank=True, verbose_name="Image")
    price = models.FloatField(default=0, verbose_name="Giá nguyên liệu")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="material_product", verbose_name="Sản phẩm") #nguyên liệu của sản phẩm nào
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="material_volume", verbose_name="Dung tích")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")
    # note = models.TextField(null=True, blank=True, verbose_name="Ghi chú", default="")
    note = RichTextUploadingField(blank=True, null = True ,verbose_name='Ghi chú')
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

    def to_dict(self):
        return {
            "key": self.id,
            "name": self.name,
            "price": self.price,
            "note": self.note,
            "status": self.status,
            "create_at": self.create_at,
            "update_at": self.update_at
        }
    class Meta:
        verbose_name = "Nguyên liệu"
        verbose_name_plural = "Nguyên liệu"
        ordering = ['name']    

    def __str__(self):
        return self.name

# Bao bì cấp 1 Chai lọ
class PackagingLevel1(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên bao bì cấp 1")
    type_packaging = models.CharField(max_length=50, default="", verbose_name="Loại bao bì")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name="packaging_level_1_product")
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Dung tích", related_name="packagin_level1_volume")
    image = models.ImageField(upload_to=get_upload_to_folder("images"), max_length=512, blank=True, verbose_name="Image")
    type_material = models.CharField(max_length=255, default="", verbose_name="Chất liệu")
    quantity_provider_sell = models.IntegerField(default=0, verbose_name="Chất liệu NCC có thể bán")
    min_order = models.IntegerField(default=0, verbose_name="Min order")
    provider = models.CharField(max_length=255, default="", verbose_name="Nhà cung cấp")
    price = models.FloatField(default=0, verbose_name="Giá")
    quantity_can_order_with_price = models.IntegerField(default=0, verbose_name="Số lượng đặt hàng tương ứng với giá")
    time_to_send = models.TextField(default="", verbose_name="Thời gian giao hàng")
    # note = models.TextField(default="", verbose_name="Ghi chú")
    note = RichTextUploadingField(blank=True, null = True ,verbose_name='Ghi chú')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    class Meta:
        verbose_name = "Bao bì cấp 1"
        verbose_name_plural = "Bao bì cấp 1"
        ordering = ['name']

    def to_dict(self):
        return {
            "key": self.id,
            "name": self.name,
            "type_packaging": self.type_packaging,
            # "image": self.image,
            "type_material": self.type_material,
            "quantity_provider_sell": self.quantity_provider_sell,
            "min_order": self.min_order,
            "provider": self.provider,
            "price": self.price,
            "quantity_can_order_with_price": self.quantity_can_order_with_price,
            "time_to_send": self.time_to_send,
            "note": self.note,
            "create_at": self.create_at,
            "update_at": self.update_at,
            "status": self.status
        }

    def __str__(self):
        return self.name

# Bao bì cấp 2 Hộp
class PackagingLevel2(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên bao bì cấp 2")
    image = models.ImageField(upload_to=get_upload_to_folder("images"), max_length=512, blank=True, verbose_name="Image")
    price = models.FloatField(default=0, verbose_name="Giá bao bì")
    type_packaging = models.CharField(max_length=50, default="", verbose_name="Loại bao bì")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="packaging_product", verbose_name="Sản phẩm") #nguyên liệu của sản phẩm nào
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="packaging_volume", verbose_name="Dung tích")
    # note = models.TextField(default="", verbose_name="Ghi chú")
    note = RichTextUploadingField(blank=True, null = True ,verbose_name='Ghi chú')
    status = models.BooleanField(default=True, verbose_name="Trạng thái")
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")

    class Meta:
        verbose_name = "Bao bì cấp 2"
        verbose_name_plural = "Bao bì cấp 2"
        ordering = ['name']

    def to_dict(self):
        return {
            "key": self.id,
            "name": self.name,
            "price": self.price,
            "note": self.note,
            "status": self.status,
            "create_at": self.create_at,
            "update_at": self.update_at
        }

    def __str__(self):
        return self.name

# Tem nhãn
class Stamp(models.Model):
    name = models.CharField(max_length=255, default="",verbose_name="Tên tem nhãn")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="stamp_product", verbose_name="Sản phẩm") #nguyên liệu của sản phẩm nào
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="stamp_volume", verbose_name="Dung tích")
    type_stamp = models.CharField(max_length=255, default="", verbose_name="Loại tem nhãn")
    price = models.FloatField(default=0, verbose_name="Giá")
    # note = models.TextField(default="", verbose_name="Ghi chú")
    note = RichTextUploadingField(blank=True, null = True ,verbose_name='Ghi chú')
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    class Meta:
        verbose_name = "Tem nhãn"
        verbose_name_plural = "Tem nhãn"
        ordering = ['name']

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "key": self.id,
            "name": self.name,
            "type_stamp": self.type_stamp,
            "price": self.price,
            "note": self.note,
            "create_at": self.create_at,
            "update_at": self.create_at,
            "status": self.status
        }

# Nhân công đóng gói
class PackingWorker(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên gói chi phí công nhân đóng gói")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="packing_worker_product", verbose_name="Sản phẩm")
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="packing_worker_volume", verbose_name="Dung tích")
    price = models.FloatField(default=0, verbose_name="Giá")
    # note = models.TextField(default="", verbose_name="Ghi chú")
    note = RichTextUploadingField(blank=True, null = True ,verbose_name='Ghi chú')
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    class Meta:
        verbose_name = "Nhân công đóng gói"
        verbose_name_plural = "Nhân công đóng gói"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            "key": self.id,
            "name": self.name,
            "price": self.price,
            "note": self.note,
            "create_at": self.create_at,
            "update-at": self.update_at,
            "status": self.status
        }

# Công bố kiểm nghiệm
class Announced(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên gói công bố kiểm nghiệm")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="annonced_product", verbose_name="Sản phẩm")
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="annonced_volume", verbose_name="Dung tích")
    price = models.FloatField(default=0, verbose_name="Giá")
    # note = models.TextField(default="", verbose_name="Ghi chú")
    note = RichTextUploadingField(blank=True, null = True ,verbose_name='Ghi chú')
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    class Meta:
        verbose_name = "Công bố kiểm nghiệm"
        verbose_name_plural = "Công bố kiểm nghiệm"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            "key": self.id,
            "name": self.name,
            "price": self.price,
            "note": self.note,
            "create_at": self.create_at,
            "update-at": self.update_at,
            "status": self.status
        }
#Phí vận chuyển
class FeeShipping(models.Model):
    name = models.CharField(max_length=255, default="", verbose_name="Tên gói phí vận chuyển")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="fee_shipping_product", verbose_name="Sản phẩm")
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="fee_shipping_volume", verbose_name="Dung tích")
    price = models.FloatField(default=0, verbose_name="Giá")
    # note = models.TextField(default="", verbose_name="Ghi chú")
    note = RichTextUploadingField(blank=True, null = True ,verbose_name='Ghi chú')
    create_at = models.DateField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    class Meta:
        verbose_name = "Vận chuyển"
        verbose_name_plural = "Vận chuyển"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            "key": self.id,
            "name": self.name,
            "price": self.price,
            "note": self.note,
            "create_at": self.create_at,
            "update-at": self.update_at,
            "status": self.status
        }

# Đếm lượt tạo báo giá
class Quote(models.Model):
    count = models.IntegerField(default=0, verbose_name="lượt tạo báo giá")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="quote_product", verbose_name="Sản phẩm")
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name="quote_volume", verbose_name="Dung tích")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="quote_material", verbose_name="Nguyên liệu")
    packaging_level1 = models.ForeignKey(PackagingLevel1, on_delete=models.CASCADE, related_name="quote_packaging_level1", verbose_name="Bao bì cấp 1")
    packaging_level2 = models.ForeignKey(PackagingLevel2, on_delete=models.CASCADE, related_name="quote_packaging_level2", verbose_name="Bao bì cấp 2")
    stamp = models.ForeignKey(Stamp, on_delete=models.CASCADE, related_name="quote_stamp", verbose_name="Gói tem nhãn")
    packing_worker = models.ForeignKey(PackingWorker, on_delete=models.CASCADE, related_name="quote_packingworker", verbose_name="Gói nhân công đóng gói")
    announced = models.ForeignKey(Announced, on_delete=models.CASCADE, related_name="quote_announced", verbose_name="Gói công bố kiểm nghiệm")
    feeship = models.ForeignKey(FeeShipping, on_delete=models.CASCADE, related_name="quote_feeship", verbose_name="Gói vận chuyển")
    creat_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    update_at = models.DateField(auto_now=True, verbose_name="Cập nhật")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")

    def __str__(self) -> str:
        return self.product
    
    class Meta:
        verbose_name = "Bảng báo giá"
        verbose_name_plural = "Bảng báo giá"
        ordering = ['id']
# Custom url when create quote
class Param(models.Model):
    url = models.TextField(blank=True, verbose_name="URL")
    md5 = models.CharField(blank=True, default="", max_length= 255, verbose_name="MD5")

    def to_dict(self):
        return {
            "url": self.md5,
        }

    class Meta:
        verbose_name = "Bảng url export PDF"
        verbose_name_plural = "Bảng export PDF"
        ordering = ['id']
    
# Hình ảnh sản phẩm
class ImageProduct(models.Model):
    image = models.ImageField(upload_to=get_upload_to_folder("products"), max_length=512, blank=True, verbose_name="Image")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, verbose_name=("Product"), related_name="child_media")

    class Meta:
        verbose_name = "Hình ảnh sản phẩm"
        verbose_name_plural = "Hình ảnh sản phẩm"
        ordering = ['id']
# Hình ảnh Nguyên liệu
class ImageMaterial(models.Model):
    image = models.ImageField(upload_to=get_upload_to_folder("materials"), max_length=512, blank=True, verbose_name="Image")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=False, blank=False, verbose_name=("Material"), related_name="child_media")

    class Meta:
        verbose_name = "Hình ảnh Nguyên liệu"
        verbose_name_plural = "Hình ảnh Nguyên liệu"
        ordering = ['id']

# Hình ảnh Bao bì cấp 1 Chai lọ
class ImagePackagingLevel1(models.Model):
    image = models.ImageField(upload_to=get_upload_to_folder("packaginglevel1"), max_length=512, blank=True, verbose_name="Image")
    packaginglevel1 = models.ForeignKey(PackagingLevel1, on_delete=models.CASCADE, null=False, blank=False, verbose_name=("PackagingLevel1"), related_name="child_media")

    class Meta:
        verbose_name = "Hình ảnh Bao bì cấp 1"
        verbose_name_plural = "Hình ảnh Bao bì cấp 1"
        ordering = ['id']

# Hình ảnh Bao bì cấp 1 Chai lọ
class ImagePackagingLevel2(models.Model):
    image = models.ImageField(upload_to=get_upload_to_folder("packaginglevel1"), max_length=512, blank=True, verbose_name="Image")
    packaginglevel2 = models.ForeignKey(PackagingLevel2, on_delete=models.CASCADE, null=False, blank=False, verbose_name=("PackagingLevel2"), related_name="child_media")

    class Meta:
        verbose_name = "Hình ảnh Bao bì cấp 2"
        verbose_name_plural = "Hình ảnh Bao bì cấp 2"
        ordering = ['id']


class BannerHome(models.Model):
    image = models.ImageField(upload_to=get_upload_to_folder("bannerhome"), max_length=512, blank=True, verbose_name="Image")
    status = models.BooleanField(default=True, verbose_name="Trạng thái")
    create_at = models.DateTimeField(auto_created=True, verbose_name="Ngày tạo")
    
    class Meta:
        verbose_name = "Banner trang chủ"
        verbose_name_plural = "Banner trang chủ"
        ordering = ['id']
