#2.	Crear una calculadora simple que realice operaciones basicas.

while True:
    print("\nSeleccionar qué desea hacer")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    try:
        opcion = int(input("Ingrese la opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue  # Vuelve a pedir una opción

    if opcion == 5:
        print("Saliendo del programa...")
        break  # Termina el programa

    if opcion in [1, 2, 3, 4]:  # Solo pide números si la opción es válida
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Por favor, ingrese números válidos.")
            continue  # Vuelve a pedir opción

        if opcion == 1:
            print("La suma es:", num1 + num2)
        elif opcion == 2:
            print("La resta es:", num1 - num2)
        elif opcion == 3:
            print("La multiplicación es:", num1 * num2)
        elif opcion == 4:
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                print("La división es:", num1 / num2)
    else:
        print("Opción inválida, intente de nuevo.")
