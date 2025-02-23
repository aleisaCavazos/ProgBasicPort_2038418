# 21.Calcular el área y volumen de distintas figuras geométricas.
import math

def calcular_area_volumen():
    print("\nFiguras disponibles:")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Esfera")
    print("4. Cubo")

    opcion = int(input("\nElige una figura (1-4): "))

    if opcion == 1:
        radio = float(input("Ingresa el radio del círculo: "))
        area = math.pi * radio**2
        print(f"Área del círculo: {area:.2f}")

    elif opcion == 2:
        lado = float(input("Ingresa el lado del cuadrado: "))
        area = lado**2
        print(f"Área del cuadrado: {area:.2f}")

    elif opcion == 3:
        radio = float(input("Ingresa el radio de la esfera: "))
        area = 4 * math.pi * radio**2
        volumen = (4/3) * math.pi * radio**3
        print(f"Área de la esfera: {area:.2f}")
        print(f"Volumen de la esfera: {volumen:.2f}")

    elif opcion == 4:
        lado = float(input("Ingresa el lado del cubo: "))
        area = 6 * lado**2
        volumen = lado**3
        print(f"Área del cubo: {area:.2f}")
        print(f"Volumen del cubo: {volumen:.2f}")

    else:
        print("Opción no válida. Intenta de nuevo.")

calcular_area_volumen()
