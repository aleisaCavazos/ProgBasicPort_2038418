#20. Implementar busqueda binaria y lineal.
def busqueda_lineal(lista, objetivo):
    """Busca un elemento en la lista de forma lineal."""
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return f"Elemento encontrado en la posición {i}"
    return "Elemento no encontrado"


def busqueda_binaria(lista, objetivo):
    """Busca un elemento en la lista usando el método binario."""
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return f"Elemento encontrado en la posición {medio}"
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return "Elemento no encontrado"


# Ejemplo de uso
lista = [2, 4, 5, 7, 9, 11, 15, 18, 21]
print("Lista:", lista)

# Buscar con búsqueda lineal
objetivo = int(input("Ingresa el número a buscar: "))
resultado_lineal = busqueda_lineal(lista, objetivo)
print("Búsqueda Lineal:", resultado_lineal)

# Buscar con búsqueda binaria (lista debe estar ordenada)
resultado_binaria = busqueda_binaria(lista, objetivo)
print("Búsqueda Binaria:", resultado_binaria)
