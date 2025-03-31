# EJRCICIO 3
# Lista para almacenar los contactos
agenda_contactos = []

# Función para agregar un nuevo contacto
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono del contacto: ")
    correo = input("Ingrese el correo electrónico del contacto: ")
    
    # Crear una tupla con los datos del contacto
    contacto = (nombre, numero, correo)
    
    # Agregar el contacto a la lista
    agenda_contactos.append(contacto)
    print(f"Contacto '{nombre}' agregado exitosamente.")

# Función para buscar un contacto por nombre
def buscar_contacto():
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
    
    encontrado = False
    for contacto in agenda_contactos:
        if contacto[0].lower() == nombre_buscar.lower():
            print(f"Nombre: {contacto[0]}")
            print(f"Número: {contacto[1]}")
            print(f"Correo: {contacto[2]}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"Contacto con el nombre '{nombre_buscar}' no encontrado.")

# Función para listar todos los contactos en orden alfabético
def listar_contactos():
    # Ordenar la lista de contactos por nombre (primer elemento de la tupla)
    agenda_contactos_ordenada = sorted(agenda_contactos, key=lambda contacto: contacto[0].lower())
    
    print("Lista de contactos (ordenados alfabéticamente):")
    for contacto in agenda_contactos_ordenada:
        print(f"Nombre: {contacto[0]} | Número: {contacto[1]} | Correo: {contacto[2]}")

# Función principal para interactuar con el usuario
def menu():
    while True:
        print("\nMenu de opciones:")
        print("1. Agregar nuevo contacto")
        print("2. Buscar contacto por nombre")
        print("3. Listar todos los contactos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            listar_contactos()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()
