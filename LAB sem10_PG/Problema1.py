#EJERCICIO 1 
# Función para analizar el texto
def analizar_texto(texto):
    # Paso 1: Convertir todo el texto a minúsculas y dividirlo en palabras
    palabras = texto.lower().split()

    # Paso 2: Usar un conjunto para obtener las palabras únicas
    palabras_unicas = set(palabras)

    # Paso 3: Usar un diccionario para contar la frecuencia de cada palabra
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    # Paso 4: Encontrar la palabra más frecuente
    palabra_mas_frecuente = max(frecuencia, key=frecuencia.get)
    frecuencia_palabra_mas_frecuente = frecuencia[palabra_mas_frecuente]

    # Paso 5: Mostrar los resultados
    print(f"Número total de palabras: {len(palabras)}")
    print(f"Cantidad de palabras únicas: {len(palabras_unicas)}")
    print("Frecuencia de cada palabra:")
    for palabra, conteo in frecuencia.items():
        print(f"'{palabra}': {conteo}")
    print(f"La palabra más frecuente es '{palabra_mas_frecuente}' con {frecuencia_palabra_mas_frecuente} apariciones.")

# Solicitar al usuario que ingrese un texto
texto_usuario = input("Ingresa un texto: ")

# Analizar el texto
analizar_texto(texto_usuario)
