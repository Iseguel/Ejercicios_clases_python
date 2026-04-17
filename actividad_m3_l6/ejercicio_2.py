#Ejercicio 2: 
#Realizar un programa que lea por teclado las 5 notas obtenidas 
#por un alumno (comprendidas entre  0 y 10). 
#A continuación, debe mostrar todas las notas, 
#la nota media, la nota más alta que ha sacado  y la menor.  
def calcular_promedio(notas):
    promedio = round((sum(notas)/len(notas)), 1)
    return promedio

def revision_notas(nombre, notas):
    print("========================================")
    print(f"Estudiante: {nombre}")
    print("Notas:")
    for n in notas:
        print (f" - {n}")
    print(f"Nota maxima  = {max(notas)}")
    print(f"Nota media = {calcular_promedio(notas)}")
    print(f"Nota minima = {min(notas)}")

while True:
    lista_nota = []
    nombre = input("Ingrese el nombre del estudiante o (s) para salir: ")
    if nombre == "s":
        print(" ------------ Fin ------------")
        break
    else:
        for i in range(5):
            ingreso = input(f" Ingrese la nota Nro {i+1}: ")
            try:  # intenta convertir a float
                nota = float(ingreso)
                if nota >= 0 and nota <= 10:
                    lista_nota.append(nota)
                else:
                    print(" *** fuera del rango ***")
                    break
            except ValueError:            
                print(" *** ingreso no valido *** ")
                break
        if len(lista_nota) == 5:
            revision_notas(nombre, lista_nota) 
            
    