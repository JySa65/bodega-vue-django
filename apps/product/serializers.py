from rest_framework import serializers
from apps.product.models import Product, Category, Price
# Serializers define the API representation.


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ('price_buy', 'price_sell', 'created_at')


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    price_set = PriceSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('name', 'categories', 'price_set')
