-- Consultas de información para ecommerce_db (sección 3.4)

-- 1. Listar todos los productos junto a su categoría
SELECT
    p.id_producto,
    p.nombre,
    p.precio,
    c.nombre AS categoria
FROM producto p
JOIN categoria c ON c.id_categoria = p.id_categoria
ORDER BY c.nombre, p.nombre;


-- 2. Buscar productos por nombre (coincidencia parcial, sin distinguir mayúsculas)
-- ILIKE en vez de LIKE: en Postgres, LIKE es sensible a mayúsculas/minúsculas.
SELECT
    id_producto,
    nombre,
    precio
FROM producto
WHERE nombre ILIKE '%producto_1%';   


-- 3. Filtrar productos por categoría
SELECT
    p.id_producto,
    p.nombre,
    p.precio
FROM producto p
JOIN categoria c ON c.id_categoria = p.id_categoria
WHERE c.nombre = 'Miniaturas';       


-- 4. Mostrar los productos asociados a un pedido
SELECT
    dp.id_pedido,
    pr.nombre,
    dp.cantidad,
    dp.precio_unitario,
    (dp.cantidad * dp.precio_unitario) AS subtotal
FROM detalle_pedido dp
JOIN producto pr ON pr.id_producto = dp.id_producto
WHERE dp.id_pedido = 1;            


-- 5. Calcular el total de un pedido
SELECT id_pedido, total
FROM pedido
WHERE id_pedido = 1;


-- 6. Identificar productos con stock bajo
-- Umbral de ejemplo: menos de 5 unidades.
SELECT
    p.nombre,
    s.cantidad
FROM producto p
JOIN stock s ON s.id_producto = p.id_producto
WHERE s.cantidad < 5
ORDER BY s.cantidad ASC;