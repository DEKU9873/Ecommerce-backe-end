from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.products_view, name='products'),
    path('products/<int:pk>/', views.product_detail_view, name='product_detail'),
    path('categories/', views.categories_view, name='categories'),
    path('categories/<int:pk>/', views.category_detail_view, name='category_detail'),
    path('brands/', views.brands_view, name='brands'),
    path('brands/<int:pk>/', views.brand_detail_view, name='brand_detail'),
    path('subcategories/', views.subcategories_view, name='subcategories'),
    path('subcategories/<int:pk>/', views.subcategory_detail_view, name='subcategory_detail'),
    path('category/<int:pk>/subcategories/', views.category_subcategories_view, name='category_subcategories'),

]
