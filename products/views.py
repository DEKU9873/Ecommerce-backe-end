from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Brand, SubCategory
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer, SubCategorySerializer
from rest_framework import status
from django.db import IntegrityError
from .pagination import CustomPagination
from .filters import ProductFilter

# عرض واضافة وحذف المنتجات
@api_view(['GET', 'POST', 'DELETE'])
def products_view(request):
    if request.method == 'GET':
        filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by('id'))
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(filterset.qs, request)
        serializer = ProductSerializer(result_page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Product.objects.all().delete()
        return Response({"message": "All products have been deleted."}, status=status.HTTP_200_OK)

# عرض وتعديل وحذف المنتج
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        serializer = ProductSerializer(product, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"data":serializer.data})
            except IntegrityError:
                return Response({"error": "Database integrity error"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except IntegrityError:
            return Response({"error": "Cannot delete product due to dependencies"}, status=status.HTTP_400_BAD_REQUEST)

# عرض واضافة وحذف الماركات
@api_view(['GET', 'POST', 'DELETE'])
def brands_view(request):
    if request.method == 'GET':
        brands = Brand.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(brands, request)
        serializer = BrandSerializer(result_page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Brand.objects.all().delete()
        return Response({"message": "All brands have been deleted."}, status=status.HTTP_200_OK)

# عرض وتعديل وحذف الماركة
@api_view(['GET', 'PUT', 'DELETE'])
def brand_detail_view(request, pk):
    brand = get_object_or_404(Brand, pk=pk)

    if request.method == 'GET':
        serializer = BrandSerializer(brand)
        return Response({"data":serializer.data})

    elif request.method == 'PUT':
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            brand.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except IntegrityError:
            return Response({"error": "Cannot delete brand due to dependencies"}, status=status.HTTP_400_BAD_REQUEST)

# عرض واضافة وحذف التصنيفات
@api_view(['GET', 'POST', 'DELETE'])
def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(categories, request)
        serializer = CategorySerializer(result_page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Category.objects.all().delete()
        return Response({"message": "All categories have been deleted."}, status=status.HTTP_200_OK)

# عرض وتعديل وحذف التصنيف
@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response({"data":serializer.data})

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except IntegrityError:
            return Response({"error": "Cannot delete category due to dependencies"}, status=status.HTTP_400_BAD_REQUEST)

# عرض واضافة وحذف التصنيفات الفرعية
@api_view(['GET', 'POST', 'DELETE'])
def subcategories_view(request):
    if request.method == 'GET':
        subcategories = SubCategory.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(subcategories, request)
        serializer = SubCategorySerializer(result_page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        SubCategory.objects.all().delete()
        return Response({"message": "All subcategories have been deleted."}, status=status.HTTP_200_OK)

# عرض وتعديل وحذف التصنيف الفرعية
@api_view(['GET', 'PUT', 'DELETE'])
def subcategory_detail_view(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)

    if request.method == 'GET':
        serializer = SubCategorySerializer(subcategory)
        return Response({"data":serializer.data})

    elif request.method == 'PUT':
        serializer = SubCategorySerializer(subcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            subcategory.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except IntegrityError:
            return Response({"error": "Cannot delete subcategory due to dependencies"}, status=status.HTTP_400_BAD_REQUEST)
        

# عرض واضافة تصنيف فرعي في تصنيف رئيسي
@api_view(['GET', 'POST'])
def category_subcategories_view(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'GET':
        subcategories = SubCategory.objects.filter(category=category)
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response({"data": serializer.data})

    elif request.method == 'POST':
        data = request.data.copy()  
        data['category'] = category.id  
        serializer = SubCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

