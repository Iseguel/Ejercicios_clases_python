# Conexion y modelo

## 1. Conexión a PostgreSQL 
**• Instala el paquete necesario para conectarse a PostgreSQL:** 
**R:** `pip install psycopg2`

**• Crea una base de datos vacía en PostgreSQL llamada libreria.**
**• En el archivo settings.py de tu proyecto Django, reemplaza la configuración de base de datos por:**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'libreria',
        'USER': 'postgres',
        'PASSWORD': '*********',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
       
## 2. Definición de un modelo 
**• En la app principal, crea un modelo Libro con los siguientes campos:** 

```python
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    anio_publicacion = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo}"
```

**• Indica qué campo actuaría como clave primaria por defecto.**
**R:** `id`

**• Explica cómo se definiría una clave primaria compuesta si se quisiera hacer manualmente.**
**R:** En Django no existe soporte nativo para definir claves primarias compuestas directamente usando `primary_key=True` en múltiples campos. Para lograr un comportamiento equivalente (garantizar que la combinación de dos o más campos sea única), se debe declarar la clase `Meta` dentro del modelo y agregar una restricción usando `models.UniqueConstraint(fields=['campo1', 'campo2'], name='clave_compuesta')` (o el atributo heredado `unique_together`). Aunque Django seguirá generando un `id` autoincremental como Primary Key real de la tabla, a nivel lógico se aplicará la restricción compuesta.


## 3. Aplicar migraciones 
**• Ejecuta los siguientes comandos desde consola y explica qué hace cada uno:**

```bash
python3 manage.py makemigrations  # Genera el archivo de migración
python3 manage.py migrate         # Ejecuta las migraciones en la base de datos
```


## 4. Operaciones CRUD (puede ser en shell o vista) 
**Utilizando el ORM, realiza las siguientes acciones y describe en el .md los comandos o código utilizados:**

**• Crear un nuevo libro** 
**R:** `Libro.objects.create(titulo="Duna", autor="Franck Herbert", anio_publicacion="1965", disponible=True)`

**• Listar todos los libros** 
**R:** `Libro.objects.all()`

**• Buscar un libro por su título** 
**R:** `Libro.objects.get(titulo="Duna")`

**• Actualizar el campo disponible de un libro**
**R:** `Libro.objects.filter(titulo="Duna").update(disponible=False)`

**• Eliminar un libro** 
**R:** `Libro.objects.filter(titulo="Duna").delete()`


