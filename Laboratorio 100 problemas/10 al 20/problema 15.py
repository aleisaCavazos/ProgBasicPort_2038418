#15.	Determinar si un año es bisiesto.
def es_bisiesto(año):
    # Un año es bisiesto si es divisible por 4
    # pero no por 100, excepto si también es divisible por 400.
    if (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):
        return True
    return False

# Solicitamos el año al usuario
try:
    año = int(input("Ingresa un año para verificar si es bisiesto: "))
    if es_bisiesto(año):
        print(f"{año} es un año bisiesto.")
    else:
        print(f"{año} no es un año bisiesto.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")

# Casos de prueba adicionales
test_years = [1600, 1700, 2000, 2024, 2100]
for year in test_years:
    print(f"{year}: {'Bisiesto' if es_bisiesto(year) else 'No bisiesto'}")
