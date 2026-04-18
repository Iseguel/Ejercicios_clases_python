# Catálogo inicial
# Usamos una lista de diccionarios
catalogo = [
    {"id": 1, "nombre": "Box_1", "categoria": "S", "precio": 1550},
    {"id": 2, "nombre": "Box_2", "categoria": "M", "precio": 6500},
    {"id": 3, "nombre": "Box_3", "categoria": "L", "precio": 17500},
    {"id": 4, "nombre": "Box_4", "categoria": "XL", "precio": 30000},
    {"id": 5, "nombre": "Box_5", "categoria": "XXL", "precio": 60000},
    {"id": 6, "nombre": "Box_6", "categoria": "XXL", "precio": 75000},
]

# El carrito inicia vacío
carrito = []


#imprime el menu principal
def menu_principal():
    print("  ----------------------------------------  ")
    print("----        Bienvenido a 3D STORE       ----")
    print("  ----------------------------------------  ")
    print("----     Ingresa numero de la opcion    ----")
    print("(1) Ver catálogo de productos."              ) 
    print("(2) Buscar producto por nombre o categoría." ) 
    print("(3) Agregar producto al carrito."            )
    print("(4) Ver carrito y total."                    ) 
    print("(5) Vaciar carrito."                         ) 
    print("(0) Salir."                                  ) 
    print("  ----------------------------------------  ")

#imprime el menu buscar producto
def menu_busqueda():
    print("  ----------------------------------------  ")
    print("----           BUSCAR PRODUCTO          ----")
    print("  ----------------------------------------  ")
    print(" Selecciona el metodo de busqueda:          ")
    print("  (1) Busqueda por nombre                   ")
    print("  (2) Busqueda por categoria                ")
    print("  (3) Busqueda por id                       ")
    print("  (4) Volver                                ")
    print("  ----------------------------------------  ")

#imprime el menu para agregar productos al carrito
def menu_agregar():
    print("  ----------------------------------------  ")
    print("----    AGREGAR PRODUCTO AL CARRITO     ----")
    print("  ----------------------------------------  ")
    print(" Selecciona el metodo para agregar al carro ")
    print("  (1) Agregar por numero de ID              ")
    print("  (2) Agregar por nombre                    ")
    print("  (3) Volver                                ")
    print("  ----------------------------------------  ")

#imprime el catalogo de productos 
def ver_catalogo():
    print("  ----------------------------------------  ")
    print("----          CATALOGO 3D STORE         ----")
    print("  ----------------------------------------  ")
    for producto in catalogo:
        print(f" {producto["id"]} - {producto["nombre"]} = ${producto['precio']}")
    print("  ----------------------------------------  ") 
    input("presione enter par continuar  ") #mantine la pantalla hasta presionar enter 
    
#Busca productos en catalogo y los imprime en una lista
def busqueda(tipo_busqueda):
    print("  ----------------------------------------  ")
    print(f"----         BUSQUEDA POR {tipo_busqueda}        ----")
    print("  ----------------------------------------  ")
    nombre_busqueda = input(f"Ingrese {tipo_busqueda} del producto: ")
    resultados = []
    for producto in catalogo: #busca los productos en el catalogo 
        if tipo_busqueda == "nombre" or tipo_busqueda == "categoria":
            if nombre_busqueda.strip().lower() in producto[tipo_busqueda].lower():
                resultados.append(producto) #agrega los productos encontrados a resultados
        elif nombre_busqueda.isdigit():
            if int(nombre_busqueda) == producto[tipo_busqueda]:
                resultados.append(producto) #agrega los productos encontrados a resultados
    if resultados: #si hay resultados imprime una lista con los resultado 
        for producto in resultados:
            print(f" {producto['id']} - {producto['nombre']} | Categoría: {producto['categoria']} | ${producto['precio']}")
        print(" ")
        input("- Presione enter para continuar -") #mantine la pantalla hasta presionar enter 
    else:
        print(" ")
        print(" *** Producto no encontrado ***")

