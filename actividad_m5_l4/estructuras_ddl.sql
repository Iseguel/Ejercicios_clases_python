--1. Creación de tablas 

--Define las siguientes dos tablas respetando integridad referencial: 

    --CREATE TABLE departamentos (
    --    id SERIAL PRIMARY KEY,
    --    nombre VARCHAR(100) NOT NULL
    --);
    --
    --CREATE TABLE empleados (
    --    id SERIAL PRIMARY KEY,
    --    nombre VARCHAR(100) NOT NULL,
    --    correo VARCHAR(100),
    --    departamento_id INTEGER,
    --    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
    --);
--
--Explica con comentarios: 
--• Qué es una clave primaria y por qué se usa en id 
--    R. Una clave primaria es un campo o conjunto de campos que identifica de manera única cada registro en una tabla. 
--    Se usa en el campo "id" para asegurar que cada departamento y cada empleado tenga un identificador único, lo que facilita 
--    la gestión y referencia de los datos.
--
--• Qué significa NOT NULL
--    R. NOT NULL es una restricción que se aplica a un campo para indicar que no puede contener valores nulos. 
--    Esto significa que al insertar o actualizar un registro, se debe proporcionar un valor para ese campo, garantizando que 
--    la información esencial esté siempre presente. 
--
--• Qué relación existe entre empleados y departamentos
--    R. Existe una relación de uno a muchos entre departamentos y empleados. 
--    Un departamento puede tener múltiples empleados, pero cada empleado pertenece a un solo departamento. 
--    Esta relación se establece a través de la clave foránea `departamento_id` en la tabla `empleados`, 
--    que apunta a la clave primaria `id` en la tabla `departamentos`.


-- 2. Modificar tablas existentes 

-- Agrega nuevas columnas a las tablas creadas: 
-- • A empleados: un campo fecha_ingreso DATE 

-- AlTER TABLE empleados ADD COLUMN fecha_ingreso DATE;

-- • A departamentos: un campo ubicacion VARCHAR(100) 

-- ALTER TABLE departamentos ADD COLUMN ubicacion VARCHAR(100);

-- Luego: 
-- • Modifica el campo correo de empleados para que no permita nulos (SET NOT NULL) 

-- ALTER TABLE empleados ALTER COLUMN correo SET NOT NULL;


-- 3. Eliminar y truncar tablas 

-- • Escribe una sentencia para eliminar la tabla empleados (teniendo en cuenta su relación con  departamentos). 
--DROP TABLE IF EXISTS empleados;

-- • Crea una tabla temporal de prueba, inserta un par de registros, y luego ejecuta un TRUNCATE sobre ella. • Comenta la diferencia entre DELETE y TRUNCATE. 

--CREATE TABLE temporal_prueba (
--    id SERIAL PRIMARY KEY,
--    dato VARCHAR(50)
--);

--INSERT INTO temporal_prueba (dato) VALUES ('Prueba 1'), ('Prueba 2');

--TRUNCATE TABLE temporal_prueba;

-- Comentario diferencia DELETE vs TRUNCATE:
-- R. DELETE es un comando DML que borra filas una por una, permite usar la cláusula WHERE para filtrar qué borrar y registra cada operación.
-- TRUNCATE es un comando DDL que vacía toda la tabla de golpe. Es mucho más rápido, 
-- no permite usar WHERE y reinicia los contadores (como los campos SERIAL).

