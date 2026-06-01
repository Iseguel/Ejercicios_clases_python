from django.contrib import admin
from .models import Contacto, Usuario


# Registramos el modelo Contacto en el panel de administración.
# Esto permite ver, buscar, editar y eliminar registros desde /admin/.
@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):

    # Columnas que se mostrarán en la lista del panel admin.
    list_display = ('id', 'name', 'email', 'message')

    # Campos por los cuales se podrá buscar en el panel admin.
    search_fields = ('name', 'email')

@admin.register(Usuario)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'edad', 'ciudad')
    search_fields = ('username', 'email')