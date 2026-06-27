# Módulo 7: Acceso a Datos en Aplicaciones Python Django

## 1. Propósito
Implementar la capa de acceso a datos del e-commerce utilizando Django y su ORM, permitiendo administrar el catálogo de productos mediante operaciones CRUD, integrando modelos, relaciones, migraciones y consultas, dentro de una aplicación web basada en el patrón MVC de Django.

## 2. Objetivos de Aprendizaje
* **Configurar** la conexión de Django con una base de datos relacional.
* **Definir** modelos de datos utilizando el ORM de Django.
* **Implementar** relaciones entre entidades del dominio.
* **Utilizar** migraciones para mantener sincronizado el esquema de base de datos.
* **Realizar** operaciones CRUD sobre la base de datos utilizando el ORM.
* **Integrar** la capa de datos con vistas y templates de Django.

## 3. Alcance del Ejercicio (MVP — Administración)
Se debe implementar un módulo de administración de productos, funcionando como si el usuario fuera un administrador del e-commerce, enfocado exclusivamente en la gestión del catálogo.

### Funcionalidades Mínimas
* Listar productos almacenados en la base de datos.
* Crear nuevos productos mediante un formulario.
* Editar productos existentes.
* Eliminar productos del catálogo.
* Mostrar mensajes de éxito o error al realizar operaciones.

## 4. Requisitos Funcionales

### Vistas / Rutas Sugeridas (Referenciales)
* `/products/`
  * Listado de productos
* `/products/create/`
  * Formulario de creación
* `/products/edit/<id>/`
  * Formulario de edición
* `/products/delete/<id>/`
  * Eliminación de producto

### Reglas Funcionales Mínimas
* Los formularios deben validar campos obligatorios.
* El precio del producto debe ser mayor a `0`.
* Al editar o eliminar, el producto debe existir en la base de datos.
* Ante errores, se deben mostrar mensajes claros al usuario.

## 5. Requisitos Técnicos
* Uso de **Django ORM** para todas las operaciones de datos.
* Definición de modelos en `models.py`.
* Uso de **relaciones ORM** cuando corresponda (por ejemplo, producto–categoría).
* Uso de **migraciones** (`makemigrations` y `migrate`).
* Uso de **vistas Django** para manejar las operaciones CRUD.
* Uso de **templates** para renderizar formularios y listados.
* Uso del **sistema de mensajes de Django** (`django.contrib.messages`) para feedback al usuario.
* Registro del modelo `Producto` en el sitio administrativo de Django (`admin.py`).

## 6. Entregables
El estudiante debe entregar:
* Proyecto Django comprimido en un archivo `.zip` o enlace a un repositorio.
* Modelos definidos en `models.py`.
* Migraciones creadas y aplicadas.
* Vistas y templates que implementen el CRUD de productos.
* Evidencia del uso del panel administrativo de Django.
* Archivo `README.md` que incluya:
  * Motor de base de datos utilizado.
  * Descripción del modelo de datos.
  * Rutas principales del módulo de administración.
  * Pasos para ejecutar el proyecto.
  * Evidencias (capturas de pantalla) del listado y formularios.

## 7. Rúbrica de Evaluación

| Criterio | Excelente (3 pts) | Adecuado (2 pts) | Básico (1 pt) | Insuficiente (0 pts) |
| :--- | :--- | :--- | :--- | :--- |
| **Modelos y ORM** | Modelos bien definidos y coherentes con el dominio. | Modelos correctos con detalles menores. | Modelos incompletos. | No define modelos funcionales. |
| **Relaciones y migraciones** | Relaciones correctas y migraciones bien aplicadas. | Migraciones funcionales con detalles menores. | Uso limitado de relaciones o migraciones. | No utiliza migraciones. |
| **CRUD de productos** | CRUD completo y funcional mediante ORM y vistas. | CRUD funcional con pequeños errores. | CRUD incompleto. | No implementa CRUD. |
| **Integración vistas + datos** | Vistas muestran y procesan datos correctamente. | Integración funcional con detalles menores. | Integración parcial. | No integra datos persistidos. |
| **Uso de Django Admin** | Modelo correctamente registrado y usable desde admin. | Admin funcional con detalles menores. | Admin limitado. | No utiliza admin. |
| **Documentación** | README claro y completo. | README comprensible pero incompleto. | README poco claro. | No presenta README. |