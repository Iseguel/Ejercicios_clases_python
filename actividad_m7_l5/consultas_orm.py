#------------------------------------------------------------------
# consultas_orm.py
# Actividad N°5 - Consultas Personalizadas con ORM y SQL en Django
#------------------------------------------------------------------

from biblioteca.models import Libro
from django.db import connection
from django.db.models import Count
# Todos los imports van al inicio del archivo (PEP8), no solo el del modelo,
# para que sea fácil ver de un vistazo qué módulos usa el script.

#------------------------------------------------------------------
# 1. Recuperación de registros
#------------------------------------------------------------------

# Recupera todos los libros registrados.
# .all() devuelve un QuerySet "lazy": no consulta la BBDD hasta que se
# itera, imprime o convierte a lista, lo que evita consultas innecesarias.
libros = Libro.objects.all()

# Recupera solo los libros cuyo autor sea "Gabriel García Márquez".
# Se usa filter() en vez de comparar en Python porque así el filtrado
# ocurre en la BBDD (WHERE autor = ...) y no traemos registros de más.
libros_gabriel = Libro.objects.filter(autor="Gabriel García Márquez")

# Recupera los libros que tienen más de 200 páginas.
# El "__gt" (greater than) se traduce a "WHERE paginas > 200"
# directamente en SQL, evitando filtrar en memoria con Python.
libros_paginas = Libro.objects.filter(paginas__gt=200)

#------------------------------------------------------------------
# 2. Filtros y exclusiones
#------------------------------------------------------------------

# Aplica un filtro para mostrar solo libros disponibles.
# disponible=True compara directamente contra el BooleanField del modelo.
libros_disponibles = Libro.objects.filter(disponible=True)

# Excluye todos los libros que tengan menos de 100 páginas.
# exclude() es el complemento de filter(): genera un "WHERE NOT (...)",
# útil cuando es más natural describir lo que NO se quiere que lo que sí.
libros_min_100_paginas = Libro.objects.exclude(paginas__lt=100)

#------------------------------------------------------------------
# 3. Consultas personalizadas con SQL
#------------------------------------------------------------------

# Ejecuta una consulta SQL directa utilizando raw() para obtener todos
# los libros ordenados por título.
# raw() es útil cuando se necesita SQL que el ORM no puede expresar
libros_ordenados = Libro.objects.raw('SELECT * FROM biblioteca_libro ORDER BY titulo')

# Usa connection.cursor() para ejecutar una query personalizada
# (conteo de libros por autor) y mostrar los resultados.
# Se usa el cursor (en vez de raw() o el ORM) porque esta consulta
# no devuelve instancias de Libro sino datos agregados (autor, conteo),
# que no corresponden a ningún modelo concreto.
with connection.cursor() as cursor:
    cursor.execute('SELECT autor, COUNT(*) FROM biblioteca_libro GROUP BY autor')
    resultados = cursor.fetchall()
    for autor, conteo in resultados:
        print(f'Autor: {autor}, Cantidad de libros: {conteo}')

#------------------------------------------------------------------
# 4. Campos específicos y anotaciones
#------------------------------------------------------------------

# Recupera solo los títulos de todos los libros (usando values()).
# values() le pide a Django que seleccione solo esa columna en el SQL
# (SELECT titulo ...) en vez de traer la fila completa, lo que reduce
# el tráfico de datos cuando el modelo tiene muchos campos.
titulos_libros = Libro.objects.values('titulo')

# Agrega una anotación (usando annotate) para contar cuántos libros
# hay por autor.
# values('autor') agrupa los resultados por autor (como un GROUP BY),
# y annotate(Count('id')) cuenta cuántas filas caen en cada grupo.
# El orden importa: values() ANTES de annotate() es lo que produce el
# comportamiento de "GROUP BY autor" en vez de anotar cada libro individual.
libros_por_autor = Libro.objects.values('autor').annotate(cantidad=Count('id'))

#------------------------------------------------------------------
#5. Reflexión (en un archivo aparte) 
#------------------------------------------------------------------
# respuestas en resumen.md

