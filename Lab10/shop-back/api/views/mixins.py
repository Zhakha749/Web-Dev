# Level 4: Mixin-Based Views
# Combines DRF Mixins with GenericAPIView — delegates to built-in mixin methods

from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer


# ─────────────────────────────────────────────
#  PRODUCTS
# ─────────────────────────────────────────────

class ProductListAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """
    GET  /api/products/  → self.list()   (ListModelMixin)
    POST /api/products/  → self.create() (CreateModelMixin)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    """
    GET    /api/products/<product_id>/  → self.retrieve()
    PUT    /api/products/<product_id>/  → self.update()
    DELETE /api/products/<product_id>/  → soft-delete (is_active=False)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'   # maps URL param <product_id> to pk lookup

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # Custom soft-delete instead of self.destroy()
        product = self.get_object()
        product.is_active = False
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ─────────────────────────────────────────────
#  CATEGORIES
# ─────────────────────────────────────────────

class CategoryListAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """
    GET  /api/categories/  → self.list()
    POST /api/categories/  → self.create()
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetailAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    """
    GET    /api/categories/<category_id>/  → self.retrieve()
    PUT    /api/categories/<category_id>/  → self.update()
    DELETE /api/categories/<category_id>/  → blocked if category has products
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'  # maps URL param <category_id> to pk lookup

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        if category.products.exists():
            return Response(
                {'error': 'Cannot delete category because it contains products.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.destroy(request, *args, **kwargs)


class CategoryProductsAPIView(APIView):
    """
    GET /api/categories/<category_id>/products/  → list products of a category
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
