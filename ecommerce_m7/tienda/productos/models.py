from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    # MinValueValidator(0.01), no 0: el enunciado pide precio MAYOR a 0,
    # no mayor o igual.
    precio = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    # PROTECT, no CASCADE: igual que en el Módulo 5, no debería poder
    # borrarse una categoría que todavía tiene productos asociados.
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='productos'
    )

    def __str__(self):
        return self.nombre


class Stock(models.Model):
    # primary_key=True: la PK de esta tabla ES la FK a producto, no un
    # id autoincremental aparte (relación 1:1 real, igual que en el
    # schema.sql del Módulo 5).
    producto = models.OneToOneField(
        Producto, on_delete=models.CASCADE,
        primary_key=True, related_name='stock'
    )
    cantidad = models.PositiveIntegerField(default=0)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Stock de {self.producto.nombre}: {self.cantidad}'