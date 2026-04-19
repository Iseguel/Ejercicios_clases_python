#1. Exploración teórica 
#Escribe en comentarios (#) respuestas a las siguientes preguntas: 
#• ¿Qué es la programación orientada a objetos? 
# Es un paradigma de programación que se basa en el concepto de "objetos". 
# Estos objetos combinan tanto datos en forma de atributos como 
# comportamiento métodos. Se organiza el software en bloques reutilizables 
# de planos de código (clases) 
# a partir de las que se crean objetos individuales.

#• ¿En qué se diferencia de la programación estructurada? 
# La principal diferencia es cómo organizan el código y los datos.
# - La programación estructurada se centra en las funciones y los procedimientos. 
# - La programación orientada a objetos (POO) se centra en los objetos, que encapsulan
#   los datos y las funciones que operan sobre ellos. Promueve la reutilización 
#   del código y la flexibilidad (polimorfismo). 

#• Menciona un ejemplo de la vida cotidiana donde se vea reflejado el concepto de objeto. 
# Un automóvil es un ejemplo de un objeto.
# - Atributos: color, marca, modelo, número de puertas, velocidad actual.
# - Métodos: acelerar(), frenar(), encender(), apagar(), tocar_bocina().
# Cada automóvil específico es una "instancia" de la clase "Automóvil",
# compartiendo los mismos atributos y métodos, pero con valores diferentes para sus atributos.

# 2. Definición de una clase simple 


#• Define un método ladrar() que imprima "¡Guau!". 
#• Crea una instancia de la clase Perro y llama al método ladrar(). 
class Perro: #• Crea una clase llamada Perro.
    
    def __init__(self, nombre, edad, raza): #• Agrega atributos como nombre, edad y raza. 
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        
    def ladrar(self): #• Define un método llamado ladrar()  
        print("¡Guau!")
    
max = Perro("Max", 3, "Beagle") #• Crea una instancia de la clase Perro
max.ladrar() #• Llama al método ladrar()

#3. Diferenciar conceptos 
#• En comentarios, explica la diferencia entre: 
#• Clase, instancia y objeto 
#• Atributo y estado 
#• Método y comportamiento

#• Clase, instancia y objeto:
#  - Clase: Es la plantilla, el molde o el plano para crear objetos. 
#  - Objeto / Instancia: Un objeto es una "instancia" de una clase. Es la entidad concreta que se 
#                        crea usando la clase como plano, con sus propios valores para los atributos. 
#                        "max" es un objeto o una instancia de la clase Perro.

#• Atributo y estado:
#  - Atributo: Es una característicadel objeto (una variable que pertenece al objeto). 
#              Por ejemplo, "nombre", "edad" y "raza" son los atributos de la clase Perro.
#  - Estado: Es el conjunto de los valores actuales de todos los atributos de un objeto en un momento dado. 
#            El estado del objeto "max" es: nombre="Max", edad=3, raza="Beagle". 
#            El estado puede cambiar si modificamos sus atributos.

#• Método y comportamiento:
#  - Método: Es una acción o función que un objeto puede realizar. Está definido en la clase. 
#            Por ejemplo, ladrar() es un método de la clase Perro.
#  - Comportamiento: Es el conjunto de todas las acciones que un objeto puede hacer, definido por sus métodos. 
#                    El comportamiento de un objeto Perro es su capacidad de ladrar().

#4. Principios de POO 
#• Modifica la clase Perro para que los atributos estén encapsulados (prefijo _). 
#• Agrega un método mostrar_info() que devuelva el estado del objeto en forma de texto. 

class PerroEncapsulado: #• Crea una clase llamada PerroEncapsulado.
    
    def __init__(self, nombre, edad, raza): 
        self._nombre = nombre # Atributo encapsulado
        self._edad = edad     # Atributo encapsulado
        self._raza = raza     # Atributo encapsulado
        
    def ladrar(self):  
        print("¡Guau encapsulado!")
    
    def mostrar_info(self): #devuelbe el estado del objeto en forma de texto.
        return f"Nombre: {self._nombre}, Edad: {self._edad} años, Raza: {self._raza}"

#• Crea una instancia de la clase PerroEncapsulado y llama a sus métodos.
max_encapsulado = PerroEncapsulado("Max", 3, "Beagle") 
max_encapsulado.ladrar() 
print(max_encapsulado.mostrar_info())

#• Comenta brevemente qué significa la abstracción y cómo se relaciona con este ejemplo.
# Abstracción: Es el proceso de mostrar solo la funcionalidad esencial y ocultar los detalles de implementación complejos 
# En la clase Perro, la abstracción se ve en que no necesitamos saber cómo el método ladrar() imprime "¡Guau!" internamente,
# o cómo mostrar_info() construye la cadena de texto. Simplemente llamamos a estos métodos y obtenemos el resultado deseado.

