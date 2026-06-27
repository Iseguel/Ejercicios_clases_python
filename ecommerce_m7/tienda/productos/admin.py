from django.contrib import admin
from .models import Categoria, Producto, Stock


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio']
    list_filter = ['categoria']
    search_fields = ['nombre']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cantidad', 'actualizado_en']