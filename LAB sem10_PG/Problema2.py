# EJERCICIO 2
# Diccionario para almacenar el inventario
inventario = {}

# Función para agregar un producto
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    # Guardamos el producto en el inventario
    inventario[nombre] = {"categoria": categoria, "precio": precio, "cantidad": cantidad}
    print(f"Producto '{nombre}' agregado exitosamente.")

# Función para eliminar un producto
def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado exitosamente.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

# Función para buscar un producto por su nombre
def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    
    if nombre in inventario:
        producto = inventario[nombre]
        print(f"Producto encontrado: {nombre}")
        print(f"Categoría: {producto['categoria']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

# Función para mostrar todos los productos ordenados por precio
def mostrar_productos_ordenados():
    productos_ordenados = sorted(inventario.items(), key=lambda x: x[1]['precio'])
    
    print("Productos ordenados por precio:")
    for nombre, producto in productos_ordenados:
        print(f"Nombre: {nombre} | Categoría: {producto['categoria']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

# Función principal para interactuar con el usuario
def menu():
    while True:
        print("\nMenu de opciones:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto por nombre")
        print("4. Mostrar todos los productos ordenados por precio")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            mostrar_productos_ordenados()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()
