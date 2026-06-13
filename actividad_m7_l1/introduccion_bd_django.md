# Introducción a Bases de Datos en Django

## 1. Bases de datos en Django 
**• ¿Qué función cumple una base de datos dentro de una aplicación Django?** 
**R:** Cumple la función de almacenar, gestionar y recuperar de manera persistente toda la información y los datos que la aplicación necesita para funcionar (como usuarios, productos, registros, etc.).

**• ¿Qué sistemas de bases de datos relacionales soporta Django por defecto?** 
**R:** SQLite, PostgreSQL, MySQL, Oracle

**• ¿Cuál es el motor de base de datos que se utiliza por defecto al crear un nuevo proyecto? ¿Por qué crees que es ese?** 
**R:** SQLite, ya que es más liviano y permite una implementación sencilla. Al ser un archivo local, evita tener que instalar y configurar un motor o servidor de base de datos por separado en las etapas iniciales de desarrollo.

## 2. ORM en Django 
**• ¿Qué es un ORM y cómo se diferencia de escribir sentencias SQL manualmente?** 
**R:** Un ORM (Object-Relational Mapping) es una herramienta que permite trabajar con BD usando la programación orientada a objetos de Python en lugar de escribir sentencias directamente en SQL. Se diferencia en que el ORM traduce automáticamente el código de Python a las consultas SQL del motor que se este usando.

**• Menciona al menos dos ventajas de usar el ORM de Django.** 
**R:** 
1) Permite trabajar con las bases de datos directamente en Python, lo que acelera y facilita el desarrollo. 
2) Permite la portabilidad: puedes cambiar de motor de base de datos (ej. de SQLite a PostgreSQL) cambiando solo la configuración y sin reescribir tus consultas. Además, proporciona protección automática contra inyecciones SQL.

**• Explica qué significa que una clase modelo en Python represente una tabla en la base de datos.** 
**R:** Significa que la estructura de la clase es el molde para la tabla: cada atributo o propiedad de la clase se traduce a una columna en la tabla de la base de datos. A su vez, cada vez que creas una instancia (objeto) de esa clase, Django lo guarda como una nueva fila (registro) en dicha tabla.

## 3. Migraciones 
**• ¿Qué son las migraciones en Django y por qué son importantes?** 
**R:** Son archivos de código que propagan los cambios en los modelos (creación, modificación o borrado de campos) hacia el esquema de la base de datos real. Son importantes porque actúan como un sistema de control de versiones para la base de datos, permitiéndote actualizar su estructura de forma progresiva, ordenada y segura, sin tener que ejecutar comandos SQL manualmente.

**• ¿Qué comandos se utilizan para:** 

- Crear una nueva migración a partir de cambios en los modelos:
  **R:** `python manage.py makemigrations`

- Aplicar las migraciones a la base de datos:
  **R:** `python manage.py migrate`

## 4. Consultas básicas con el ORM 
**• A partir del siguiente ejemplo de modelo:** 

```python
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    publicado = models.BooleanField(default=True)
```

**Escribe cómo se realizarían las siguientes consultas usando el ORM de Django:** 

**a) Obtener todos los libros** 
**R:** `Libro.objects.all()`

**b) Filtrar los libros por autor igual a "Cervantes"** 
**R:** `Libro.objects.filter(autor="Cervantes")`

**c) Obtener un libro específico por su id** 
**R:** `Libro.objects.get(id=1)`
