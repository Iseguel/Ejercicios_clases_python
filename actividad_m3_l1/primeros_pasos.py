
# Importamos 'math' para acceder a funciones matemáticas avanzadas 
import math


print("¡Hola! Este es mi primer programa en Python.")

nombre = "Ismael"
edad = 35
ciudad = "Santiago"

print("Mi nombre es", nombre, "tengo", edad, "años y vivo en", ciudad)

#Suma de numeros
numeros = [0,1,2,3,4,5,6,7,8,9] #declaracion
resultadoSuma =  numeros[3] + numeros[5]  #Suma de numeros y asignacion a sum
print(f"La suma de {numeros[3]} + {numeros[5]} es = {resultadoSuma}")     #imprime la suma 

# número al que queremos calcularle la raíz.
numero_raiz = 25

# función sqrt() del módulo math. 
# siempre devuelve un número de tipo flotante (con decimales).
raiz_cuadrada = math.sqrt(numero_raiz)

# imrime el resultado de la raiz 
print(f"La raíz cuadrada de {numero_raiz} es: {raiz_cuadrada}")