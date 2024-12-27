from rest_framework import serializers
from .models import Product, Category, Brand, SubCategory, ProductImage

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "product", "image"]

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False),
        required=False
    )
    availableColors = serializers.ListField(
        child=serializers.CharField(max_length=255),
        required=False
    )

    class Meta:
        model = Product
        fields = [
            "id", "title", "description", "quantity", "sold", "price", "brand", 
            "category", "subcategories", "imageCover", "ratingsQuantity", 
            "images", "uploaded_images", "availableColors", "creatAt", "updateAt"
        ]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        availableColors = validated_data.pop("availableColors", [])
        subcategories = validated_data.pop('subcategories', [])
        
        # إنشاء المنتج
        product = Product.objects.create(**validated_data)
        product.availableColors = availableColors
        product.subcategories.set(subcategories)  
        product.save()

        # إضافة الصور المرتبطة
        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)

        return product

    def update(self, instance, validated_data):
        # معالجة الصور المرفوعة
        uploaded_images = validated_data.pop("uploaded_images", None)
        availableColors = validated_data.pop("availableColors", None)
        subcategories = validated_data.pop('subcategories', None)

        # تحديث البيانات العامة للمنتج
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # تحديث قائمة الألوان إذا تم تقديمها
        if availableColors is not None:
            instance.availableColors = availableColors

        # تحديث التصنيفات الفرعية إذا تم تقديمها
        if subcategories is not None:
            instance.subcategories.set(subcategories)

        instance.save()

        # تحديث الصور إذا تم تقديمها
        if uploaded_images:
            # حذف الصور القديمة المرتبطة بالمنتج
            ProductImage.objects.filter(product=instance).delete()
            # إضافة الصور الجديدة
            for image in uploaded_images:
                ProductImage.objects.create(product=instance, image=image)

        return instance


# class ProductSerializer(serializers.ModelSerializer):
#     images = ProductImageSerializer(many=True, read_only=True)
#     uploaded_images = serializers.ListField(
#         child=serializers.ImageField(max_length=1000000, allow_empty_file=False),
#         write_only=True
        
#     )
#     availableColors = serializers.ListField(
#         child=serializers.CharField(max_length=255),
#         required=False
#     )
    
#     class Meta:
#         model = Product
#         fields = [
#             "id", "title", "description", "quantity", "sold", "price", "brand", 
#             "category", "subcategories", "imageCover", "ratingsQuantity", 
#             "images", "uploaded_images", "availableColors", "creatAt", "updateAt"
#         ]

#     def create(self, validated_data):
#         uploaded_images = validated_data.pop("uploaded_images")
#         availableColors = validated_data.pop("availableColors", [])
#         subcategories = validated_data.pop('subcategories', [])
        
#         product = Product.objects.create(**validated_data)
#         product.availableColors = availableColors
#         product.subcategories.set(subcategories)  
#         product.save()

#         for image in uploaded_images:
#             ProductImage.objects.create(product=product, image=image)

#         return product