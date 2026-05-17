-- 1. Inserción de datos (INSERT) 
-- Agrega registros a las tablas: 

-- • Insertar al menos 3 nuevos clientes. 
 SELECT * FROM clientes;
 INSERT INTO clientes (rut, nombre, apellido, email, telefono, direccion, ciudad) 
 VALUES ('12345678-9', 'Emilia', 'González', 'emilia.gonzalez@email.com', '987654321', 'Calle 123', 'Santiago'),
        ('23456789-0', 'Matías', 'López', 'matias.lopez@email.com', '876543210', 'Avenida 456', 'Valparaíso'),
        ('34567890-1', 'Sofía', 'Martínez', 'sofia.martinez@email.com', '765432109', 'Plaza 789', 'Concepción');

 SELECT * FROM clientes;  


-- • Insertar al menos 5 pedidos asociados a los clientes. 
-- • Usa DEFAULT o una secuencia (SERIAL) para autogenerar los IDs. 
SELECT * FROM pedidos;  
INSERT INTO pedidos (cliente_id, empleado_id, total, metodo_pago)
VALUES (1, 1, 1000.00, 'TARJETA_DEBITO'),
       (2, 2, 2000.00, 'EFECTIVO'),
       (3, 3, 3000.00, 'TRANSFERENCIA'),
       (1, 4,  4000.00, 'TARJETA_DEBITO'),
       (2, 5,  5000.00, 'EFECTIVO');
SELECT * FROM pedidos;

-- 2. Actualización de datos (UPDATE) 
-- • Cambiar la ciudad de un cliente con id = 2 a "Viña del Mar". 
SELECT * FROM clientes;
UPDATE clientes
SET ciudad = 'Viña del Mar'
WHERE id = 2;
SELECT * FROM clientes;

-- • Modificar el total de un pedido existente. 
SELECT * FROM pedidos;
UPDATE pedidos
SET total = 1500.00
WHERE id = 1;
SELECT * FROM pedidos;

-- 3. Eliminación de datos (DELETE) 
-- • Eliminar un pedido por su id. 
SELECT * FROM pedidos;
DELETE FROM pedidos
WHERE id = 1;
SELECT * FROM pedidos;


-- • Intentar eliminar un cliente que tiene pedidos asociados 
-- y documentar el resultado (debe fallar si hay  restricción de integridad referencial).
SELECT * FROM clientes;
DELETE FROM clientes
WHERE id = 2;
SELECT * FROM clientes;


-----------------------------------------------------------
BEGIN;
UPDATE pedidos SET total = 0 WHERE id = 1;
ROLLBACK;
SELECT * FROM pedidos;

BEGIN;
DELETE FROM pedidos WHERE id = 2;
COMMIT;
SELECT * FROM pedidos;