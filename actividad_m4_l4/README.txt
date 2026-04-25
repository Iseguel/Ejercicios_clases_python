===========================================================
PROYECTO: SISTEMA ESCOLAR - IMPLEMENTACIÓN POO
===========================================================

DESCRIPCIÓN:
Este proyecto es una implementación en Python de un sistema 
educacional utilizando los principios de la Programación Orientada a 
Objetos (POO). Modela la jerarquía y administración básica de un 
colegio, abarcando desde los alumnos hasta el establecimiento mismo.

ESTRUCTURA DE CLASES:
- Persona: Clase base con atributos encapsulados (nombre, edad, rut).
- Alumno y Profesor: Heredan de Persona, añadiendo atributos y 
  comportamientos específicos (ej. estudiar(), dictar_clase()).
- Materia: Define la asignatura con sus respectivas horas y días.
- Curso: Relaciona a los alumnos con un profesor y una materia.
- Grado: Agrupa varios cursos bajo un mismo nivel (ej. "Primero Medio").
- Establecimiento: Clase principal que administra los grados, el registro 
  de profesores y contabiliza el total de alumnos.

CONCEPTOS DE POO APLICADOS:
- Herencia: Reutilización de código de 'Persona' hacia 'Alumno' y 'Profesor'.
- Encapsulamiento: Uso de atributos privados (__) y métodos accesadores (get/set).
- Composición / Agregación: Construcción de objetos complejos a partir de 
  otros más simples (Establecimiento -> Grado -> Curso).

EJECUCIÓN:
Ejecutar mediante el comando: `python poo_sistema_educacional.py`