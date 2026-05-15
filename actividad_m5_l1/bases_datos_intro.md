# Introducción a Bases de Datos Relacionales

---

## 1. El rol de una base de datos

### ¿Qué es y para qué sirve una base de datos relacional en una organización?

Una base de datos relacional es un sistema organizado para almacenar, gestionar y recuperar información de manera estructurada, usando tablas que se relacionan entre sí mediante claves. Dentro de una organización cumple el rol de ser la **fuente central de informacion** para los datos del negocio: permite que múltiples usuarios y aplicaciones accedan a la misma información de forma simultánea, consistente y segura, eliminando la duplicidad y los errores propios de manejar datos en archivos dispersos (como hojas de cálculo).

En términos prácticos, una base de datos relacional permite a la organización:
- Registrar y consultar información en tiempo real.
- Mantener la integridad de los datos mediante reglas y restricciones.
- Escalar el almacenamiento y el acceso a medida que el negocio crece.
- Generar reportes y análisis a partir de datos confiables.

### 3 ejemplos concretos de uso

| # | Caso de uso | Descripción |
|---|-------------|-------------|
| 1 | **Sistema de ventas** | Registra cada transacción: cliente, productos comprados, cantidades, precios, fechas y formas de pago. Permite generar facturas, controlar ingresos y analizar el comportamiento de compra. |
| 2 | **Gestión de usuarios / RR.HH.** | Almacena la información de empleados: datos personales, cargo, departamento, historial de sueldos y contratos. Facilita la liquidación de sueldos y el control de accesos al sistema. |
| 3 | **Control de inventario** | Registra el stock de productos, movimientos de entrada y salida, proveedores y ubicaciones en bodega. Permite alertar cuando un producto está bajo el mínimo y generar órdenes de compra automáticas. |

---

## 2. Características de un RDBMS

### ¿Qué es un RDBMS?

Un **RDBMS** (*Relational Database Management System* / Sistema Gestor de Bases de Datos Relacionales) es el software que permite crear, administrar, consultar y controlar el acceso a una base de datos relacional. Actúa como intermediario entre los usuarios o aplicaciones y los datos almacenados en disco.

### 3 características que lo diferencian de otros sistemas de almacenamiento

1. **Modelo relacional y lenguaje SQL**  
   Los datos se organizan en tablas (filas y columnas) y se consultan mediante SQL (*Structured Query Language*), un estándar universal que permite filtrar, combinar y transformar datos con precisión. 

2. **Propiedades ACID**  
   Los RDBMS garantizan transacciones **Atómicas, Consistentes, Aisladas y Durables**. Esto significa que una operación o se completa por completo o no ocurre en absoluto, evitando estados inconsistentes en los datos 

3. **Integridad referencial**  
   A través de llaves primarias y foráneas, el RDBMS asegura que las relaciones entre tablas sean válidas: no se puede registrar una venta de un cliente que no existe, ni eliminar un cliente si tiene órdenes activas asociadas.

### 3 RDBMS ampliamente usados en la industria

| RDBMS | Contexto típico de uso |
|-------|------------------------|
| **PostgreSQL** | Proyectos open-source, startups y empresas medianas-grandes que requieren funcionalidades avanzadas (JSON, extensiones geoespaciales, alta concurrencia). |
| **MySQL / MariaDB** | Aplicaciones web (WordPress, e-commerce), servicios de internet y entornos LAMP donde se prioriza velocidad y facilidad de configuración. |
| **Microsoft SQL Server** | Entornos corporativos Windows, integración con herramientas Microsoft (Power BI, Azure), sistemas ERP y aplicaciones empresariales de gran escala. |

---

## 3. Herramientas y objetos

### Herramientas para consultar y administrar bases de datos

**Herramientas gráficas (GUI):**

- **DBeaver** — Editor SQL y explorador de bases de datos universal (open-source). Soporta PostgreSQL, MySQL, SQLite, SQL Server y muchos más.
- **MySQL Workbench** — Herramienta oficial de Oracle para MySQL/MariaDB. Ofrece diseño visual de esquemas, administración del servidor y editor SQL con autocompletado.
- **SQLiteStudio** — Herramienta liviana y portable para SQLite, ideal para proyectos pequeños o aprendizaje.
- **pgAdmin** — Interfaz web/de escritorio oficial para PostgreSQL, con panel de monitoreo y editor de consultas.

**Herramientas de línea de comandos (CLI):**

- **psql** — Cliente oficial de PostgreSQL en terminal. Permite conectarse a una base de datos y ejecutar comandos SQL y meta-comandos (`\dt` para listar tablas, `\d nombre_tabla` para describir una tabla).
- **mysql** — Cliente CLI oficial de MySQL/MariaDB, con funcionalidad equivalente a psql para ese motor.
- **sqlite3** — Intérprete interactivo de SQLite incluido en la mayoría de los sistemas operativos.

---

### Objetos dentro de una base de datos

#### Tabla
Es la estructura fundamental de almacenamiento. Organiza los datos en filas (registros) y columnas (campos/atributos). Cada tabla representa una entidad del dominio, por ejemplo: `clientes`, `productos`, `pedidos`.

```
clientes
-------------------------------------------
│ id │ nombre       │ email               │
-------------------------------------------
│  1 │ Ana Torres   │ ana@email.com        │
│  2 │ Pedro López  │ pedro@email.com      │
└-------------------------------------------
```

#### Vista (View)
Es una consulta SQL guardada con nombre propio que se comporta como una tabla virtual. No almacena datos por sí misma, sino que los obtiene en tiempo real desde las tablas subyacentes. Se usa para simplificar consultas complejas, restringir el acceso a columnas sensibles o presentar datos pre-calculados.

```sql
-- Ejemplo de vista
CREATE VIEW resumen_ventas AS
SELECT cliente_id, COUNT(*) AS total_pedidos, SUM(monto) AS total_gastado
FROM pedidos
GROUP BY cliente_id;
```

#### Índice
Es una estructura auxiliar que acelera las búsquedas sobre una o más columnas de una tabla, similar al índice de un libro. Al crear un índice, el RDBMS mantiene una copia ordenada de esa columna para evitar escanear toda la tabla en cada consulta. El costo es un mayor espacio en disco y mayor tiempo en escrituras (INSERT/UPDATE/DELETE).

```sql
-- Acelera búsquedas por email
CREATE INDEX idx_clientes_email ON clientes(email);
```

#### Llave Primaria (Primary Key)
Es una columna (o combinación de columnas) que identifica de forma **única e irrepetible** cada fila de una tabla. No puede contener valores nulos. El RDBMS crea automáticamente un índice sobre ella. Es el punto de referencia desde el cual otras tablas pueden relacionarse.

```sql
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,  -- Llave primaria
    nombre VARCHAR(100)
);
```

#### Llave Foránea (Foreign Key)
Es una columna en una tabla que referencia la llave primaria de otra tabla, estableciendo una relación entre ambas. Garantiza la **integridad referencial**: no puede existir un registro con una llave foránea que apunte a un valor inexistente en la tabla referenciada.

```sql
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),  -- Llave foránea
    monto DECIMAL(10,2)
);
```

---
