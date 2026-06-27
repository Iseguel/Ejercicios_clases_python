from productos.models import Categoria, Producto, Stock

categorias = {nombre: Categoria.objects.get_or_create(nombre=nombre)[0] for nombre in ['Cuadros', 'Miniaturas', 'Accesorios']}

datos = [('producto_1', 'Cuadro decorativo modelo 1', 15990, 'Cuadros', 8), 
         ('producto_2', 'Cuadro decorativo modelo 2', 22990, 'Cuadros', 5), 
         ('producto_3', 'Cuadro decorativo modelo 3', 18990, 'Cuadros', 10), 
         ('producto_4', 'Miniatura coleccionable 1', 5990, 'Miniaturas', 6), 
         ('producto_5', 'Miniatura coleccionable 2', 7990, 'Miniaturas', 3), 
         ('producto_6', 'Miniatura coleccionable 3', 6490, 'Miniaturas', 9), 
         ('producto_7', 'Miniatura coleccionable 4', 8990, 'Miniaturas', 4), 
         ('producto_8', 'Accesorio decorativo 1', 3990, 'Accesorios', 7), 
         ('producto_9', 'Accesorio decorativo 2', 4990, 'Accesorios', 5), 
         ('producto_10', 'Accesorio decorativo 3', 2990, 'Accesorios', 6)]

for n, d, pr, c, s in datos: p, _ = Producto.objects.get_or_create(nombre=n, defaults={'descripcion': d, 'precio': pr, 'categoria': categorias[c]}); Stock.objects.get_or_create(producto=p, defaults={'cantidad': s})

print(f'Productos: {Producto.objects.count()} | Stock: {Stock.objects.count()} | Categorías: {Categoria.objects.count()}')