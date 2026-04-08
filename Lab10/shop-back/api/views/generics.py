# Level 5: Generic Views (minimal code)
# Inherits directly from DRF generic views — almost no boilerplate needed

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer


# ─────────────────────────────────────────────
#  PRODUCTS
# ─────────────────────────────────────────────

class ProductListAPIView(generics.ListCreateAPIView):
    """
    GET  /api/products/  → list all products
    POST /api/products/  → create a new product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/products/<product_id>/  → retrieve a product
    PUT    /api/products/<product_id>/  → update a product
    DELETE /api/products/<product_id>/  → soft-delete (is_active=False)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

    def perform_destroy(self, instance):
        """Override to soft-delete instead of hard delete."""
        instance.is_active = False
        instance.save()


# ─────────────────────────────────────────────
#  CATEGORIES
# ─────────────────────────────────────────────

class CategoryListAPIView(generics.ListCreateAPIView):
    """
    GET  /api/categories/  → list all categories
    POST /api/categories/  → create a new category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/categories/<category_id>/  → retrieve a category
    PUT    /api/categories/<category_id>/  → update a category
    DELETE /api/categories/<category_id>/  → blocked if category has products
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'

    def perform_destroy(self, instance):
        """Override to block deletion when category has products."""
        if instance.products.exists():
            from rest_framework.exceptions import ValidationError
            raise ValidationError(
                'Cannot delete category because it contains products.'
            )
        instance.delete()


class CategoryProductsAPIView(APIView):
    """
    GET /api/categories/<category_id>/products/  → list products in a category
    Custom view because this endpoint doesn't map 1-to-1 to a generic pattern.
    """

    def get(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response(
                {'error': 'Category not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        products = category.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
