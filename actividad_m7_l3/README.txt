Proyecto: Blog (Actividad M7 L3)
=================================
Este archivo describe brevemente cada uno de los pasos realizados para la construcción de este proyecto.

● Levantar un proyecto Django
  Se inició un nuevo proyecto y aplicación en Django mediante la consola 
  usando `django-admin startproject` configurando previamente un entorno virtual e instalando las dependencias necesarias.

● Levantar una base de datos Postgres con credenciales de acceso
  Se creó una base de datos relacional vacía en PostgreSQL de forma local (blog_db), definiendo un usuario, contraseña y puerto específicos para este proyecto.

● Configurar el acceso a la base de datos en el archivo settings.py del proyecto Django
  Se reemplazó la configuración predeterminada de SQLite en la variable `DATABASES` del archivo `settings.py`, 
  colocando el motor `django.db.backends.postgresql` junto con el nombre de la BD y las credenciales creadas en el paso anterior.

● Crear los modelos de datos en el archivo models.py
  Se definieron las clases de Python dentro de `models.py` (Autor, Artículo, Comentario y Categoría) especificando sus campos (CharField, TextField, etc.). 
  Estas clases representan la estructura de las tablas del blog.

● Hacer la migración de datos a la base de datos
  Se ejecutó el comando `python manage.py makemigrations` para generar los archivos de migración y luego `python manage.py migrate` para aplicar los cambios 
  y construir las tablas reales en PostgreSQL.

● Crear nuevas entradas en cada tabla y realizar una consulta ORM
  Se interactuó con la base de datos mediante la shell interactiva de Django (`python manage.py shell`) 
  utilizando el ORM para instanciar nuevos objetos (crear registros) y realizar consultas
