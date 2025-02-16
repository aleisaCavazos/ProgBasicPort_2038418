#5.	Verificar si un nu´mero es primo.
def es_primo(num):
    if num < 2:
        return False  # Los números menores a 2 no son primos

    for i in range(2, int(num ** 0.5) + 1):  # Solo revisamos hasta la raíz cuadrada de num
        if num % i == 0:
            return False  # Si es divisible por otro número, no es primo
    
    return True  # Si no encontró divisores, es primo

num = int(input("Ingrese un número: "))

if es_primo(num):
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")
