from django.urls import path
from apps.product.views import ProductGenericsList, CategoryGenericsList


app_name = "products"

urlpatterns = [
    path('', ProductGenericsList.as_view(), name="product-list"),
    path('category/', CategoryGenericsList.as_view(), name="category-list"),
]
