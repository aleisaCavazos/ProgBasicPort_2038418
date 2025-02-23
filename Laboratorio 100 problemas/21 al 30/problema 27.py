# 27. Crear un conversor de unidades.
# Función para convertir unidades de longitud
def convertir_unidad(valor, unidad_origen, unidad_destino):
    # Diccionario de conversiones
    conversiones = {
        'metros': {'kilometros': 0.001, 'millimetros': 1000, 'centimetros': 100, 'millas': 0.000621371},
        'kilometros': {'metros': 1000, 'millimetros': 1000000, 'centimetros': 100000, 'millas': 0.621371},
        'millimetros': {'metros': 0.001, 'kilometros': 0.000001, 'centimetros': 0.1, 'millas': 6.2137e-7},
        'centimetros': {'metros': 0.01, 'kilometros': 0.00001, 'millimetros': 10, 'millas': 6.2137e-6},
        'millas': {'metros': 1609.34, 'kilometros': 1.60934, 'millimetros': 1609340, 'centimetros': 160934},
    }
    
    # Verificar si las unidades están en el diccionario
    if unidad_origen in conversiones and unidad_destino in conversiones[unidad_origen]:
        # Realizar la conversión
        factor_conversion = conversiones[unidad_origen][unidad_destino]
        resultado = valor * factor_conversion
        return resultado
    else:
        return "Conversión no soportada entre estas unidades."

# Menú interactivo para el conversor
def menu():
    print("Bienvenido al Conversor de Unidades de Longitud.")
    valor = float(input("Ingrese el valor que desea convertir: "))
    
    print("\nUnidades disponibles: metros, kilometros, millimetros, centimetros, millas.")
    
    unidad_origen = input("Ingrese la unidad de origen: ").lower()
    unidad_destino = input("Ingrese la unidad de destino: ").lower()
    
    resultado = convertir_unidad(valor, unidad_origen, unidad_destino)
    
    if isinstance(resultado, float):
        print(f"{valor} {unidad_origen} es igual a {resultado} {unidad_destino}.")
    else:
        print(resultado)

# Ejecutar el menú
menu()
