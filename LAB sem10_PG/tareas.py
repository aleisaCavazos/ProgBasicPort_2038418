# Función para agregar una tarea
def agregar_tarea(lista, tarea):
    lista.append(tarea)
    print(f"Tarea '{tarea}' agregada a la lista.")

# Función para eliminar una tarea
def eliminar_tarea(lista, tarea):
    if tarea in lista:
        lista.remove(tarea)
        print(f"Tarea '{tarea}' eliminada de la lista.")
    else:
        print(f"Tarea '{tarea}' no encontrada.")

# Función para mostrar las tareas
def mostrar_tareas(lista):
    if lista:
        print("\nLista de tareas:")
        for tarea in lista:
            print(f"- {tarea}")
    else:
        print("No hay tareas en la lista.")
