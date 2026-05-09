
 #   • (Opcional) Un archivo README.md o .txt con:
  #  o Descripción breve de la app.
   # o Cómo ejecutar el programa.


from datetime import datetime

class ProductoNoEncontradoError(Exception):
    """Se lanza cuando se busca un producto que no existe en el catálogo."""
    pass

class CantidadInvalidaError(Exception):
    """Se lanza cuando la cantidad ingresada es 0 o negativa."""
    pass

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Admin(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)

    #imprime el menu principal
    def menu_principal(self):
        print("  ----------------------------------------  ")
        print("----         3D STORE MENU ADMIN        ----")
        print("  ----------------------------------------  ")
        print("----     Ingresa numero de la opcion    ----")
        print("(1) Ver catálogo de productos."              ) 
        print("(2) Crear nuevo producto"                    ) 
        print("(3) Actualizar producto del catalogo"        )
        print("(4) Eliminar producto del catalogo"          ) 
        print("(5) Guardar catalogo en archivo"             ) 
        print("(0) Salir."                                  ) 
        print("  ----------------------------------------  ")

    def crear_producto(self):
        print("  ----------------------------------------  ")
        print("         AGREGAR NUEVO PRODUCTO"             )
        print("  ----------------------------------------  ")
        try: 
            id = int(input("Ingrese el id del producto: "))
            nuevo_nombre = input("Ingrese el nombre del producto: ")
            nueva_categoria = input("Ingrese la categoria del producto: ")  
            nuevo_precio = float(input("Ingrese el precio del producto: "))
            catalogo.agregar_producto(Producto(id, nuevo_nombre, nueva_categoria, nuevo_precio))
        except ValueError:
            print(" ❌ Ingrese solo numeros ")


    def eliminar_producto(self):
        print("  ----------------------------------------  ")
        print("         ELIMINAR PRODUCTO"                  )        
        print("  ----------------------------------------  ")
        try:
            id = int(input("Ingrese el id del producto a eliminar: "))
            catalogo.eliminar_producto(id)     
        except ValueError:
            print(" ❌ Ingrese solo numeros ")

    def actualizar_producto(self):
        try:
            id_producto = int(input("Ingrese el id del producto a actualizar: "))
        except ValueError:
            print(" ❌ Ingrese solo numeros ")
            return
        else:
            for producto in catalogo.productos:
                if producto.id == id_producto:
                    print("  ----------------------------------------  ")
                    print("           ACTUALIZAR PRODUCTO"              )        
                    print("  ----------------------------------------  ")
                    print("----     Ingresa numero de la opcion    ----")
                    print("(1) Actualizar nombre"            ) 
                    print("(2) Actualizar categoria"         ) 
                    print("(3) Actualizar precio"            ) 
                    print("  ----------------------------------------  ")
                    opcion = input("  ")
                    if opcion == "1": #actualizar nombre
                        nombre_nuevo = input("Ingrese nuevo nombre: ")
                        catalogo.actualizar_producto(id_producto, nombre_nuevo, producto.categoria, producto.precio)
                        print(" ✅ --- Se actualizo el nombre del producto ---")
                    elif opcion == "2": #actualizar categoria
                        categoria_nueva = input("Ingrese nueva categoria: ")
                        catalogo.actualizar_producto(id_producto, producto.nombre, categoria_nueva, producto.precio)
                        print(" ✅ --- Se actualizo la categoria del producto ---")
                    elif opcion == "3": #actualizar precio      
                        precio_nuevo = input("Ingrese nuevo precio: $")
                        if not precio_nuevo.isdigit():
                            print(" ❌ Ingrese solo numeros ")
                            return
                        catalogo.actualizar_producto(id_producto, producto.nombre, producto.categoria, float(precio_nuevo))
                        print(" ✅ --- Se actualizo el precio del producto ---")
                    else:
                        print("❌ opcion no valida, solo numeros 1, 2, 3")
                        return  

