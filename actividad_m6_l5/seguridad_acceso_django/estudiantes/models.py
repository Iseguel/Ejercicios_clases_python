#from django.db import models
#
#class Estudiante(models.Model):
#    nombre = models.CharField(max_length=100)
#    apellido = models.CharField(max_length=100)
#    email = models.EmailField(unique=True)
#    curso = models.CharField(max_length=100)
#    password = models.CharField(max_length=200)
#
#    def __str__(self):
#        return f"{self.nombre} {self.apellido}"


from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    # Solo los campos EXTRA
    curso = models.CharField(
        max_length=100,
        blank=True)
    direccion = models.CharField(
        max_length=200,
        blank=True)
    beca = models.CharField(
        max_length=50,
        blank=True)

    def __str__(self):
        return self.username
    
