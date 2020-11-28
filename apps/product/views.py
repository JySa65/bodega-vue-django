from rest_framework import generics
from rest_framework.response import Response
from apps.product.models import Product
from apps.product.serializers import ProductSerializer
# Create your views here.


class ProductGenericsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
