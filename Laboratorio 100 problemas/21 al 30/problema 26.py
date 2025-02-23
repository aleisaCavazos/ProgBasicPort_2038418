# 26. Implementar una agenda de contactos 
# Definir la clase Agenda
class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono, correo):
        if nombre not in self.contactos:
            self.contactos[nombre] = {'telefono': telefono, 'correo': correo}
            print(f"Contacto {nombre} agregado.")
        else:
            print(f"El contacto {nombre} ya existe.")

    def ver_contactos(self):
        if self.contactos:
            print("\nLista de contactos:")
            for nombre, info in self.contactos.items():
                print(f"Nombre: {nombre} - Teléfono: {info['telefono']} - Correo: {info['correo']}")
        else:
            print("No hay contactos registrados.")

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            info = self.contactos[nombre]
            print(f"Contacto encontrado: {nombre} - Teléfono: {info['telefono']} - Correo: {info['correo']}")
        else:
            print(f"No se encontró el contacto con el nombre: {nombre}")

    def actualizar_contacto(self, nombre, telefono=None, correo=None):
        if nombre in self.contactos:
            if telefono:
                self.contactos[nombre]['telefono'] = telefono
            if correo:
                self.contactos[nombre]['correo'] = correo
            print(f"Contacto {nombre} actualizado.")
        else:
            print(f"No se encontró el contacto {nombre}.")

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto {nombre} eliminado.")
        else:
            print(f"No se encontró el contacto {nombre}.")

# Crear una instancia de la agenda
agenda = Agenda()

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú de Agenda ---")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Buscar contacto")
        print("4. Actualizar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono: ")
            correo = input("Ingrese el correo electrónico: ")
            agenda.agregar_contacto(nombre, telefono, correo)
        
        elif opcion == "2":
            agenda.ver_contactos()
        
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto que desea buscar: ")
            agenda.buscar_contacto(nombre)
        
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
            telefono = input("Nuevo teléfono (deje en blanco si no desea cambiarlo): ")
            correo = input("Nuevo correo (deje en blanco si no desea cambiarlo): ")
            agenda.actualizar_contacto(nombre, telefono if telefono else None, correo if correo else None)
        
        elif opcion == "5":
            nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
            agenda.eliminar_contacto(nombre)
        
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()