class Cliente(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)    
        self.carrito = Carrito()  # cada cliente tiene su propio carrito

        #imprime el menu principal
    def menu_principal(self):
        print("  ----------------------------------------  ")
        print("----        3D STORE MENU CLIENTES      ----")
        print("  ----------------------------------------  ")
        print("----     Ingresa numero de la opcion    ----")
        print("(1) Ver catálogo de productos."              ) 
        print("(2) Buscar producto por nombre o categoría." ) 
        print("(3) Agregar producto al carrito."            )
        print("(4) Ver carrito y total."                    ) 
        print("(5) Confirmar compra."                       ) 
        print("(6) Vaciar carrito."                         ) 
        print("(0) Salir."                                  ) 
        print("  ----------------------------------------  ")

    #imprime el menu buscar producto
    def buscar_producto(self):
        while True:
            print("  ----------------------------------------  ")
            print("----           BUSCAR PRODUCTO          ----")
            print("  ----------------------------------------  ")
            print(" Selecciona el metodo de busqueda:          ")
            print("  (1) Busqueda por nombre                   ")
            print("  (2) Busqueda por categoria                ")
            print("  (3) Busqueda por id                       ")
            print("  (4) Volver                                ")
            print("  ----------------------------------------  ")      
            opcion = input("  ")
            if opcion == "1": #Busqueda por nombre          
                self.busqueda("nombre")
                print(" ")
                input("- Presione enter para continuar -") #mantine la pantalla hasta presionar enter                      
            elif opcion == "2": #Busqueda por categoria               
                self.busqueda("categoria")
                print(" ")
                input("- Presione enter para continuar -") #mantine la pantalla hasta presionar enter  
            elif opcion == "3": #Busqueda por id             
                self.busqueda("id")
                print(" ")
                input("- Presione enter para continuar -") #mantine la pantalla hasta presionar enter  
            elif opcion == "4": #Volver
                print("  ")
                break
            else:
                print("❌ opcion no valida, solo numeros 1, 2, 3 0 4 ")

    def busqueda(self, tipo_busqueda):
        nombre_busqueda = input(f"Ingrese {tipo_busqueda} del producto: ")
        resultados = []
        for producto in catalogo.productos: #busca los productos en el catalogo 
            if tipo_busqueda == "nombre":
                if nombre_busqueda.strip().lower() in producto.nombre.strip().lower():
                    resultados.append(producto) #agrega los productos encontrados a resultados
            elif tipo_busqueda == "categoria":
                if nombre_busqueda.strip().lower() in producto.categoria.strip().lower():
                    resultados.append(producto) #agrega los productos encontrados a resultados
            elif nombre_busqueda.isdigit():
                if int(nombre_busqueda) == producto.id:
                    resultados.append(producto) #agrega los productos encontrados a resultados
        if resultados: #si hay resultados imprime una lista con los resultado 
            for producto in resultados:
                print(f" {producto.id} - {producto.nombre} | Categoría: {producto.categoria} | ${producto.precio}")
        else:
            print(" ")
            print(" ❌ Producto no encontrado ")

    #imprime el menu para agregar productos al carrito
    def agregar_al_carrito(self):
        while True:
            print("  ----------------------------------------  ")
            print("----    AGREGAR PRODUCTO AL CARRITO     ----")
            print("  ----------------------------------------  ")
            print(" Selecciona el metodo para agregar al carro ")
            print("  (1) Agregar por numero de ID              ")
            print("  (2) Agregar por nombre                    ")
            print("  (3) Volver                                ")
            print("  ----------------------------------------  ")
            opcion = input("  ")
            if opcion == "1": #Agregar por id          
                self.agregar("id")           
            elif opcion == "2": #Agregar por nombre             
                self.agregar("nombre")   
            elif opcion == "3": #Volver
                print("  ")
                break
    
    def cantidad_produto(self):
        cantidad = input(f"Ingrese la cantidad: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            return cantidad
        else:
            print(" ❌ Ingrese solo numeros ")
            return 0            

    def agregar(self, tipo_busqueda):
        estado = False
        nombre_busqueda = input(f"Ingrese {tipo_busqueda} del producto: ")
        for producto in catalogo.productos: #busca los productos en el catalogo 
            if tipo_busqueda == "nombre":
                if nombre_busqueda.strip().lower() == producto.nombre.strip().lower():
                    cantidad = (self.cantidad_produto() + 1)
                    if cantidad > 0:
                        for a in range(cantidad):
                            self.carrito.agregar_item(producto) #agrega los productos encontrados a resultados
                        print("")
                        print(f" ✅ --- Se agrego {a} unidades de {producto.nombre} al carrito | ${a * producto.precio}")
                        estado = True
            elif tipo_busqueda == "id":
                if nombre_busqueda.isdigit():
                    if int(nombre_busqueda) == producto.id: #busca por id      
                        cantidad = (self.cantidad_produto() + 1)
                        if cantidad > 0:
                            for a in range(1,cantidad):
                                self.carrito.agregar_item(producto) #agrega los productos encontrados a resultados
                            print("")
                            print(f" ✅ --- Se agrego {a} unidades de {producto.nombre} al carrito | ${a * producto.precio}")
                            estado = True
                else:
                    print(" ❌ Ingrese solo numeros ")
        if not estado:
            print(" ❌ Producto no encontrado ")
        

 

class Producto:
    def __init__(self, id, nombre, categoria, precio):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        


class Catalogo:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                break
        else:
            print(" ❌ Producto no encontrado")

    def actualizar_producto(self, id, nuevo_nombre, nueva_categoria, nuevo_precio):
        for producto in self.productos:
            if producto.id == id:
                producto.nombre = nuevo_nombre
                producto.categoria = nueva_categoria
                producto.precio = nuevo_precio
                break
        else:
            print(" ❌ Producto no encontrado") 

    def guardar_catalogo(self, archivo):
        try:
            with open(archivo, "w", encoding="utf-8") as f:
                for producto in self.productos:
                    f.write(f"{producto.id},{producto.nombre},{producto.categoria},{producto.precio}\n")
        except FileNotFoundError:
            print(" ❌ Archivo no encontrado")
        except PermissionError:
            print(" ❌ No tienes permisos para escribir en el archivo")
    
    def cargar_catalogo(self, archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    id, nombre, categoria,  precio = linea.strip().split(",")
                    p = Producto(int(id), nombre, categoria, float(precio))
                    self.agregar_producto(p)
        except FileNotFoundError:
            print(" ❌ Archivo no encontrado")
        except Exception as e:
            print(f"❌ Error: {e}")

         #imprime el catalogo de productos 
    
    def ver_catalogo(self):
        print("  ----------------------------------------  ")
        print("----          CATALOGO 3D STORE         ----")
        print("  ----------------------------------------  ")
        if not catalogo.productos:
            print(" *** El catalogo esta vacio ***")
        else:
            print(" ID | NOMBRE | CATEGORIA | PRECIO")
            for producto in self.productos:
                print(f"  {producto.id} -  {producto.nombre} -      {producto.categoria}    - ${producto.precio}")
        print("  ----------------------------------------  ") 
        input("presione enter par continuar  ") #mantine la pantalla hasta presionar enter 


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item) 
    
    def eliminar_item(self, id):
        for item in self.items:
            if item.id == id:
                self.items.remove(item)
                break
        else:
            print(" ❌ Producto no encontrado") 

    def vaciar_carrito(self):
        self.items = []
        

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.precio * item.cantidad
        return total
    
    def ver_carrito(self):      
        if self.items:
            productos = set(self.items)
            total_carrito = 0
            print("  ----------------------------------------  ")
            print("----         CARRITO DE COMPRAS         ----")
            print("  ----------------------------------------  ")
            print(f"{' NOMBRE':<12} | {'PRECIO UNITARIO':<15} | {'CANTIDAD':<8} | {'SUBTOTAL':<10}")
            for item in productos:
                item.cantidad = self.items.count(item)
                subtotal = item.precio * item.cantidad
                total_carrito += subtotal
                print(f" {item.nombre:<11} |  ${item.precio:<14} | {item.cantidad:^8} |  ${subtotal:<10}")
            print("  ----------------------------------------  ")
            print(f"                  TOTAL = ${total_carrito}")
            print(" ")
            input("- Presione enter para continuar -") #mantine la pantalla hasta presionar enter 
        else:
            print(" *** El carrito esta vacio ***")

    def confirmar_carrito(self):
        if self.items:  
            item_set = set(self.items)
            total_carrito = 0
            try:
                fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("compra.txt", "a", encoding="utf-8") as f:
                    f.write("  ----------------------------------------  \n")
                    f.write("          DETALLE COMPRA 3D STORE \n"          )
                    f.write("  ----------------------------------------  \n")
                    f.write(f"Fecha y hora: {fecha_hora}\n")
                    f.write("  ----------------------------------------  \n")
                    f.write(f"{' NOMBRE':<12} | {'PRECIO UNITARIO':<15}  | {'CANTIDAD':<8} | {'SUBTOTAL':<10}\n")
                    for item in item_set:
                        cantidad = self.items.count(item)
                        subtotal = item.precio * cantidad
                        total_carrito += subtotal
                        f.write(f" {item.nombre:<11} |  ${item.precio:<14} | {cantidad:^8} |  ${subtotal:<10}\n")
                    f.write(f"                                      TOTAL = ${total_carrito}\n")      
                self.vaciar_carrito()  
                print(" ✅ Compra confirmada, se guardo en compra.txt")                        
            except FileNotFoundError:
                print(" ❌ Archivo no encontrado")
            except PermissionError:
                print(" ❌ No tienes permisos para escribir en el archivo")      
        else:
            print(" *** El carrito esta vacio ***")
        
#___________________________________________________________________________________________--

def menu_inicial():
    print("  ---------------------------------------  ")
    print("----       Bienvenido a 3D STORE        ----")
    print("  ----------------------------------------  ")
    print(" Selecciona el modo en que desea ingresar:  ")
    print("  (1) Modo Cliente                          ")
    print("  (2) Modo Admin                            ")
    print("  (3) Salir                               ")
    print("  ----------------------------------------  ")

catalogo = Catalogo()
cliente = Cliente("Cliente")
admin = Admin("Admin")  

catalogo.cargar_catalogo("catalogo.txt")

  
        
menu_inicial()
opcion = input("  ")
if opcion == "1": #cliente
    while True:
        cliente.menu_principal()
        opcion_cliente = input("  ")
        match opcion_cliente: 
            case "1":
                catalogo.ver_catalogo()
            case "2":
                cliente.buscar_producto()
            case "3":
                cliente.agregar_al_carrito()    
            case "4":
                cliente.carrito.ver_carrito()
            case "5":
                cliente.carrito.confirmar_carrito()
            case "6":
                cliente.carrito.vaciar_carrito()
                print(" ✅ --- El carrito se vacio ---")
            case "0": #salir
                print("  ----------------------------------------  ")
                print("----    Ten un buen dia, vuelve pronto  ----")
                print("  ----------------------------------------  ")
                break
            case _:
                print("❌ opcion no valida, solo numeros del 0 al 5")

elif opcion == "2": #admin
    while True:
        admin.menu_principal()
        opcion_admin = input(" ")
        match opcion_admin:
            case "1": #1. Listar productos del catálogo.
                catalogo.ver_catalogo()
            case "2": #2. Crear producto nuevo indicando al menos: id, nombre, categoría, precio.
                admin.crear_producto()
            case "3": #3. Actualizar producto (por ejemplo, cambiar nombre, precio o categoría).
                admin.actualizar_producto()
            case "4": #4. Eliminar producto del catálogo.
                admin.eliminar_producto()
            case "5": #5. Guardar catálogo en archivo (ej: catalogo.txt o catalogo.csv).
                catalogo.guardar_catalogo("catalogo.txt")
            case "0": #salir
                print("  ----------------------------------------  ")
                print("----    Ten un buen dia, vuelve pronto  ----")
                print("  ----------------------------------------  ")
                break
            case _:
                print("❌ opcion no valida, solo numeros del 0 al 5")

elif opcion == "3": #salir
    print("  ----------------------------------------  ")
    print("----    Ten un buen dia, vuelve pronto  ----")
    print("  ----------------------------------------  ")
else:
    print(" ❌ opcion no valida, solo numeros del 0 al 3") 

