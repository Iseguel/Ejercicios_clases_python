from django.conf import settings
from django.db import models


class Libro(models.Model):
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='libros'
    )
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=1000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name_plural = 'Libros'

    def __str__(self):
        return f'{self.titulo}'
