import os
import csv
from io import StringIO
from decimal import Decimal
from django.http import HttpResponseRedirect
from django.urls import path, reverse_lazy
from django.contrib import admin
from django import forms
from apps.product.models import Product, Category, Price
# Register your models here.

admin.site.register(Category)


class PriceStackInline(admin.StackedInline):
    model = Price
    extra = 1


class CsvUploadForm(forms.Form):
    csv_file = forms.FileField()

    def clean_csv_file(self):
        csv_file = self.cleaned_data['csv_file']
        _, ext = os.path.splitext(csv_file.name)
        if ext != '.csv':
            raise forms.ValidationError("Not allowed filetype!")
        return csv_file


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    change_list_template = "admin/upload_csv_changelist.html"
    list_display = ('name', 'get_categories',
                    'get_prices_buy', 'get_prices_sell')
    search_fields = ('name',)
    list_filter = ('name',)
    readonly_fields = ('created_at',)

    inlines = (PriceStackInline, )

    def get_categories(self, obj):
        return [item.name for item in obj.categories.all()]

    def get_prices_buy(self, obj):
        data = obj.price_set.last()
        return getattr(data, 'price_buy') if data else 0

    def get_prices_sell(self, obj):
        data = obj.price_set.last()
        return getattr(data, 'price_sell') if data else 0

    get_categories.short_description = "Categorias"
    get_prices_buy.short_description = "Precios de compra"
    get_prices_sell.short_description = "Precios de venta"

    def get_urls(self):
        urls = super().get_urls()
        additional_urls = [
            path("upload-csv/", self.upload_csv),
        ]
        return additional_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra = extra_context or {}
        extra["csv_upload_form"] = CsvUploadForm()
        return super(ProductAdmin, self).changelist_view(request, extra_context=extra)

    def upload_csv(self, request):
        if request.method == "POST":
            form = CsvUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES["csv_file"]
                csvf = StringIO(csv_file.read().decode())
                reader = csv.reader(csvf, delimiter=',', skipinitialspace=True)
                for row in reader:
                    col1, col2, col3 = row
                    if col1 != '':
                        1150000, 00
                        col2 = col2.replace(',', '.') if col2 != '' else 0
                        col3 = col3.replace(',', '.') if col3 != '' else 0
                        product = Product.objects.create(name=col1)
                        Price.objects.create(
                            price_buy=Decimal(col2), price_sell=Decimal(col3), product=product)
        return HttpResponseRedirect(reverse_lazy('admin:product_product_changelist'))


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'price_buy', 'created_at')
    search_fields = ('product__name',)
    list_filter = ('product',)
    readonly_fields = ('created_at',)
