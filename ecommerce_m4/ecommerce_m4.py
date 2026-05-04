"""
1) Propósito
    Re-estructurar el ecommerce de consola desarrollado en el Módulo 3 usando Programación
    Orientada a Objetos en Python, incorporando roles y utilizando:
    • Clases, atributos y métodos (colaboración y composición).
    • Herencia simple para diferenciar tipos de usuarios.
    • Manejo de excepciones para validar y controlar errores.
    • Lectura/escritura de archivos de texto para guardar información básica del sistema.
2) Descripción general de la app
    La aplicación será un Ecommerce por consola con dos roles:
    • ADMIN
    o Gestiona el catálogo de productos.
    • CLIENTE
    o Navega por el catálogo, agrega productos al carrito y confirma compras.
    Al iniciar, el programa pregunta si el usuario se identificará como ADMIN o CLIENTE y muestra el
    menú correspondiente.
3) Requisitos funcionales
    3.1. Rol ADMIN
        El ADMIN debe poder:
        1. Listar productos del catálogo.
        2. Crear producto nuevo indicando al menos: id, nombre, categoría, precio.
        3. Actualizar producto (por ejemplo, cambiar nombre, precio o categoría).
        4. Eliminar producto del catálogo.
        5. Guardar catálogo en archivo (ej: catalogo.txt o catalogo.csv).
        El catálogo inicial puede cargarse desde el código o, opcionalmente, leerse desde un archivo al inicio.
    3.2. Rol CLIENTE
        El CLIENTE debe poder:
        1. Ver catálogo de productos.
        2. Buscar productos por nombre o categoría.
        3. Agregar productos al carrito, indicando:
        o id del producto.
        o cantidad (entero > 0).
        4. Ver carrito y total:
        o Listar ítems (nombre, cantidad, precio unitario, subtotal).
        o Mostrar total a pagar.
        5. Confirmar compra:
        o Si el carrito está vacío, avisar y no permitir la compra.
        o Registrar la compra en un archivo de texto simple (ej: ordenes.txt) con fecha/hora,
        productos y total.
        o Vaciar el carrito tras confirmar.
    3.3. Manejo de errores (excepciones)
        • Deben manejarse casos como:
        o ID de producto inexistente.
        o Cantidad menor o igual a 0.
        o Archivos que no se pueden abrir/escribir.
        • Debe utilizarse al menos una excepción personalizada (por ejemplo,
        ProductoNoEncontradoError o CantidadInvalidaError) además de excepciones estándar

4) Requisitos técnicos
    La solución debe:
    1. Estar implementada en Python, ejecutable en consola.
    2. Incluir clases que reflejen la estructura del problema. Ejemplo (puedes adaptarlo):
        o Producto
        o Catalogo (contiene muchos Producto)
        o Carrito (contiene ítems de producto + cantidad)
        o Usuario (clase base)
        o Admin y Cliente (heredan de Usuario)
        o Aplicacion o Tienda (coordina la ejecución y menús)
    3. Aplicar:
        o Composición: por ejemplo, Carrito tiene una colección de productos.
        o Herencia: Admin y Cliente extienden a Usuario, con comportamientos distintos.
    4. Usar métodos claros para cada acción importante:
        o agregar/eliminar/actualizar producto,
        o agregar al carrito,
        o calcular total,
        o guardar/leer de archivo, etc.
    5. Usar excepciones con bloques try/except y, cuando corresponda, finally.
    6. Usar archivos de texto para:
        o Guardar catálogo (opcional pero recomendado).
        o Registrar compras (obligatorio).
    7. Mantener buena legibilidad:
        o Nombres en snake_case.
        o Identación correcta.
        o Comentarios breves donde sea necesario.
    No se debe usar bases de datos, librerías externas, frameworks web ni temas que no se hayan pasado
    en el módulo.
5) Entregables
    • Código fuente (por ejemplo):
    o main.py
    o Otros archivos .py si se separa en módulos (opcional, pero recomendable).
    • (Opcional) Un archivo README.md o .txt con:
    o Descripción breve de la app.
    o Cómo ejecutar el programa.

"""
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
        print("(5) Vaciar carrito."                         ) 
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
                        print(f" --- Se agrego {a} unidades de {producto.nombre} al carrito | ${a * producto.precio}")
                        estado = True
            elif tipo_busqueda == "id":
                if nombre_busqueda.isdigit():
                    if int(nombre_busqueda) == producto.id: #busca por id      
                        cantidad = (self.cantidad_produto() + 1)
                        if cantidad > 0:
                            for a in range(1,cantidad):
                                self.carrito.agregar_item(producto) #agrega los productos encontrados a resultados
                            print("")
                            print(f" --- Se agrego {a} unidades de {producto.nombre} al carrito | ${a * producto.precio}")
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
            print("Producto no encontrado") 

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
        print(" --- El carrito se vacio ---")

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
                cliente.carrito.vaciar_carrito()
            case "0":
                break
            case _:
                print("❌ opcion no valida, solo numeros del 0 al 5")

elif opcion == "2": #admin
    pass
elif opcion == "3": #salir
    print("  ----------------------------------------  ")
    print("----    Ten un buen dia, vuelve pronto  ----")
    print("  ----------------------------------------  ")
else:
    print(" ❌ opcion no valida, solo numeros del 0 al 3") 

