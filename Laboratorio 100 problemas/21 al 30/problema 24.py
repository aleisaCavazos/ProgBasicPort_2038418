# 24. Calcular la suma de una serie numerica.
def suma_serie():
    print("\nTipo de serie disponible:")
    print("1. Aritmética")
    print("2. Geométrica")

    opcion = int(input("\nElige el tipo de serie (1 o 2): "))

    if opcion == 1:
        inicio = int(input("Ingresa el primer término: "))
        razon = int(input("Ingresa la razón: "))
        n = int(input("Ingresa el número de términos: "))
        suma = n * (2 * inicio + (n - 1) * razon) // 2
        print(f"La suma de la serie aritmética es: {suma}")

    elif opcion == 2:
        inicio = int(input("Ingresa el primer término: "))
        razon = float(input("Ingresa la razón: "))
        n = int(input("Ingresa el número de términos: "))
        if razon == 1:
            suma = inicio * n
        else:
            suma = inicio * (1 - razon**n) / (1 - razon)
        print(f"La suma de la serie geométrica es: {suma:.2f}")

    else:
        print("Opción no válida. Intenta de nuevo.")

suma_serie()
