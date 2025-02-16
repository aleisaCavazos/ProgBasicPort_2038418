#13.	Convertir una temperatura entre distintas escalas.
def convertir_temperatura(valor, escala_origen, escala_destino):
    # Convertimos la escala a minúsculas para evitar errores por mayúsculas
    escala_origen = escala_origen.lower()
    escala_destino = escala_destino.lower()

    # Convertimos de la escala origen a Celsius
    if escala_origen == 'celsius':
        celsius = valor
    elif escala_origen == 'fahrenheit':
        celsius = (valor - 32) * 5/9
    elif escala_origen == 'kelvin':
        celsius = valor - 273.15
    else:
        return "Escala de origen no válida. Usa 'Celsius', 'Fahrenheit' o 'Kelvin'."

    # Convertimos de Celsius a la escala destino
    if escala_destino == 'celsius':
        resultado = celsius
    elif escala_destino == 'fahrenheit':
        resultado = (celsius * 9/5) + 32
    elif escala_destino == 'kelvin':
        resultado = celsius + 273.15
    else:
        return "Escala de destino no válida. Usa 'Celsius', 'Fahrenheit' o 'Kelvin'."

    return round(resultado, 2)

# Solicitamos al usuario los datos
valor = float(input("Ingresa la temperatura: "))
escala_origen = input("Ingresa la escala de origen (Celsius, Fahrenheit, Kelvin): ")
escala_destino = input("Ingresa la escala de destino (Celsius, Fahrenheit, Kelvin): ")

resultado = convertir_temperatura(valor, escala_origen, escala_destino)
print(f"La temperatura convertida es: {resultado} {escala_destino.capitalize()}")
