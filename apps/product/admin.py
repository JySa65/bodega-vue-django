from django.contrib import admin
from apps.product.models import Product, Category, Price
# Register your models here.

admin.site.register(Category)
admin.site.register(Price)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_categories')

    def get_categories(self, obj):
        return [item.name for item in obj.categories.all()]
