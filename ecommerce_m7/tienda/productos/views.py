from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm, StockForm
from .models import Producto, Stock


@login_required
def lista_productos(request):
    # select_related evita una consulta SQL aparte por cada fila para
    # traer su categoría y su stock (join en una sola query).
    productos = Producto.objects.select_related('categoria', 'stock').all()
    return render(request, 'productos/admin_lista.html', {'productos': productos})


@login_required
def crear_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        stock_form = StockForm(request.POST)
        if producto_form.is_valid() and stock_form.is_valid():
            # atomic: si falla el guardado del stock, el producto
            # recién creado tampoco debe quedar guardado.
            with transaction.atomic():
                producto = producto_form.save()
                stock = stock_form.save(commit=False)
                stock.producto = producto
                stock.save()
            messages.success(request, f'Producto "{producto.nombre}" creado correctamente.')
            return redirect('productos_admin_lista')
        messages.error(request, 'Revisa los errores del formulario.')
    else:
        producto_form = ProductoForm()
        stock_form = StockForm()
    return render(request, 'productos/admin_form.html', {
        'producto_form': producto_form,
        'stock_form': stock_form,
        'titulo': 'Crear producto',
    })


@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    # get_or_create: por si alguna vez existe un producto sin stock
    # (ej. cargado por fixture), evita un error 1-to-1 al editarlo.
    stock, _ = Stock.objects.get_or_create(producto=producto)

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, instance=producto)
        stock_form = StockForm(request.POST, instance=stock)
        if producto_form.is_valid() and stock_form.is_valid():
            with transaction.atomic():
                producto_form.save()
                stock_form.save()
            messages.success(request, f'Producto "{producto.nombre}" actualizado.')
            return redirect('productos_admin_lista')
        messages.error(request, 'Revisa los errores del formulario.')
    else:
        producto_form = ProductoForm(instance=producto)
        stock_form = StockForm(instance=stock)
    return render(request, 'productos/admin_form.html', {
        'producto_form': producto_form,
        'stock_form': stock_form,
        'titulo': 'Editar producto',
    })


@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        nombre = producto.nombre
        producto.delete()
        messages.success(request, f'Producto "{nombre}" eliminado.')
        return redirect('productos_admin_lista')
    # GET: solo muestra la página de confirmación, no borra nada todavía.
    return render(request, 'productos/admin_confirmar_eliminar.html', {'producto': producto})