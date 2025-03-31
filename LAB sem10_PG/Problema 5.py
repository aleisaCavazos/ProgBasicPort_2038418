# EJERCICIO 5

import conversor  # Importa el módulo conversor.py

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Convertir kilómetros a millas")
        print("2. Convertir Celsius a Fahrenheit")
        print("3. Convertir litros a galones")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            km = float(input("Ingrese la cantidad en kilómetros: "))
            millas = conversor.km_a_millas(km)
            print(f"{km} kilómetros son {millas} millas.")
        
        elif opcion == "2":
            celsius = float(input("Ingrese la temperatura en Celsius: "))
            fahrenheit = conversor.celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C son {fahrenheit}°F.")
        
        elif opcion == "3":
            litros = float(input("Ingrese la cantidad en litros: "))
            galones = conversor.litros_a_galones(litros)
            print(f"{litros} litros son {galones} galones.")
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()