def cantidad_produto():
    cantidad = input(f"Ingrese la cantidad: ")
    if cantidad.isdigit():
        cantidad = int(cantidad)
        return cantidad
    else:
        print(" *** Ingrese solo numeros ***")
        return 0
        

    

#Agrega productos a la lista carrito 
def agregar_al_carrito(tipo_busqueda):
    print("  ----------------------------------------  ")
    print(f"----        AGREGAR POR {tipo_busqueda}       ----")
    print("  ----------------------------------------  ")
    resultados = False
    nombre_busqueda = input(f"Ingrese {tipo_busqueda} del producto: ")
    for producto in catalogo: #busca los productos en el catalogo 
        if tipo_busqueda == "nombre" or tipo_busqueda == "categoria":
            if nombre_busqueda.strip().lower() == producto[tipo_busqueda].lower():
                cantidad = (cantidad_produto() + 1)
                if cantidad > 0:
                    for a in range(cantidad):
                        carrito.append(producto) #agrega los productos encontrados a resultados
                    print("")
                    print(f" --- Se agrego {a} unidades de {producto["nombre"]} al carrito | ${a * producto["precio"]}")
                    resultados = True
        elif nombre_busqueda.isdigit():
            if int(nombre_busqueda) == producto[tipo_busqueda]: #busca por id               
                cantidad = (cantidad_produto() + 1)
                if cantidad > 1:
                    for a in range(1,cantidad):
                        carrito.append(producto) #agrega los productos encontrados a resultados
                    print("")
                    print(f" --- Se agrego {a} unidades de {producto["nombre"]} al carrito | ${a * producto["precio"]}")
                    resultados = True    
    if not resultados:   
        print(" *** Producto no encontrado ***")

def imprime_carrito():
    if carrito:
        total_carrito = 0
        for producto in carrito:
            print(f"  {producto["nombre"]} | Categoría: {producto["categoria"]} | ${producto["precio"]}")
            total_carrito += producto["precio"]
        print("  ----------------------------------------  ")
        print(f"                  Total = ${total_carrito}")
        print(" ")
        input("- Presione enter para continuar -") #mantine la pantalla hasta presionar enter 
    else:
        print(" *** El carrito esta vacio ***")

#loop principal
while True:
    menu_principal()
    opcion = input("  ")
    match opcion:
        case "1": #Ver catalogo de productos 
            ver_catalogo()    

        case "2": #Buscar producto por nombre o categoria
            estado_menu_busqueda = True
            while(estado_menu_busqueda):
                menu_busqueda()
                opcion = input("  ")
                if opcion == "1": #Busqueda por nombre          
                    busqueda("nombre")                      
                elif opcion == "2": #Busqueda por categoria               
                    busqueda("categoria")
                elif opcion == "3": #Busqueda por id             
                    busqueda("id")
                elif opcion == "4": #Volver
                    print("  ")
                    estado_menu_busqueda = False
                else: #opcion no valida 
                    print("*** opcion no valida, solo numeros 1, 2, 3 0 4 ***")
                    
        case "3": #Agregar producto al carrito           
            while True:
                menu_agregar()
                opcion = input("  ")
                if opcion == "1": #Agregar por id        
                    agregar_al_carrito("id")                      
                elif opcion == "2": #Agregar por nombre               
                    agregar_al_carrito("nombre")
                elif opcion == "3": #Volver
                    print("  ")
                    break
                else: #opcion no valida 
                    print("*** opcion no valida, solo numeros 1, 2 o 3 ***")
            
        case "4": #Ver carrito y total
            print("  ----------------------------------------  ")
            print("----         CARRITO DE COMPRAS         ----")
            print("  ----------------------------------------  ")
            imprime_carrito()

        case "5":#Vaciar carrito
            print("  ----------------------------------------  ")
            print("----            CARRITO VACIO           ----")
            print("  ----------------------------------------  ")
            carrito = []

        case "0":#Salir
            print("  ----------------------------------------  ")
            print("----    Ten un buen dia, vuelve pronto  ----")
            print("  ----------------------------------------  ")
            break

        case _: #default
            print("********************************************************")
            print("**     opcion no valida, solo numeros del 0 al 5      **")
            print("********************************************************")