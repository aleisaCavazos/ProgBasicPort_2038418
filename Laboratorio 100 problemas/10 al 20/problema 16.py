#16.	Contar el nu´mero de vocales y consonantes en una cadena.
def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    num_vocales = 0
    num_consonantes = 0
    
    for letra in cadena:
        if letra in vocales:
            num_vocales += 1
        elif letra in consonantes:
            num_consonantes += 1
    
    return num_vocales, num_consonantes

# Ejemplo de uso
cadena = input("Ingresa una cadena: ")
vocales, consonantes = contar_vocales_consonantes(cadena)

print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
