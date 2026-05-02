#1. Escribir en un archivo
def escribir_archivo():
    try:
        with open("datos.txt", "w", encoding="utf-8") as archivo:
            archivo.write("La esclerótica amplia y despigmentada del ser humano es uno de los legados anatómicos más profundos de nuestra historia como\n"
                         "especie cooperativa. Aunque hallazgos recientes en otros primates como los chimpancés de Ngogo nos obligan a matizar la idea de una\n"
                         "singularidad absoluta, la optimización funcional del ojo humano para la señalización social sigue siendo única en la naturaleza.\n")
    except PermissionError:
        print(" ❌ Faltan permisos para crear el archivo")
    except Exception as e:
        print(f"❌ Error: {e}") 

#2. Leer el archivo completo
def leer_archivo():
    try:
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            atributos_y_cierre(archivo)
            contenido = archivo.read()
            print(contenido)
            print("______________________________________________________________________________________________")
    except FileNotFoundError:
        print(" ❌ El archivo no existe")
    except Exception as e:
        print(f"❌ Error: {e}")

#3. Leer línea por línea
def leer_linea():
    try:
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            atributos_y_cierre(archivo)
            primera_linea = archivo.readline()
            print(primera_linea)
            for linea in archivo:
                print(linea)   
            print("______________________________________________________________________________________________") 
    except FileNotFoundError:
        print(" * El archivo no existe")
    except Exception as e:
        print(f"❌ Error: {e}")

#4. Añadir contenido (modo append)
def agregar_contenido():
    try:
        with open("datos.txt", "a", encoding="utf-8") as archivo:
            archivo.write("Los humanos sacrificaron protección física y camuflaje para ganar la transparencia emocional necesaria para construir sociedades complejas.\n") 
    except PermissionError:
        print(" ❌ Faltan permisos para crear el archivo")
    except Exception as e:
        print(f"❌ Error: {e}")

#5. Atributos y cierre
def atributos_y_cierre(archivo):
    print(f"Nombre del archivo: {archivo.name}")
    print(f"Estado del archivo: {'Abierto' if not archivo.closed else 'Cerrado'}")
    print(f"Modo de apertura: {archivo.mode}")
    print("------------------------------------------")

        
#-------------------------------------------

escribir_archivo()
leer_archivo()
leer_linea()
agregar_contenido()
leer_archivo()