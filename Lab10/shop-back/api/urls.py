"""
api/urls.py
URL configuration for the Online Shop API.

All levels (FBV / CBV / Mixins / Generics) expose the same class names
through api/views/__init__.py, so this file never needs to change when
switching implementation levels.
"""

from django.urls import path
from api.views import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView,
)

urlpatterns = [
    # ── Products ──────────────────────────────────────────────────────────────
    # GET  /api/products/          → list all products
    # POST /api/products/          → create a product
    path('products/', ProductListAPIView.as_view(), name='product-list'),

    # GET    /api/products/<product_id>/  → retrieve
    # PUT    /api/products/<product_id>/  → update
    # DELETE /api/products/<product_id>/  → soft-delete
    path('products/<int:product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),

    # ── Categories ────────────────────────────────────────────────────────────
    # GET  /api/categories/        → list all categories
    # POST /api/categories/        → create a category
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),

    # GET    /api/categories/<category_id>/  → retrieve
    # PUT    /api/categories/<category_id>/  → update
    # DELETE /api/categories/<category_id>/  → delete (blocked if has products)
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view(), name='category-detail'),

    # GET /api/categories/<category_id>/products/  → products in a category
    path('categories/<int:category_id>/products/', CategoryProductsAPIView.as_view(), name='category-products'),
]
