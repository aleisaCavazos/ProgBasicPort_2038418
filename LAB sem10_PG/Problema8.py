#EJERCICIO 8
# Función para fusionar dos sublistas ordenadas
def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    
    # Comparar los elementos de ambas listas y fusionarlos
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Si quedan elementos en la lista izquierda, agregarlos
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1
    
    # Si quedan elementos en la lista derecha, agregarlos
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1
    
    return resultado

# Función para implementar el algoritmo Mergesort
def mergesort(lista):
    if len(lista) <= 1:
        return lista
    # Dividir la lista en dos mitades
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    
    # Ordenar ambas mitades de manera recursiva y fusionarlas
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)
    
    return merge(izquierda, derecha)

# Función principal
def main():
    # Ingresar la lista de números
    lista = list(map(int, input("Ingrese una lista de números separados por espacio: ").split()))
    
    # Mostrar la lista antes del ordenamiento
    print("\nLista original:")
    print(lista)
    
    # Ordenar la lista utilizando Mergesort
    lista_ordenada = mergesort(lista)
    
    # Mostrar la lista después del ordenamiento
    print("\nLista ordenada con Mergesort:")
    print(lista_ordenada)

# Ejecutar el programa
if __name__ == "__main__":
    main()
