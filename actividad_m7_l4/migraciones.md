###
## 1. Comprensión teórica 
Responde brevemente las siguientes preguntas: 
• ¿Qué es una migración en Django? 
R: Una migración en Django es una forma de mantener un historial (como un control de versiones) de los cambios que realizamos en los modelos y trasladar esas modificaciones de manera estructurada al esquema de nuestra base de datos relacional.

• ¿Qué problema soluciona respecto a los cambios en los modelos? 
R: Permite trabajar y alterar la estructura de la base de datos a medida que el proyecto evoluciona sin tener que escribir sentencias SQL manualmente. Además, soluciona el problema de sincronizar los cambios de forma segura entre todos los desarrolladores del equipo y el entorno de producción.

• ¿Por qué no basta con modificar el archivo models.py directamente sin hacer migraciones? 
R: Para propagar los cambios es necesario ejecutar los comandos de migración. Modificar models.py solo actualiza la estructura lógica en Python. Las migraciones son indispensables para que Django traduzca esa nueva lógica a lenguaje SQL y aplique los cambios físicos reales (como ALTER TABLE) en la base de datos.


## 2. Crear y aplicar migraciones 
Utilizando una app existente de tu proyecto Django (por ejemplo, principal), realiza lo siguiente: 
a) Agrega un nuevo campo a un modelo existente: 


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    anio = models.IntegerField(verbose_name='Año de publicación')
    stock = models.IntegerField(default=1)
    descripcion = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='libros')
    #---- Campos nuevos ----
    isbn = models.CharField(max_length=20, unique=True, null=True, blank=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo

    def disponible(self):
        return self.stock > 0

b) Ejecuta los siguientes comandos y anota qué hace cada uno: 

Python manage.py makemigrations 

Migrations for 'biblioteca':
  biblioteca/migrations/0009_libro_editorial_libro_isbn.py
    + Add field editorial to libro
    + Add field isbn to libro

Python manage.py migrate 

Operations to perform:
  Apply all migrations: admin, auth, biblioteca, contenttypes, sessions, usuarios
Running migrations:
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying biblioteca.0009_libro_editorial_libro_isbn... OK
  Applying sessions.0001_initial... OK

c) Verifica desde el admin o el shell que el nuevo campo isbn esté disponible en la base de datos. 

>>> from biblioteca.models import Libro
>>> Libro.objects.all().values('isbn')
<QuerySet [{'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}, {'isbn': None}]>


## 3. Aplicar migraciones existentes 
• Elimina el archivo de migración generado (solo con fines pedagógicos, no en producción). 
• Vuelve a ejecutar makemigrations y migrate. 

python3 manage.py makemigrations biblioteca

Migrations for 'biblioteca':
  biblioteca/migrations/0009_libro_editorial_libro_isbn.py
    + Add field editorial to libro
    + Add field isbn to libro

python3 manage.py migrate  

Operations to perform:
  Apply all migrations: admin, auth, biblioteca, contenttypes, sessions, usuarios
Running migrations:
  No migrations to apply.

• Describe lo que sucede si no aplicas una migración pendiente. 
R: Si no se aplica una migración pendiente, la estructura física de la base de datos quedará desincronizada respecto a la estructura lógica de los modelos en `models.py`. Como consecuencia, si intentamos acceder o modificar los datos que dependen de esa migración (por ejemplo, usar un campo nuevo), Django arrojará un error en la base de datos (como `OperationalError: no such column`) porque la tabla o columna real aún no existe. Además, al iniciar el servidor, Django mostrará una advertencia en la terminal indicando que hay migraciones sin aplicar.

## 4. Opcional: Revisión de estado 
Ejecuta el comando: 
    python3 manage.py showmigrations 
• Comenta qué información te entrega y cómo puedes saber qué migraciones ya se aplicaron.  

 [X] 0012_alter_user_first_name_max_length
biblioteca
 [X] 0001_initial
 [X] 0002_editorial
 [X] 0003_autor_biografia_autor_fecha_nacimiento
 [X] 0004_libro_paginas
 [X] 0005_alter_libro_paginas
 [X] 0006_tag_remove_autor_biografia_and_more
 [X] 0007_poblar_generos
 [X] 0008_poblar_autores
 [X] 0009_libro_editorial_libro_isbn
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
sessions
 [X] 0001_initial
usuarios
 [X] 0001_initial
