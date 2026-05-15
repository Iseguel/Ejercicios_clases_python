--CREATE TABLE clientes (
--    id SERIAL PRIMARY KEY,
--    nombre VARCHAR(100),
--    ciudad VARCHAR(50)
--);

--CREATE TABLE pedidos (
--    id SERIAL PRIMARY KEY,
--    cliente_id INTEGER 
--    fecha DATE,
--    total NUMERIC
--    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
--);


-- 1. Consultas a una sola tabla 
-- Escribe consultas SQL que realicen lo siguiente: 

-- • Obtener todos los registros de la tabla clientes. 
--SELECT * FROM clientes;

-- • Obtener el nombre y ciudad de todos los clientes que vivan en "Valparaíso".
--SELECT nombre, ciudad FROM clientes WHERE ciudad = 'Valparaíso';

-- • Usar COUNT() para contar cuántos clientes hay en total. 
--SELECT COUNT(*) FROM clientes;

-- • Obtener todas las ciudades distintas en las que hay clientes (DISTINCT). 
--SELECT DISTINCT ciudad FROM clientes;

-- • Agrupar clientes por ciudad y contar cuántos hay en cada una. 
--SELECT ciudad, COUNT(*) FROM clientes GROUP BY ciudad;

-- 2. Consultas entre varias tablas 
-- Responde lo siguiente en respuestas.md y realiza las consultas en consultas_sql.sql: • ¿Qué es un modelo de datos y para qué sirve en bases relacionales? 
-- • ¿Qué es una clave foránea y qué garantiza? 

-- Consulta con SQL: 
-- • Obtener todos los pedidos, incluyendo el nombre del cliente. 
--SELECT * FROM pedidos INNER JOIN clientes ON pedidos.cliente_id = clientes.id;

-- • Obtener los pedidos hechos por clientes de "Santiago".
--SELECT * FROM pedidos INNER JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = 'Santiago';

-- • Obtener el total de pedidos por cliente (usando GROUP BY).
--SELECT clientes.nombre, SUM(pedidos.total) FROM pedidos INNER JOIN clientes ON pedidos.cliente_id = clientes.id GROUP BY clientes.nombre;

-- • Usar un LEFT JOIN para listar todos los clientes y sus pedidos, incluyendo aquellos que no han hecho  pedidos. 
--SELECT clientes.nombre, pedidos.total FROM clientes LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;  

-- • Crear una consulta anidada que muestre los clientes cuyo total de pedidos supera los $100.000. 
--SELECT * FROM clientes WHERE id IN (SELECT cliente_id FROM pedidos GROUP BY cliente_id HAVING SUM(total) > 100000);
