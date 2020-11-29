from rest_framework import generics
from rest_framework.response import Response
from apps.product.models import Product, Category
from apps.product.serializers import ProductSerializer, CategorySerializer
# Create your views here.


class ProductGenericsList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.request.GET.get('category', '')
        product = self.request.GET.get('product', '')
        filters = {}

        if category != '':
            filters['categories__name'] = category
        if product != '':
            filters['name__lower__icontains'] = product
        return Product.objects.filter(**filters).order_by('name')


class CategoryGenericsList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
