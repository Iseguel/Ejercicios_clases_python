-- Operación transaccional: registrar una compra (sección 3.5)

BEGIN;

-- Bloqueamos las filas de stock que vamos a tocar ANTES de leerlas.
SELECT cantidad FROM stock
WHERE id_producto = (SELECT id_producto FROM producto WHERE nombre = 'producto_8')
FOR UPDATE;

SELECT cantidad FROM stock
WHERE id_producto = (SELECT id_producto FROM producto WHERE nombre = 'producto_10')
FOR UPDATE;

-- 1. Crear el pedido. El total queda en 0 porque todavía no existe el detalle.
WITH nuevo_pedido AS (
    INSERT INTO pedido (id_usuario, estado, total)
    VALUES ((SELECT id_usuario FROM usuario WHERE email = 'usuario_4@mail.com'), 'pendiente', 0)
    RETURNING id_pedido
)
-- 2. Insertar el detalle. precio_unitario se toma del precio ACTUAL del
-- producto en este instante: queda fijo aunque el precio cambie después.
INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario)
SELECT np.id_pedido, p.id_producto, v.cantidad, p.precio
FROM nuevo_pedido np
CROSS JOIN (VALUES ('producto_8', 2), ('producto_10', 3)) AS v(nombre, cantidad)
JOIN producto p ON p.nombre = v.nombre;

-- 3. Descontar el stock vendido.
-- Si esta resta deja cantidad < 0, salta el CHECK definido en schema.sql
-- y Postgres aborta TODA la transacción: el pedido y el detalle de los
-- pasos 1 y 2 tampoco quedan guardados. Así se evita vender stock que no existe.
UPDATE stock s
SET cantidad = s.cantidad - dp.cantidad,
    actualizado_en = now()
FROM detalle_pedido dp
WHERE s.id_producto = dp.id_producto
  AND dp.id_pedido = (
      SELECT MAX(id_pedido) FROM pedido
      WHERE id_usuario = (SELECT id_usuario FROM usuario WHERE email = 'usuario_4@mail.com')
  );

-- 4. Recalcular el total del pedido recién creado, ahora que el detalle existe.
UPDATE pedido p
SET total = sub.total
FROM (
    SELECT id_pedido, SUM(cantidad * precio_unitario) AS total
    FROM detalle_pedido
    WHERE id_pedido = (
        SELECT MAX(id_pedido) FROM pedido
        WHERE id_usuario = (SELECT id_usuario FROM usuario WHERE email = 'usuario_4@mail.com')
    )
    GROUP BY id_pedido
) sub
WHERE p.id_pedido = sub.id_pedido;

COMMIT;