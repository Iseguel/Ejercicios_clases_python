# Respuestas

**• ¿Cómo funciona el flujo completo de una operación CRUD?** 

R: Todo parte de una petición HTTP a una URL definida en `urls.py`, que Django enruta hacia una vista. La vista valida permisos (`@login_required`/`@permission_required`) y, si es necesario, recupera el objeto con `get_object_or_404()` validando también la propiedad (`creado_por=request.user`). 
Para Create/Update se procesa un formulario: si es GET se muestra vacío o con los datos actuales; si es POST se valida y, si es válido, se guarda 
con `.save()` y se redirige. 
Para Read se hace una consulta con el ORM y se pasa el resultado al template; 
para Delete se confirma la acción y luego se ejecuta `.delete()`. En todos los casos la vista termina devolviendo un `render()` o un `redirect()`, nunca dejando la lógica de negocio en el template.

**• ¿Qué aprendiste sobre el enrutamiento y los parámetros dinámicos en URLs?**

R: Las URLs pueden capturar valores variables usando *path converters* como `<int:id>` o `<int:pk>`, que Django pasa automáticamente como argumento a la vista correspondiente. Esto permite reutilizar una sola vista para todos los objetos de un modelo (por ejemplo `libros/editar/<int:id>/`) en vez de crear una ruta por cada registro. Aprendí también que el `name=` de cada `path()` es clave para no hardcodear URLs: usando `{% url 'libros:editar' libro.id %}` en el template o `reverse('libros:editar', args=[id])` en la vista, si la URL cambia solo se actualiza en `urls.py` y no en cada lugar donde se referencia. Además, el parámetro capturado es el mismo que se usa para aplicar el filtro de propiedad (`creado_por=request.user`), conectando el enrutamiento con la seguridad a nivel de objeto.