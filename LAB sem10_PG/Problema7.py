# EJERCICIO 7
import random

# Función de Quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivot]
    derecha = [x for x in lista if x > pivot]
    return quicksort(izquierda) + [pivot] + quicksort(derecha)

# Función de búsqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  # Encontrado, devolver el índice
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # No encontrado

# Generar lista de números aleatorios
def generar_lista(tamano, rango_min, rango_max):
    return [random.randint(rango_min, rango_max) for _ in range(tamano)]

# Función principal
def main():
    tamano_lista = int(input("Ingrese el tamaño de la lista: "))
    rango_min = int(input("Ingrese el valor mínimo del rango: "))
    rango_max = int(input("Ingrese el valor máximo del rango: "))

    # Generar lista de números aleatorios
    lista = generar_lista(tamano_lista, rango_min, rango_max)
    
    print("\nLista original:")
    print(lista)
    
    # Ordenar la lista con Quicksort
    lista_ordenada = quicksort(lista)
    print("\nLista ordenada:")
    print(lista_ordenada)
    
    # Buscar un número en la lista ordenada usando búsqueda binaria
    objetivo = int(input("\nIngrese el número a buscar: "))
    indice = busqueda_binaria(lista_ordenada, objetivo)
    
    if indice != -1:
        print(f"\nEl número {objetivo} se encuentra en la posición {indice} de la lista ordenada.")
    else:
        print(f"\nEl número {objetivo} no se encuentra en la lista.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
