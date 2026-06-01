from django.db import models

class Contacto(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"

class Usuario(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=100)


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"