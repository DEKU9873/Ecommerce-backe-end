from django.db import models

# نموذج التصنيفات
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    creatAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

# نموذج التصنيفات الفرعية   
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    creatAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

# نموذج الماركات
class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand_images/', null=True, blank=True)
    creatAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# نموذج المنتجات  
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    sold = models.IntegerField(default=0, blank=True, null=True) 
    image = models.ImageField(upload_to = 'img',  blank = True, null=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategories = models.ManyToManyField(SubCategory, blank=True)
    imageCover = models.ImageField(upload_to='imageCover/', null=True, blank=True)
    ratingsQuantity = models.IntegerField(default=0, blank=True, null=True)
    creatAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    availableColors = models.JSONField(default=list, blank=True)  

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)