from django.contrib import admin
from apps.generic.models import PriceUsd
# Register your models here.


@admin.register(PriceUsd)
class PriceUsdModelAmin(admin.ModelAdmin):
    list_display = ('get_price_page', 'price_sell', 'created_at',)
    readonly_fields = ('created_at',)

    def get_price_page(self, obj):
        return "1 $ = {}".format(obj.price_page)

    get_price_page.short_description = "Precio de Pagina"
