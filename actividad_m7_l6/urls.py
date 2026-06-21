from django.urls import path

from . import views

app_name = 'libros'

urlpatterns = [
    # ============================================================
    # READ
    # ============================================================
    # Ruta para listar los libros del usuario autenticado.
    # Debe llamar a la vista views.lista_libros
    path('', views.lista_libros, name='lista'),

    # Ruta para ver el detalle de un libro específico.
    # Debe llamar a la vista views.detalle_libro
    # Recibe el id del libro como parámetro de la URL.
    path('libro/<int:id>/', views.detalle_libro, name='detalle'),


    # ============================================================
    # CREATE / UPDATE
    # ============================================================
    # Ruta para crear un nuevo libro o sugerencia.
    # Debe llamar a la vista views.crear_libro
    path('crear/', views.crear_libro, name='crear'),

    # Ruta para editar un libro existente.
    # Debe llamar a la vista views.editar_libro
    # Recibe el id del libro a editar.
    path('libro/<int:id>/editar/', views.editar_libro, name='editar'),


    # ============================================================
    # DELETE
    # ============================================================
    # Ruta para eliminar un libro (con confirmación previa).
    # Debe llamar a la vista views.eliminar_libro
    path('libro/<int:id>/eliminar/', views.eliminar_libro, name='eliminar'),

]
