# EJERCICIO 9

import tareas 

# Paradigma Imperativo
def menu():
    lista_de_tareas = []  # Lista vacía de tareas

    while True:
        print("\nMenú de tareas:")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        # Estructura de control Imperativa
        if opcion == "1":
            tarea = input("Ingrese la tarea que desea agregar: ")
            tareas.agregar_tarea(lista_de_tareas, tarea)  # Llamada a función estructurada
        elif opcion == "2":
            tarea = input("Ingrese la tarea que desea eliminar: ")
            tareas.eliminar_tarea(lista_de_tareas, tarea)  # Llamada a función estructurada
        elif opcion == "3":
            tareas.mostrar_tareas(lista_de_tareas)  # Llamada a función estructurada
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Paradigma Orientado a Objetos (OO)
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

class ListaDeTareas:
    def __init__(self):
        self.lista = []

    def agregar(self, tarea):
        self.lista.append(tarea)

    def eliminar(self, tarea):
        if tarea in self.lista:
            self.lista.remove(tarea)

    def mostrar(self):
        if self.lista:
            print("\nLista de tareas:")
            for tarea in self.lista:
                print(f"- {tarea}")
        else:
            print("No hay tareas en la lista.")

# Ejemplo de uso de la programación orientada a objetos
def ejemplo_objetos():
    lista_tareas_objetos = ListaDeTareas()

    tarea1 = Tarea("Estudiar matemáticas")
    tarea2 = Tarea("Hacer ejercicio")
    tarea3 = Tarea("Comprar víveres")

    lista_tareas_objetos.agregar(tarea1)
    lista_tareas_objetos.agregar(tarea2)
    lista_tareas_objetos.agregar(tarea3)

    lista_tareas_objetos.mostrar()

    lista_tareas_objetos.eliminar(tarea2)
    print("\nDespués de eliminar una tarea:")
    lista_tareas_objetos.mostrar()

# Llamar a la función que implementa el paradigma estructurado
menu()

# Llamar al ejemplo del paradigma orientado a objetos
ejemplo_objetos()
