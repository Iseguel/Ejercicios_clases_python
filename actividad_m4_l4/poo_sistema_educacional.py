# ===========================================
#  SISTEMA ESCOLAR  –  Implementación del UML
# ===========================================

class Persona:
    #clase padre para Alumno y Profesor
    def __init__(self, nombre: str, edad: str, rut: str):
        # Atributos privados (- nombre, - edad, - rut)
        self.__nombre = nombre
        self.__edad   = edad
        self.__rut    = rut

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_rut(self) -> str:
        return self.__rut

    def get_edad(self):
        return self.__edad

    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_edad(self, edad: str):
        self.__edad = edad

    def set_rut(self, rut: str):
        self.__rut = rut

    def mostrar_info(self):
        print(f"  Nombre : {self.__nombre}")
        print(f"  Edad   : {self.__edad}")
        print(f"  RUT    : {self.__rut}")

class Alumno(Persona):   #Hereda de Persona. 
    def __init__(self, nombre: str, edad: str, rut: str, numero_lista: int):
        super().__init__(nombre, edad, rut)
        self.notas        : list = []   # + notas : list
        self.asistencia   : int  = 0    # + asistencia : int
        self.numero_lista : int  = numero_lista  # + numero_lista : int

    def estudiar(self) -> None:
        print(f"  {self.obtener_nombre()} está estudiando.")

    def asistir(self) -> None:          # renombrado para no chocar con el atributo
        self.asistencia += 1
        print(f"  {self.obtener_nombre()} registró asistencia "
              f"(total: {self.asistencia}).")

    def agregar_nota(self, nota: float):
        self.notas.append(nota)

    def mostrar_info(self):
        print(f"[Alumno #{self.numero_lista}]")
        super().mostrar_info()
        print(f"  Notas      : {self.notas}")
        print(f"  Asistencia : {self.asistencia} días")

class Profesor(Persona): #Hereda de Persona. 
    def __init__(self, nombre: str, edad: str, rut: str,
                 especialidad: str):
        super().__init__(nombre, edad, rut)
        self.especialidad: str = especialidad   # + especialidad : string

    def dictar_clase(self) -> None:
        print(f"  Prof. {self.obtener_nombre()} está dictando clase ({self.especialidad}).")

    def prueba(self) -> None:
        print(f"  Prof. {self.obtener_nombre()} está tomando una prueba.")

    def control(self) -> None:
        print(f"  Prof. {self.obtener_nombre()} está tomando un control.")

    def mostrar_info(self):
        print("[Profesor]")
        super().mostrar_info()
        print(f"  Especialidad : {self.especialidad}")


class Materia:
    def __init__(self, nombre: str, horas: int, dias: int):
        self.nombre: str = nombre   # + nombre : string
        self.horas : int = horas    # + horas  : int
        self.dias  : int = dias     # + dias   : int

    def contenido(self) -> str:
        info = (f"Materia '{self.nombre}' | "
                f"{self.horas} hrs/semana | "
                f"{self.dias} día(s)/semana")
        print(f"  {info}")
        return info

class Curso:
    #composición con Grado, asociación con Materia y Profesor.
    def __init__(self, seccion: str, año: str,
                 profesor: Profesor, materia: Materia):
        self.seccion          : str      = seccion   # + seccion : string
        self.año              : str      = año        # + año     : string
        self.cantidad_alumnos : int      = 0          # + cantidad_alumnos : int
        self._alumnos         : list     = []
        self.profesor         : Profesor = profesor   # asociación con Profesor
        self.materia          : Materia  = materia    # dependencia con Materia

    def agregar_alumno(self, alumno: Alumno) -> None:
        self._alumnos.append(alumno)
        self.cantidad_alumnos += 1
        print(f"  Alumno '{alumno.obtener_nombre()}' agregado "
              f"al curso {self.seccion} ({self.año}).")

    def profesor_acargo(self) -> None:
        print(f"  Profesor a cargo: {self.profesor.obtener_nombre()} "
              f"– {self.profesor.especialidad}")

    def mostrar_detalle(self):
        print(f"\n{'='*40}")
        print(f"  CURSO  : {self.seccion}  |  Año: {self.año}")
        self.profesor_acargo()
        self.materia.contenido()
        print(f"  Alumnos ({self.cantidad_alumnos}):")
        for a in self._alumnos:
            print(f"    #{a.numero_lista} {a.obtener_nombre()}")
        print(f"{'='*40}")


