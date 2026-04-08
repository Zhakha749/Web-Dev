# api/views/__init__.py
#
# This file controls WHICH implementation level is currently active.
# To switch levels, change the single import block below:
#
#   Level 2 (FBV):      uncomment the FBV block
#   Level 3 (CBV):      uncomment the CBV block
#   Level 4 (Mixins):   uncomment the Mixins block
#   Level 5 (Generics): uncomment the Generics block  ← ACTIVE
#
# All levels expose the same names and support .as_view() so urls.py
# never needs to change when switching implementation levels.
#
# NOTE: FBV functions decorated with @api_view already have .as_view()
#       built-in — but to keep the interface uniform we wrap them in a
#       tiny helper class below.

# ── ACTIVE LEVEL: 5 — Generic Views ──────────────────────────────────────────
from api.views.generics import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView,
)

# ── To switch to Level 4 (Mixins), replace the block above with: ─────────────
# from api.views.mixins import (
#     ProductListAPIView,
#     ProductDetailAPIView,
#     CategoryListAPIView,
#     CategoryDetailAPIView,
#     CategoryProductsAPIView,
# )

# ── To switch to Level 3 (CBV), replace the block above with: ────────────────
# from api.views.cbv import (
#     ProductListAPIView,
#     ProductDetailAPIView,
#     CategoryListAPIView,
#     CategoryDetailAPIView,
#     CategoryProductsAPIView,
# )

# ── To switch to Level 2 (FBV), replace the block above with: ────────────────
# from api.views._fbv_adapter import (
#     ProductListAPIView,
#     ProductDetailAPIView,
#     CategoryListAPIView,
#     CategoryDetailAPIView,
#     CategoryProductsAPIView,
# )
