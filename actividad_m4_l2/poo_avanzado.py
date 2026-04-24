

# 4 – Colaboración: clase Autor 
class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

# 5 – Composición: clase Editorial 
class Editorial:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

# 1 – Clase Libro con constructor
class Libro:
    def __init__(self, titulo, autor, anio_publicacion, nombre_editorial, ciudad_editorial):
        self.titulo = titulo
        self.autor = autor                          # objeto de tipo Autor (colaboración)
        self.anio_publicacion = anio_publicacion
        self.editorial = Editorial(nombre_editorial, ciudad_editorial)  # composición: se crea AQUÍ

    def mostrar_info(self):
        print("-" * 42)
        print("*   Información del libro   *")
        print("")
        print(f"  Título          : {self.titulo}")
        print(f"  Año publicación : {self.anio_publicacion}")
        # Ejercicio 4: muestra datos del objeto Autor
        print(f"  Autor           : {self.autor.nombre}")
        print(f"  País del autor  : {self.autor.pais}")
        # Ejercicio 5: muestra datos del objeto Editorial
        print(f"  Editorial       : {self.editorial.nombre}")
        print(f"  Ciudad          : {self.editorial.ciudad}")
        print("-" * 42)

    
    #  2 – Accesadores y mutadores
    def get_titulo(self):
        return self.titulo

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_anio_publicacion(self):
        return self.anio_publicacion

    def set_anio_publicacion(self, anio_publicacion):
        self.anio_publicacion = anio_publicacion

    
    # 3 – Sobrecarga de métodos (simulada con valor por defecto)
    def resumen(self, texto=None):
        print("")
        print(" ===   Resumen del libro   ===")
        print("")
        if texto is None:
            print(" *** Libro sin resumen disponible ***")
        else:
            print(f"  {texto}")
        print("-" * 42)


# ============================================================

autor_1 = Autor("Frank Herbert", "Estados Unidos")
libro_1 = Libro("Dune", autor_1, 1965, "RoBooks", "Santiago")

libro_1.mostrar_info()

libro_1.set_titulo("Dune Mesías")
libro_1.set_anio_publicacion(1969)

libro_1.mostrar_info()

libro_1.resumen()
libro_1.resumen("Continúa la historia de Paul Atreides en el planeta Arrakis.")


autor_2 = Autor("Isaac Asimov", "Rusia")
libro_2 = Libro("Fundación", autor_2, 1951, "Libros del cerro", "concepción")

libro_2.mostrar_info()
libro_2.resumen("Narra la caída del Imperio Galáctico y el plan para preservar el conocimiento.")