class Grado:
    def __init__(self, nombre: str, tipo: str):
        self.nombre : str  = nombre   # + nombre : string
        self.tipo   : str  = tipo     # + tipo   : string
        self._cursos: list = []       # composición → Curso

    def agregar_curso(self, curso: Curso):
        self._cursos.append(curso)
        print(f"  Curso '{curso.seccion}' agregado al grado '{self.nombre}'.")

    def lista_de_cursos(self) -> list:
        return self._cursos

    def mostrar_cursos(self):
        print(f"\n[Grado: {self.nombre} – {self.tipo}]")
        for c in self._cursos:
            c.mostrar_detalle()

class Establecimiento:
    def __init__(self, nombre_establecimiento: str, direccion: str):
        self.nombre_establecimiento: str  = nombre_establecimiento
        self.direccion             : str  = direccion
        self.cantidad_de_alumnos   : int  = 0          # + cantidad_de_alumnos : int
        self._grados               : list = []
        self._profesores           : list = []

    def agregar_grado(self, grado: Grado) -> None:
        self._grados.append(grado)
        # actualiza contador sumando alumnos de todos los cursos del grado
        for curso in grado.lista_de_cursos():
            self.cantidad_de_alumnos += curso.cantidad_alumnos
        print(f"  Grado '{grado.nombre}' agregado a {self.nombre_establecimiento}.")

    def lista_profesores(self) -> None:
        print(f"\n[Profesores de {self.nombre_establecimiento}]")
        if not self._profesores:
            print("  (sin profesores registrados)")
        for p in self._profesores:
            print(f"  – {p.obtener_nombre()} ({p.especialidad})")

    def registrar_profesor(self, profesor: Profesor):
        #Registra a un profesor en el establecimiento.
        self._profesores.append(profesor)

    def mostrar_info(self):
        print(f"\n{'*'*45}")
        print(f"  ESTABLECIMIENTO : {self.nombre_establecimiento}")
        print(f"  Dirección       : {self.direccion}")
        print(f"  Total alumnos   : {self.cantidad_de_alumnos}")
        print(f"  Grados          : {len(self._grados)}")
        print(f"{'*'*45}")


#  EJEMPLO DE USO

if __name__ == "__main__":

    # Establecimiento
    colegio = Establecimiento("Liceo Nacional", "Av. Principal 123")

    # Profesores
    prof_1 = Profesor("Sra. García",  "38", "12.345.678-9", "Matemáticas")
    prof_2 = Profesor("Sr. Ramírez",  "45", "98.765.432-1", "Historia")
    colegio.registrar_profesor(prof_1)
    colegio.registrar_profesor(prof_2)

    # Materias
    mat_1 = Materia("Álgebra",  4, 3)
    mat_2 = Materia("Historia", 3, 2)

    # Cursos
    curso_a = Curso("1°A", "2025", prof_1, mat_1)
    curso_b = Curso("1°B", "2025", prof_2, mat_2)

    # Alumnos
    alumno_1 = Alumno("Juan Pérez",   "16", "20.123.456-7", 1)
    alumno_2 = Alumno("Ana Torres",   "15", "21.234.567-8", 2)
    alumno_3 = Alumno("Luis Castillo","16", "22.345.678-9", 3)

    curso_a.agregar_alumno(alumno_1)
    curso_a.agregar_alumno(alumno_2)
    curso_b.agregar_alumno(alumno_3)

    grado_primero = Grado("Primero Medio", "Científico-Humanista")
    grado_primero.agregar_curso(curso_a)
    grado_primero.agregar_curso(curso_b)

    colegio.agregar_grado(grado_primero)

    colegio.mostrar_info()
    colegio.lista_profesores()
    grado_primero.mostrar_cursos()

    print("\n[Acciones]")
    alumno_1.estudiar()
    alumno_1.asistir()
    alumno_1.agregar_nota(6.5)
    alumno_1.mostrar_info()

    prof_1.dictar_clase()
    prof_1.prueba()

    mat_1.contenido()