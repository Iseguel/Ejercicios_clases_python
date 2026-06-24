# Diccionario de Datos — Universidad (Estudiantes, Cursos, Matrículas)

## Resumen del modelo conceptual

- **Entidades fuertes:** `Estudiante` y `Curso`. Ambas tienen identificador propio (`rut`, `codigo`) que no depende de ninguna otra entidad, por lo que **no existen entidades débiles** en este escenario.
- **Relación:** `Estudiante` (N) — `Matricula` — (M) `Curso`. Es una relación muchos a muchos, y como tiene atributos propios (`fecha_inscripcion`, `anio`), se transforma obligatoriamente en una **tabla intermedia** en el modelo relacional.

---

## Tabla: `estudiante`

| Campo  | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones |
|--------|--------------|----------------|-----------------|-----------------|----------------------------------------|
| rut    | VARCHAR(10)  | No             | Sí              | No              | Identificador único del estudiante |
| nombre | VARCHAR(100) | No             | No              | No              | Nombre completo del estudiante |
| correo | VARCHAR(150) | No             | No              | No              | Correo de contacto; se restringe como único (UNIQUE) |

## Tabla: `curso`

| Campo                | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones |
|-----------------------|--------------|----------------|-----------------|-----------------|----------------------------------------|
| codigo                | VARCHAR(10)  | No             | Sí              | No              | Identificador único del curso |
| nombre                | VARCHAR(100) | No             | No              | No              | Nombre del curso |
| docente_responsable   | VARCHAR(100) | No             | No              | No              | Nombre del docente a cargo del curso |

## Tabla: `matricula`

| Campo               | Tipo de Dato | Permite Nulos | Clave Primaria   | Clave Foránea            | Observaciones |
|----------------------|--------------|----------------|--------------------|----------------------------|----------------------------------------------------|
| rut_estudiante       | VARCHAR(10)  | No             | Sí (compuesta)     | Sí → `estudiante.rut`      | Identifica al estudiante matriculado |
| codigo_curso         | VARCHAR(10)  | No             | Sí (compuesta)     | Sí → `curso.codigo`        | Identifica el curso en el que se matricula |
| fecha_inscripcion    | DATE         | No             | No                 | No                         | Fecha exacta en que se realizó la matrícula |
| anio                 | INTEGER      | No             | No                 | No                         | Año académico de la matrícula (restringido a >= 2000) |

> La clave primaria compuesta `(rut_estudiante, codigo_curso)` impide que el mismo estudiante quede matriculado dos veces en el mismo curso. Si la universidad permite repetir un curso en años distintos, se debe reemplazar por una clave surrogate `id_matricula` + restricción `UNIQUE (rut_estudiante, codigo_curso, anio)` (ver nota en `modelo_relacional.sql`).

---

## Reflexión

**¿Cuál fue la mayor dificultad al transformar el modelo conceptual al relacional?**

La mayor dificultad no fue decidir cómo representar correctamente la relación N:M `Matricula`. Al tener atributos propios (`fecha_inscripcion`, `anio`) no bastaba con una FK simple en una de las dos tablas; era necesaria una tabla intermedia. Y dentro de esa tabla intermedia identficar qué clave usar como primaria.

**¿Qué ventajas tiene normalizar una base de datos? ¿Y cuándo conviene desnormalizarla?**

Normalizar (llevar las tablas a 2FN/3FN, como se hizo aquí al separar `Matricula` de `Estudiante` y `Curso`) evita la redundancia de datos no se repite el nombre del curso en cada fila de matrícula, reduce el riesgo de inconsistencias al actualizar y mantiene la integridad referencial mediante las FK. El costo es que las consultas que necesitan combinar información requieren más `JOIN`. Desnormalizar conviene cuando el sistema prioriza la velocidad de lectura sobre el modelo: reportes, dashboards, p
