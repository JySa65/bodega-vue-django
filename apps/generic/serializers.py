from rest_framework import serializers
from apps.generic.models import PriceUsd
# Serializers define the API representation.


class PriceUsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceUsd
        fields = ('price_page',
                  'price_sell',
                  'created_at',)
