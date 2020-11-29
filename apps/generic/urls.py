from django.urls import path
from apps.generic.views import PriceUsdGenericsAPIView


app_name = "generic"

urlpatterns = [
    path('price-usd', PriceUsdGenericsAPIView.as_view(), name="generic-priceusd"),
]
