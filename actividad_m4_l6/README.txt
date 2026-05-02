====================================================
README – Actividad N°6: Manejo de Archivos en Python
====================================================

Archivo principal: manejo_archivos.py

----------------------------------------------------
Respuestas a las preguntas de reflexión:
----------------------------------------------------

• ¿Qué diferencia notaste entre write() y append()?
R: El método write() se usa para escribir en un archivo (y lo crea si no existe), pero sobrescribe todo su contenido si este ya existe. En cambio, append() se utiliza para agregar datos al final del archivo sin borrar la información anterior.

• ¿Qué ventaja tiene usar with open(...) frente a abrir y cerrar manualmente?
R: El bloque with open() gestiona la memoria y los recursos de forma óptima, cerrando el archivo automáticamente una vez que el bloque de código finaliza (incluso si ocurre un error). Esto elimina la necesidad de llamar manualmente al método close() y ayuda a prevenir fugas de memoria o errores de archivos bloqueados por el sistema operativo.