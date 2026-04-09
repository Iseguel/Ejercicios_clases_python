#1. Decisión simple, evalua si el usuario es mayor de edad.
numero_ingresado = input("--- 1. Ingrese edad: ")
if numero_ingresado.isdigit():
    edad = int(numero_ingresado)
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
else:
    print("----------------------------------------")
    print("   El numero ingresado no es valido")
    print("    ingrese solo numeros naturales")
    print("----------------------------------------")


#2. Decisión múltiple con elif, clasificar una nota del 1 al 7 usando elif.
numero_ingresado = input("--- 2. Ingrese una calificacion entre 1 y 7: ")
if numero_ingresado.isdigit():
    calificacion = int(numero_ingresado)
    if calificacion == 7:
        print("Excelente")
    elif calificacion == 6:
        print("Muy bien")
    elif calificacion == 5:
        print("Bien")
    elif calificacion == 4:
        print("Suficiente")   
    elif calificacion < 4 and calificacion >= 1:
        print("Insuficiente")  
    else:
        print("----------------------------------------")
        print("   El numero ingresado no es valido")
        print("   ingrese solo numeros entre 1 y 7")
        print("----------------------------------------")
else:
    print("----------------------------------------")
    print("   El numero ingresado no es valido")
    print("   ingrese solo numeros entre 1 y 7")
    print("----------------------------------------")



#3. Condiciones anidadas, determinar si un número es positivo, negativo o cero usando anidación.
numero_ingresado = input("--- 3. Ingrese un numero entero: ")
if numero_ingresado.isdigit():
    nuevo_numero = int(numero_ingresado)
    if nuevo_numero > 0:
        print("Número positivo")
    elif nuevo_numero == 0:
        print("Es cero")
    elif nuevo_numero < 0:
        print("Número negativo")
else:
    print("----------------------------------------")
    print("   El numero ingresado no es valido")
    print("     ingrese solo numeros enteros")
    print("----------------------------------------")



#4. Condición de borde, Verificar si el número está en los límites (1 o 100), dentro o fuera.
numero_ingresado = input("--- 4. Ingrese un numero entre 1 y 100: ")
if numero_ingresado.isdigit():
    numero_cien = int(numero_ingresado)
    if numero_cien == 1 or numero_cien == 100:
        print("Estás en un límite permitido")
    elif numero_cien > 1 and numero_cien < 100:
        print("Numero dentro del rango")
    else:
        print(" ")
        print("Numero fuera del rango")
 


