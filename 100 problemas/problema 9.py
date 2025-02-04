#9.	Generar una lista de numeros pares e impares hasta un lımite dado.
def generar_pares_impares(limite):
    pares = []  # Lista para los números pares
    impares = []  # Lista para los números impares

    for num in range(1, limite + 1):
        if num % 2 == 0:
            pares.append(num)  # Agrega a la lista de pares
        else:
            impares.append(num)  # Agrega a la lista de impares

    return pares, impares

# Solicitar el límite al usuario
limite = int(input("Ingrese el límite hasta el cual generar los números: "))

# Generar y mostrar las listas
pares, impares = generar_pares_impares(limite)

print(f"Números pares hasta {limite}: {pares}")
print(f"Números impares hasta {limite}: {impares}")
