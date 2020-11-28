from django.urls import path
from apps.product.views import ProductGenericsList


app_name = "products"

urlpatterns = [
    path('', ProductGenericsList.as_view(), name="product-list"),
]
