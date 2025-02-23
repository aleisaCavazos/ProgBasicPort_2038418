#30. Implementar funciones recursivas.	
# Función recursiva para calcular el factorial
def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Función principal para interactuar con el usuario
def menu():
    print("¡Bienvenido al cálculo de Factorial!")
    numero = int(input("Ingrese un número para calcular su factorial: "))
    
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        resultado = factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")

# Ejecutar el menú
menu()
