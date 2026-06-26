-- Esquema relacional del e-commerce (Módulo 5)

CREATE TABLE usuario (
    id_usuario      SERIAL PRIMARY KEY,
    nombre          VARCHAR(100) NOT NULL,
    email           VARCHAR(150) NOT NULL UNIQUE,
    password_hash   VARCHAR(255) NOT NULL,
    rol             VARCHAR(20) NOT NULL DEFAULT 'cliente'
                    CHECK (rol IN ('cliente', 'administrador')),
    fecha_registro  TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE categoria (
    id_categoria    SERIAL PRIMARY KEY,
    nombre          VARCHAR(80) NOT NULL UNIQUE,
    descripcion     TEXT
);

CREATE TABLE producto (
    id_producto     SERIAL PRIMARY KEY,
    nombre          VARCHAR(120) NOT NULL,
    descripcion     TEXT,
    precio          NUMERIC(10,2) NOT NULL CHECK (precio >= 0),
    id_categoria    INTEGER NOT NULL REFERENCES categoria(id_categoria)
                    -- RESTRICT: no permite borrar una categoría mientras
                    -- tenga productos asociados (evita productos huérfanos).
                    ON DELETE RESTRICT
);

CREATE TABLE stock (
    -- id_producto es PK y FK a la vez: encierra la relación 1:1
    -- "cada producto tiene exactamente un registro de stock".
    id_producto     INTEGER PRIMARY KEY REFERENCES producto(id_producto)
                    -- CASCADE: si se borra el producto, no tiene sentido
                    -- mantener un stock huérfano.
                    ON DELETE CASCADE,
    cantidad        INTEGER NOT NULL DEFAULT 0 CHECK (cantidad >= 0),
    actualizado_en  TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE pedido (
    id_pedido       SERIAL PRIMARY KEY,
    id_usuario      INTEGER NOT NULL REFERENCES usuario(id_usuario)
                    -- RESTRICT: el historial de pedidos no debe perderse
                    -- aunque se elimine el usuario (lo normal sería
                    -- desactivar usuarios, no borrarlos).
                    ON DELETE RESTRICT,
    fecha_pedido    TIMESTAMP NOT NULL DEFAULT now(),
    estado          VARCHAR(20) NOT NULL DEFAULT 'pendiente'
                    CHECK (estado IN ('pendiente', 'pagado', 'enviado', 'cancelado')),
    total           NUMERIC(10,2) NOT NULL DEFAULT 0 CHECK (total >= 0)
);

CREATE TABLE detalle_pedido (
    id_pedido        INTEGER NOT NULL REFERENCES pedido(id_pedido)
                     -- CASCADE: si se borra el pedido, sus líneas de
                     -- detalle no tienen sentido sin él.
                     ON DELETE CASCADE,
    id_producto      INTEGER NOT NULL REFERENCES producto(id_producto)
                     -- RESTRICT: protege el historial de compras; no se
                     -- puede borrar un producto que ya fue vendido.
                     ON DELETE RESTRICT,
    cantidad         INTEGER NOT NULL CHECK (cantidad > 0),
    -- snapshot del precio al momento de la compra (no referencia al
    -- precio actual de producto, que puede cambiar después).
    precio_unitario  NUMERIC(10,2) NOT NULL CHECK (precio_unitario >= 0),
    -- PK compuesta: un producto aparece como máximo una vez por pedido
    -- (decisión confirmada contigo).
    PRIMARY KEY (id_pedido, id_producto)
);

