from rest_framework import serializers
from apps.product.models import Product
# Serializers define the API representation.


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name',)
