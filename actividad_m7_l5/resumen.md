#------------------------------------------------------------------
# 5. Reflexión (respuestas)
#------------------------------------------------------------------

#• ¿Qué ventajas encuentras en usar el ORM frente a SQL tradicional? 
R: Facilita la implementacion de BBDD y simplifica las consultas a la BBDD 

#• ¿En qué situaciones te parece útil ejecutar SQL directamente desde Django? 
R: Solo cuando alguna consulta sea muy especifica o requiera una personalización

#• ¿Qué dificultades encontraste al trabajar con consultas más avanzadas? 
R: Requieren mas lineas de codigo para implementarlas 


#• ¿Qué ventajas encuentras en usar el ORM frente a SQL tradicional? 
R: Facilita la implementación de BBDD y simplifica las consultas. 
   Además, abstrae las diferencias entre motores de base de datos (PostgreSQL, MySQL, SQLite), 
   previene inyecciones SQL automáticamente y se integra con el sistema de migraciones para versionar el esquema.

#• ¿En qué situaciones te parece útil ejecutar SQL directamente desde Django? 
R: Cuando la consulta es muy específica o requiere personalización, 
   especialmente con funciones avanzadas que el ORM no soporta o cuando se necesita optimizar el rendimiento 
   de una consulta crítica que el ORM genera de forma poco eficiente.

#• ¿Qué dificultades encontraste al trabajar con consultas más avanzadas? 
R: Requieren más líneas de código y un razonamiento más cuidadoso sobre qué se ejecuta en la BBDD vs en Python 
   (ej. decidir entre select_related/prefetch_related), además de mayor esfuerzo para depurar el SQL real que el ORM termina generando.