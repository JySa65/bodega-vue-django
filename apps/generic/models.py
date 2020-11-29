from django.db import models

# Create your models here.


class PriceUsd(models.Model):
    price_page = models.DecimalField(
        'Precio de Pagina', max_digits=10, decimal_places=2)
    price_sell = models.DecimalField(
        'Precio de Venta', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField('Creado el', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Precio Dolar'
        verbose_name_plural = "Precio Dolares"

    def __str__(self):
        return '{} - {}'.format(self.price_page, self.price_sell)
