#14.	Implementar distintos metodos de ordenamiento.
def ordenamiento_burbuja(Lista):
    n = len(Lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if Lista[j] > Lista[j + 1]:
                Lista[j], Lista[j + 1] = Lista[j + 1], Lista[j]
    return Lista

def ordenamiento_insercion(Lista):
    for i in range(1, len(Lista)):
        actual = Lista[i]
        j = i - 1
        while j >= 0 and actual < Lista[j]:
            Lista[j + 1] = Lista[j]
            j -= 1
        Lista[j + 1] = actual
    return Lista

def ordenamiento_seleccion(Lista):
    n = len(Lista)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if Lista[j] < Lista[minimo]:
                minimo = j
        Lista[i], Lista[minimo] = Lista[minimo], Lista[i]
    return Lista

def main():
    Lista = [64, 34, 25, 12, 22, 11, 90]
    print(f"Lista original: {Lista}")
    print(f"Lista ordenada con burbuja: {ordenamiento_burbuja(Lista[:])}")
    print(f"Lista ordenada con insercion: {ordenamiento_insercion(Lista[:])}")
    print(f"Lista ordenada con seleccion: {ordenamiento_seleccion(Lista[:])}")

if __name__ == "__main__":
    main()

