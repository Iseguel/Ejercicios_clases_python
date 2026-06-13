from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email',
        'curso', 'direccion', 'beca',
        'is_staff'
    )
    fieldsets = UserAdmin.fieldsets + (
        ('Datos extra', {
            'fields': ('curso', 'direccion', 'beca')
        }),
    )