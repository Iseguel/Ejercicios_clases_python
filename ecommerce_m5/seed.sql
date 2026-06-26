
-- Datos de ejemplo para ecommerce_db

-- 1. Categorías
INSERT INTO categoria (nombre, descripcion) VALUES
('Cuadros', 'Pinturas y cuadros decorativos'),
('Miniaturas', 'Figuras y miniaturas coleccionables'),
('Accesorios', 'Accesorios y complementos varios');

-- 2. Productos (referencio la categoría por nombre, no por id,
-- para no depender de que SERIAL haya asignado el número que yo creo)
INSERT INTO producto (nombre, descripcion, precio, id_categoria) VALUES
('producto_1',  'Cuadro decorativo modelo 1', 15990, (SELECT id_categoria FROM categoria WHERE nombre = 'Cuadros')),
('producto_2',  'Cuadro decorativo modelo 2', 22990, (SELECT id_categoria FROM categoria WHERE nombre = 'Cuadros')),
('producto_3',  'Cuadro decorativo modelo 3', 18990, (SELECT id_categoria FROM categoria WHERE nombre = 'Cuadros')),
('producto_4',  'Miniatura coleccionable 1',   5990, (SELECT id_categoria FROM categoria WHERE nombre = 'Miniaturas')),
('producto_5',  'Miniatura coleccionable 2',   7990, (SELECT id_categoria FROM categoria WHERE nombre = 'Miniaturas')),
('producto_6',  'Miniatura coleccionable 3',   6490, (SELECT id_categoria FROM categoria WHERE nombre = 'Miniaturas')),
('producto_7',  'Miniatura coleccionable 4',   8990, (SELECT id_categoria FROM categoria WHERE nombre = 'Miniaturas')),
('producto_8',  'Accesorio decorativo 1',      3990, (SELECT id_categoria FROM categoria WHERE nombre = 'Accesorios')),
('producto_9',  'Accesorio decorativo 2',      4990, (SELECT id_categoria FROM categoria WHERE nombre = 'Accesorios')),
('producto_10', 'Accesorio decorativo 3',      2990, (SELECT id_categoria FROM categoria WHERE nombre = 'Accesorios'));

-- 3. Stock (mismo criterio: referencio producto por nombre)
INSERT INTO stock (id_producto, cantidad) VALUES
((SELECT id_producto FROM producto WHERE nombre = 'producto_1'),  8),
((SELECT id_producto FROM producto WHERE nombre = 'producto_2'),  5),
((SELECT id_producto FROM producto WHERE nombre = 'producto_3'), 10),
((SELECT id_producto FROM producto WHERE nombre = 'producto_4'),  6),
((SELECT id_producto FROM producto WHERE nombre = 'producto_5'),  3),
((SELECT id_producto FROM producto WHERE nombre = 'producto_6'),  9),
((SELECT id_producto FROM producto WHERE nombre = 'producto_7'),  4),
((SELECT id_producto FROM producto WHERE nombre = 'producto_8'),  7),
((SELECT id_producto FROM producto WHERE nombre = 'producto_9'),  5),
((SELECT id_producto FROM producto WHERE nombre = 'producto_10'), 6);

-- 4. Usuarios (4 clientes + 1 administrador)
-- password_hash es un valor de relleno: en una app real iría el hash que genera Django con make_password()), nunca texto plano.
INSERT INTO usuario (nombre, email, password_hash, rol) VALUES
('usuario_1', 'usuario_1@mail.com', 'hash_placeholder_1', 'cliente'),
('usuario_2', 'usuario_2@mail.com', 'hash_placeholder_2', 'cliente'),
('usuario_3', 'usuario_3@mail.com', 'hash_placeholder_3', 'cliente'),
('usuario_4', 'usuario_4@mail.com', 'hash_placeholder_4', 'cliente'),
('administrador_1', 'administrador_1@mail.com', 'hash_placeholder_admin', 'administrador');

-- 5. Pedidos + detalle
-- Uso WITH ... RETURNING para encadenar el id_pedido recién creado

WITH nuevo_pedido AS (
    INSERT INTO pedido (id_usuario, estado, total)
    VALUES ((SELECT id_usuario FROM usuario WHERE email = 'usuario_1@mail.com'), 'pagado', 0)
    RETURNING id_pedido
)
INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario)
SELECT np.id_pedido, p.id_producto, v.cantidad, p.precio
FROM nuevo_pedido np
CROSS JOIN (VALUES ('producto_1', 2), ('producto_3', 1)) AS v(nombre, cantidad)
JOIN producto p ON p.nombre = v.nombre;

WITH nuevo_pedido AS (
    INSERT INTO pedido (id_usuario, estado, total)
    VALUES ((SELECT id_usuario FROM usuario WHERE email = 'usuario_2@mail.com'), 'pendiente', 0)
    RETURNING id_pedido
)
INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario)
SELECT np.id_pedido, p.id_producto, v.cantidad, p.precio
FROM nuevo_pedido np
CROSS JOIN (VALUES ('producto_5', 1), ('producto_2', 3)) AS v(nombre, cantidad)
JOIN producto p ON p.nombre = v.nombre;

WITH nuevo_pedido AS (
    INSERT INTO pedido (id_usuario, estado, total)
    VALUES ((SELECT id_usuario FROM usuario WHERE email = 'usuario_3@mail.com'), 'enviado', 0)
    RETURNING id_pedido
)
INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario)
SELECT np.id_pedido, p.id_producto, v.cantidad, p.precio
FROM nuevo_pedido np
CROSS JOIN (VALUES ('producto_7', 2), ('producto_9', 1)) AS v(nombre, cantidad)
JOIN producto p ON p.nombre = v.nombre;

-- 6. Recalcular el total de cada pedido a partir de su detalle
UPDATE pedido p
SET total = sub.total
FROM (
    SELECT id_pedido, SUM(cantidad * precio_unitario) AS total
    FROM detalle_pedido
    GROUP BY id_pedido
) sub
WHERE p.id_pedido = sub.id_pedido;