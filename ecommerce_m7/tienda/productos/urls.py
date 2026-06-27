from django.urls import path
from . import views

urlpatterns = [
    path('productos/admin/', views.lista_productos, name='productos_admin_lista'),
    path('productos/admin/crear/', views.crear_producto, name='productos_admin_crear'),
    path('productos/admin/<int:pk>/editar/', views.editar_producto, name='productos_admin_editar'),
    path('productos/admin/<int:pk>/eliminar/', views.eliminar_producto, name='productos_admin_eliminar'),
]