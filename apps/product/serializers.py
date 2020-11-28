from rest_framework import serializers
from apps.product.models import Product, Category
# Serializers define the API representation.


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('name', 'categories')
