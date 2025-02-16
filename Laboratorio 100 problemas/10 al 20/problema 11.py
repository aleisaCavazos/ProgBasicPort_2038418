#11.	Verificar si una cadena es un palındromo.
def es_palindroma(frase):
    #Eliminar espacios y tener todas las letras en minisculas
    frase = frase.replace(" ", "").lower()
    
    # Comparamos la frase con su reverso
    return frase == frase[::-1]

# Ejemplo de uso
palabra = input("Ingresa una palabra o frase: ")
if es_palindroma(palabra):
    print(f'"{palabra}" es una palabra/frase palíndroma.')
else:
    print(f'"{palabra}" NO es una palabra/frase palíndroma.')
