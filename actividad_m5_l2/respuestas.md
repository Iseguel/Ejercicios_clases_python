2. Consultas entre varias tablas 
-- Responde lo siguiente en respuestas.md y realiza las consultas en consultas_sql.sql: • ¿Qué es un modelo de datos y para qué sirve en bases relacionales? 
-- • ¿Qué es una clave foránea y qué garantiza? 

**¿Qué es un modelo de datos y para qué sirve en bases relacionales?**
Un modelo de datos es como un plano arquitectónico que organiza cómo se guardará la información. 
En bases de datos relacionales, sirve para definir qué tablas existirán, sus columnas y cómo se conectan entre sí. 
Es fundamental porque asegura que los datos estén bien estructurados, evitando información duplicada o desordenada. 
Gracias a esto, podemos guardar y buscar datos de forma mucho más lógica y segura.

**¿Qué es una clave foránea y qué garantiza?**
Una clave foránea (o *foreign key*) es una columna en una tabla que hace referencia al identificador principal de otra tabla. 
Básicamente, funciona como un puente que conecta la información de ambas (como conectar `pedidos` con `clientes`). 
Garantiza la "integridad referencial", es decir, asegura que las relaciones siempre sean válidas. 
Por ejemplo, gracias a ella el sistema no te dejará crear un pedido para un cliente que no existe.
