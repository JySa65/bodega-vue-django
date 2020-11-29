from rest_framework import generics
from rest_framework.response import Response

from apps.generic.models import PriceUsd
from apps.generic.serializers import PriceUsdSerializer
# Create your views here.


class PriceUsdGenericsAPIView(generics.ListAPIView):
    serializer_class = PriceUsdSerializer

    def get_queryset(self):
        return [PriceUsd.objects.last()]
