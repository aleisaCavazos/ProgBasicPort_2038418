# 23. Implementar y operar con matrices.	(Dificultad: 6)
import numpy as np

def operar_matrices():
    filas = int(input("Ingresa el número de filas: "))
    columnas = int(input("Ingresa el número de columnas: "))

    print("\nIngresa los elementos de la primera matriz:")
    matriz1 = np.array([[int(input(f"Elemento [{i+1}][{j+1}]: ")) for j in range(columnas)] for i in range(filas)])

    print("\nIngresa los elementos de la segunda matriz:")
    matriz2 = np.array([[int(input(f"Elemento [{i+1}][{j+1}]: ")) for j in range(columnas)] for i in range(filas)])

    print("\nMatriz 1:")
    print(matriz1)

    print("\nMatriz 2:")
    print(matriz2)

    print("\nSuma de matrices:")
    print(matriz1 + matriz2)

    print("\nMultiplicación de matrices elemento por elemento:")
    print(matriz1 * matriz2)

operar_matrices()
