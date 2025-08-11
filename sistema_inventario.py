"""
Sistema de Inventario con Programación Orientada a Objetos
Desarrollado para gestionar productos y realizar operaciones de inventario.
"""


class Producto:
    """
    Clase que representa un producto en el inventario.
    
    Atributos:
        nombre (str): Nombre del producto
        precio (float): Precio unitario del producto
        cantidad (int): Cantidad disponible en inventario
    """
    
    def __init__(self, nombre, precio, cantidad):
        """
        Constructor de la clase Producto.
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio unitario del producto
            cantidad (int): Cantidad disponible
            
        Raises:
            ValueError: Si los datos no cumplen las validaciones
        """
        # Validación del nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío")
        
        # Validación del precio
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número positivo o cero")
        
        # Validación de la cantidad
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero positivo o cero")
        
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = cantidad
    
    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto.
        
        Args:
            nuevo_precio (float): Nuevo precio del producto
            
        Raises:
            ValueError: Si el precio no es válido
        """
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número positivo o cero")
        
        self.precio = float(nuevo_precio)
        print(f"Precio actualizado correctamente a ${self.precio:.2f}")
    
    def actualizar_cantidad(self, nueva_cantidad):
        """
        Actualiza la cantidad del producto.
        
        Args:
            nueva_cantidad (int): Nueva cantidad del producto
            
        Raises:
            ValueError: Si la cantidad no es válida
        """
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero positivo o cero")
        
        self.cantidad = nueva_cantidad
        print(f"Cantidad actualizada correctamente a {self.cantidad} unidades")
    
    def calcular_valor_total(self):
        """
        Calcula el valor total del producto (precio × cantidad).
        
        Returns:
            float: Valor total del producto
        """
        return self.precio * self.cantidad
    
    def __str__(self):
        """
        Representación en cadena del producto.
        
        Returns:
            str: Información formateada del producto
        """
        valor_total = self.calcular_valor_total()
        return (f"Producto: {self.nombre}\n"
                f"  Precio: ${self.precio:.2f}\n"
                f"  Cantidad: {self.cantidad} unidades\n"
                f"  Valor Total: ${valor_total:.2f}")


class Inventario:
    """
    Clase que gestiona una colección de productos.
    
    Atributos:
        productos (list): Lista de productos en el inventario
    """
    
    def __init__(self):
        """Constructor de la clase Inventario."""
        self.productos = []
    
    def agregar_producto(self, producto):
        """
        Añade un producto al inventario.
        
        Args:
            producto (Producto): Objeto de tipo Producto a añadir
            
        Raises:
            TypeError: Si el objeto no es de tipo Producto
        """
        if not isinstance(producto, Producto):
            raise TypeError("El objeto debe ser de tipo Producto")
        
        # Verificar si ya existe un producto con el mismo nombre
        producto_existente = self.buscar_producto(producto.nombre)
        if producto_existente:
            respuesta = input(f"Ya existe un producto llamado '{producto.nombre}'. "
                            "¿Desea actualizar la cantidad? (s/n): ").lower().strip()
            if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                nueva_cantidad = producto_existente.cantidad + producto.cantidad
                producto_existente.actualizar_cantidad(nueva_cantidad)
                print(f"Cantidad actualizada. Total: {nueva_cantidad} unidades")
            else:
                print("Producto no agregado.")
        else:
            self.productos.append(producto)
            print(f"Producto '{producto.nombre}' agregado exitosamente al inventario.")
    
    def buscar_producto(self, nombre):
        """
        Busca un producto por su nombre.
        
        Args:
            nombre (str): Nombre del producto a buscar
            
        Returns:
            Producto or None: El producto encontrado o None si no existe
        """
        nombre = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre:
                return producto
        return None
    
    def calcular_valor_inventario(self):
        """
        Calcula el valor total de todos los productos en el inventario.
        
        Returns:
            float: Valor total del inventario
        """
        return sum(producto.calcular_valor_total() for producto in self.productos)
    
    def listar_productos(self):
        """
        Muestra todos los productos del inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
            return
        
        print(f"\n{'='*50}")
        print("LISTADO DE PRODUCTOS EN INVENTARIO")
        print(f"{'='*50}")
        
        for i, producto in enumerate(self.productos, 1):
            print(f"\n{i}. {producto}")
            print("-" * 40)
        
        valor_total = self.calcular_valor_inventario()
        print(f"\nVALOR TOTAL DEL INVENTARIO: ${valor_total:.2f}")
        print(f"TOTAL DE PRODUCTOS: {len(self.productos)}")


