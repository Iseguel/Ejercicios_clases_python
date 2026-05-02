
class EdadInvalidaError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def division():
    while True:
        try:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            div = num1/num2
            print(f"La división es: {div}")
            break
        except ValueError:
            print("Ingrese solo números")
        except ZeroDivisionError:
            print("No se puede dividir por cero")
        
def validar_edad():
    try:
        edad =int(input("Ingrese su edad: "))
        if edad < 0:
            raise EdadInvalidaError("La edad no puede ser negativa")
    except EdadInvalidaError as e:
        print(e)
    else:
        print(f"Su edad es: {edad}")
    finally:
        print("Cerrando archivo...")

def ejecutar():
    print("Abriendo archivo...")
    division()
    validar_edad()

#___________________________________________________________________

ejecutar()