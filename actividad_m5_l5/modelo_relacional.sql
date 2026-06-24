-- -----------------------------------------------------
-- Tabla `estudiantes`
-- Almacena la información de cada estudiante.
-- -----------------------------------------------------
CREATE TABLE estudiantes (
  rut VARCHAR(12) PRIMARY KEY NOT NULL,
  nombre VARCHAR(255) NOT NULL,
  correo VARCHAR(255) NOT NULL UNIQUE
);

-- -----------------------------------------------------
-- Tabla `cursos`
-- Almacena la información de los cursos ofrecidos.
-- -----------------------------------------------------
CREATE TABLE cursos (
  codigo VARCHAR(10) PRIMARY KEY NOT NULL,
  nombre VARCHAR(255) NOT NULL,
  docente_responsable VARCHAR(255) NOT NULL
);

-- -----------------------------------------------------
-- Tabla `matriculas`
-- Tabla asociativa que registra la inscripción de un estudiante en un curso.
-- -----------------------------------------------------
CREATE TABLE matriculas (
  estudiante_rut VARCHAR(12) NOT NULL,
  curso_codigo VARCHAR(10) NOT NULL,
  fecha DATE NOT NULL,
  PRIMARY KEY (estudiante_rut, curso_codigo),
  FOREIGN KEY (estudiante_rut) REFERENCES estudiantes(rut),
  FOREIGN KEY (curso_codigo) REFERENCES cursos(codigo)
);