def solicitar_datos_producto():
    """
    Solicita al usuario los datos para crear un nuevo producto.
    
    Returns:
        Producto: Nuevo producto creado con los datos ingresados
        
    Raises:
        ValueError: Si los datos ingresados no son válidos
    """
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    
    # Solicitar nombre
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío. Intente nuevamente.")
    
    # Solicitar precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: $"))
            if precio >= 0:
                break
            else:
                print("El precio debe ser positivo o cero.")
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")
    
    # Solicitar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en inventario: "))
            if cantidad >= 0:
                break
            else:
                print("La cantidad debe ser positiva o cero.")
        except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad.")
    
    return Producto(nombre, precio, cantidad)


def menu_principal():
    """
    Función principal que muestra el menú y procesa las opciones del usuario.
    """
    inventario = Inventario()
    
    while True:
        print(f"\n{'='*50}")
        print("SISTEMA DE GESTIÓN DE INVENTARIO")
        print(f"{'='*50}")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar todos los productos")
        print("4. Calcular valor total del inventario")
        print("5. Actualizar precio de producto")
        print("6. Actualizar cantidad de producto")
        print("7. Salir")
        print("-" * 50)
        
        try:
            opcion = input("Seleccione una opción (1-7): ").strip()
            
            if opcion == "1":
                # Agregar producto
                try:
                    producto = solicitar_datos_producto()
                    inventario.agregar_producto(producto)
                except ValueError as e:
                    print(f"Error al crear el producto: {e}")
                except Exception as e:
                    print(f"Error inesperado: {e}")
            
            elif opcion == "2":
                # Buscar producto
                nombre = input("Ingrese el nombre del producto a buscar: ").strip()
                if nombre:
                    producto = inventario.buscar_producto(nombre)
                    if producto:
                        print(f"\n✅ PRODUCTO ENCONTRADO:")
                        print("-" * 30)
                        print(producto)
                    else:
                        print(f"❌ No se encontró ningún producto con el nombre '{nombre}'")
                else:
                    print("Debe ingresar un nombre para buscar.")
            
            elif opcion == "3":
                # Listar productos
                inventario.listar_productos()
            
            elif opcion == "4":
                # Calcular valor total
                valor_total = inventario.calcular_valor_inventario()
                print(f"\n💰 VALOR TOTAL DEL INVENTARIO: ${valor_total:.2f}")
                if inventario.productos:
                    print(f"📦 TOTAL DE PRODUCTOS: {len(inventario.productos)}")
                else:
                    print("📦 El inventario está vacío")
            
            elif opcion == "5":
                # Actualizar precio
                nombre = input("Ingrese el nombre del producto: ").strip()
                if nombre:
                    producto = inventario.buscar_producto(nombre)
                    if producto:
                        try:
                            nuevo_precio = float(input(f"Precio actual: ${producto.precio:.2f}\n"
                                                     "Ingrese el nuevo precio: $"))
                            producto.actualizar_precio(nuevo_precio)
                        except ValueError as e:
                            print(f"Error: {e}")
                    else:
                        print(f"No se encontró el producto '{nombre}'")
                else:
                    print("Debe ingresar un nombre.")
            
            elif opcion == "6":
                # Actualizar cantidad
                nombre = input("Ingrese el nombre del producto: ").strip()
                if nombre:
                    producto = inventario.buscar_producto(nombre)
                    if producto:
                        try:
                            nueva_cantidad = int(input(f"Cantidad actual: {producto.cantidad} unidades\n"
                                                     "Ingrese la nueva cantidad: "))
                            producto.actualizar_cantidad(nueva_cantidad)
                        except ValueError as e:
                            print(f"Error: {e}")
                    else:
                        print(f"No se encontró el producto '{nombre}'")
                else:
                    print("Debe ingresar un nombre.")
            
            elif opcion == "7":
                # Salir
                print("\n¡Gracias por usar el Sistema de Gestión de Inventario!")
                print("¡Hasta luego! 👋")
                break
            
            else:
                print("❌ Opción no válida. Por favor, seleccione una opción del 1 al 7.")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario.")
            print("¡Hasta luego! 👋")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            print("Por favor, intente nuevamente.")


if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    Instancia el inventario y ejecuta el menú principal.
    """
    try:
        menu_principal()
    except Exception as e:
        print(f"Error crítico en el programa: {e}")
        print("El programa se cerrará.")