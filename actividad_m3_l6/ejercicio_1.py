#Ejercicio 1: 
#Al ingresar un numero par cualquiera que sea del 2 al 100, 
#este imprima en pantalla todos los  números pares siguientes, 
#y si ingreso un número impar cualquiera sea del 1 al 99 se imprima en  pantalla 
#todos los números impares siguientes hasta el 99. 
#Si ingreso el 0 o un número menor y si ingreso un número mayor al 100, 
#el programa debe enviar un  mensaje de que no es posible realizarlo y volver 
#a preguntar por el ingreso del número.  

#Ejemplos:  
#Numero ingresado: 80  
#Resultado: usted ha ingresado un numero par y los números pares siguientes 
#son: Resultado:  82 84 86 88 90 92 94 96 98 100 

#Numero ingresado: 81  
#Resultado: usted ha ingresado un número impar y los números impares siguientes 
#son:  Resultado: 83 85 87 89 91 93 95 97 99  

def numeros(numero):
    print("="*30)
    print(f" Numero ingresado: {numero}")
    if (numero % 2) == 0: #numeros pares
        if (numero >= 2 and numero <=100): #imprimir numeros pares siguientes 
            print("="*30)
            print(f"Usted ha ingresado un numero par y los numeros siguientes son:")
            for i in range(numero+1, 101):
                if (i % 2 == 0):
                    print(f"- numero {i} ")
                else:
                    continue
    else: 
        if (numero >= 1 and numero <=99): #numeros impares
            print("="*30)
            print(f"Usted ha ingresado un numero impar y los numeros siguientes son:")
            for i in range(numero+1, 100):
                if (i % 2 != 0):
                    print(f"- numero {i} ")
                else:
                    continue


    
while True: 
    numero = input("Ingresa un numero positivo o (s) para salir")
    if numero.isdigit():
        numero = int(numero)
        numeros(numero)
    elif numero == "s":
        break
    else:
        print(" *** Ingreso no valido, ingresa solo numeros positivos ***")

#numeros(80)

#numeros(81)
