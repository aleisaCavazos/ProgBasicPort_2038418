#Leer, escribir y modificar un archivo de texto
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Escribir en el archivo")
    print("2. Leer el archivo")
    print("3. Modificar el archivo")
    print("4. Salir")
 
def escribir_archivo(nombre_archivo):
    texto = input("Escribe el texto que deseas agregar: ")
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)
    print("Texto escrito correctamente.")
 
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print("\nContenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo no existe. Prueba escribiendo algo primero.")
 
def modificar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        print(f"\nContenido actual:\n{contenido}")
 
        texto = input("Escribe el texto que deseas agregar: ")
        with open(nombre_archivo, 'a') as archivo:
            archivo.write('\n' + texto)
        print("Texto agregado correctamente.")
    except FileNotFoundError:
        print("El archivo no existe. Prueba escribiendo algo primero.")
 
def main():
    nombre_archivo = "archivo.txt"
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")
 
        if opcion == '1':
            escribir_archivo(nombre_archivo)
        elif opcion == '2':
            leer_archivo(nombre_archivo)
        elif opcion == '3':
            modificar_archivo(nombre_archivo)
        elif opcion == '4':
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
 
if __name__ == "__main__":
    main()