# api/views/_fbv_adapter.py
#
# Adapter that wraps FBV functions so they expose .as_view() like CBV/Generics.
# This lets urls.py use the same "XxxView.as_view()" pattern for all levels.
#
# @api_view-decorated functions already ARE callables that Django can route to,
# but they don't have a .as_view() method. This adapter adds that interface.

from rest_framework.views import APIView


class _FBVAdapter:
    """
    Wraps an @api_view function so that calling .as_view() returns the
    function itself (which is already a view callable after @api_view).
    """
    def __init__(self, fbv_func):
        self._func = fbv_func

    def as_view(self, **kwargs):
        return self._func


# Import the raw FBV functions
from api.views.fbv import (
    products_list,
    product_detail,
    categories_list,
    category_detail,
    category_products,
)

# Wrap them so they behave like CBV classes in urls.py
ProductListAPIView     = _FBVAdapter(products_list)
ProductDetailAPIView   = _FBVAdapter(product_detail)
CategoryListAPIView    = _FBVAdapter(categories_list)
CategoryDetailAPIView  = _FBVAdapter(category_detail)
CategoryProductsAPIView = _FBVAdapter(category_products)
