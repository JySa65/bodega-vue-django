from django.db import models
from django.db.models import CharField
from django.db.models.functions import Lower

# Create your models here.

CharField.register_lookup(Lower)


class Category(models.Model):
    name = models.CharField("Nombre", max_length=100)
    created_at = models.DateTimeField('Creado el', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Nombre", max_length=10000)
    categories = models.ManyToManyField(Category, verbose_name="Categorias")
    created_at = models.DateTimeField('Creado el', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name


class Price(models.Model):
    price_buy = models.DecimalField(
        'Precio de Compra', max_digits=10, decimal_places=2)
    price_sell = models.DecimalField(
        'Precio de Venta', max_digits=10, decimal_places=2)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Producto")
    created_at = models.DateTimeField('Creado el', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = "Precios"

    def __str__(self):
        return '{} - {}'.format(self.product, self.price_sell)
