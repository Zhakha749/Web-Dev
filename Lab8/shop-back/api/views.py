import json
from django.http import JsonResponse
from django.views import View
from .models import Product, Category


def product_to_dict(product):
    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "count": product.count,
        "is_active": product.is_active,
        "category": product.category.id,
    }


def category_to_dict(category):
    return {
        "id": category.id,
        "name": category.name,
    }


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        data = [product_to_dict(p) for p in products]
        return JsonResponse(data, safe=False)


class ProductDetailView(View):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            return JsonResponse(product_to_dict(product))
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        data = [category_to_dict(c) for c in categories]
        return JsonResponse(data, safe=False)


class CategoryDetailView(View):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
            return JsonResponse(category_to_dict(category))
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)


class CategoryProductsView(View):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
            products = category.products.all()
            data = [product_to_dict(p) for p in products]
            return JsonResponse(data, safe=False)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)
