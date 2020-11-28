from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name