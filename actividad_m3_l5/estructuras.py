#------------------------------------------------
# 1. Crea estructuras
#-----------------------------------------------
# --- LISTA ---
# Es mutable (puedes cambiar sus elementos) y mantiene el orden.
lista = ["a", "b", "c", "d"]
print("Lista:", lista)

# --- TUPLA ---
# Es inmutable. Una vez creada, no puedes modificar sus valores. 
# Es más rápida y segura para datos que no deben cambiar.
tupla = ("E", "F", "G", "H")
print("Tupla:", tupla)

# --- CONJUNTO (SET) ---
# No permite duplicados y sus elementos no tienen un orden fijo.
conjunto = {"i", "j", "k", "l"}
print("Conjunto:", conjunto)

# --- DICCIONARIO ---
# Diferencia: Almacena pares de clave:valor. Accedes a los datos por su clave
diccionario = { "nombre": "Ismael", "edad": 36, "mascota": "Gato"}
print("Diccionario:", diccionario)

#------------------------------------------------
#2. Acceder a elementos 
#-----------------------------------------------

print(f" Segundo elemento de la lista: {lista[1]}")
claves=[]
claves = diccionario.keys()
print(f"clave: {claves} - Valor: {diccionario['nombre']}")

# el indice asume un orden fijo, pero el set no esta ordenado es rapido
# para saber si un elemento ya existe pero no en que posicion esta 
#

#-----------------------------------------------
#3. Contar e iterar 
#-----------------------------------------------
print(f"Largo de lista: {len(lista)}")
for i in range(len(lista)):
    print(f" {i} - {lista[i]}")
print(" ---------------- ")

print(f"Largo de tupla: {len(tupla)}")
for i in range(len(tupla)):
    print(f" {i} - {tupla[i]}")
print(" ---------------- ")    

print(f"Largo de set: {len(conjunto)}")
for elemento in conjunto:
    print(f" {elemento}")

print(" ---------------- ")
print(f"Largo de diccionario: {len(diccionario)}")
for clave in diccionario:
    print(f" {clave} : {diccionario[clave]}")


#-----------------------------------------------
#4. Modificar estructuras 
#-----------------------------------------------
# Agrega un nuevo elemento a la lista y al conjunto. 
print(f"conjunto {conjunto}")
conjunto.add("M")
print(f"conjunto {conjunto}")

# Borra un elemento de la lista. 
print(f"lista {lista}")
lista.pop(0)
print(f"lista {lista}")

# Agrega una nueva clave al diccionario. 
print(f"diccionario {diccionario}")
diccionario["ciudad"] = "Santiago"
print(f"diccionario {diccionario}")

#Intenta modificar la tupla y comenta qué ocurre.
#tupla[0] = 45
#como la tupla es inmutable no permite cambiarla 

#TypeError: 'tuple' object does not support item assignment
#-----------------------------------------------