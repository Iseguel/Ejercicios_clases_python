#Ejercicio 3: 
#Crea un programa que pida un número al usuario un número de 
#mes (por ejemplo, el 4) y diga  cuántos días tiene 
#(por ejemplo, 30) y el nombre del mes. Debes usar 
#listas. Para simplificarlo vamos  a suponer que febrero tiene 28 días.  


meses = { "Enero": 31, 
          "Febrero": 28, 
          "Marzo": 31,
          "Abril" : 30,
          "Mayo" : 31,
          "Junio" : 30,
          "Julio" : 31,
          "Agosto" : 31,
          "Septiembre" : 30,
          "Octubre" : 31,
          "Noviembre" : 30,
          "Diciembre" : 31
        }
numero_meses = {1: "Enero",
                2: "Febrero",
                3: "Marzo",
                4: "Abril",
                5: "Mayo",
                6: "Junio",
                7: "Julio",
                8: "Agosto",
                9: "Septiembre",
                10: "Ocutubre",
                11: "Noviembre",
                12: "Diciembre"}

def dias_mes(mes):
    nombre_mes = numero_meses[mes]    
    print("===========================================")
    print(f"El mes numero {mes} corresponde a {nombre_mes}")
    print("")
    print(f" y tiene {meses[nombre_mes]} dias")
    print("===========================================")

while True:
    numero_usuario  = input("Ingrese el numero del mes o (s) para salir ")
    if numero_usuario.isdigit():
        mes = int(numero_usuario)
        dias_mes(mes)
    elif numero_usuario == "s":
        print(" ---  FIN ---")
        break
    else: 
        print("*** Mes invalido, intenta de 1 a 12 ***")
