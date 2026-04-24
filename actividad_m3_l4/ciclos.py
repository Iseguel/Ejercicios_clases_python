#1. Uso básico de while 
#Escribe un programa que imprima los números del 1 al 5 usando un ciclo while. 

ciclo = 0
while ciclo < 5:
    ciclo += 1
    print(ciclo)

#2. Uso básico de for 
#Escribe un ciclo for que recorra una lista de frutas (["manzana", "plátano", "naranja"]) y las imprima  en pantalla. 

frutas = ["manzana", "plátano", "naranja"]
for f in frutas:
    print(f)

#3. Condición en un ciclo 
#Crea un ciclo for que recorra los números del 1 al 10. Si encuentra un número par, imprime "Par", si es impar, imprime "Impar". 

for i in range(1, 11):
    if i % 2 == 0:
        print(f" {i} es par")
    else:
        print(f" {i} es inpar")

#4. Ciclo infinito controlado con break 
#Escribe un ciclo while True que solicite ingresar un número. El ciclo debe terminar si el número ingresado es  0. Usa break para salir. 
while True:
    ingreso = input("Ingrese un numero: ")
    if ingreso.isdigit():
        if int(ingreso) == 0:
            break
    else:
        print("*** ingreso no valido")

#5. Ciclo anidado 
#Escribe un programa que imprima una tabla de multiplicar del 1 al 3, usando un ciclo for dentro de otro for.

for tabla in range (1, 4):
    print(f" Tabla del {tabla}:")
    for i in range(1, 11):
        resultado = tabla * i
        print(f" {tabla} x {i} = {resultado}")
    print("...")
    
#6. Uso de continue 
#Recorre una lista de nombres. Si el nombre es "Juan", omítelo usando continue. Imprime todos los demás. 
lista_nombres = ["Felipe", "Nicolas", "Juan", "Pedro", "Antonio"]
for nombre in lista_nombres:
    if nombre != "Juan":
        print(nombre)
    else:
        continue

