#7.	Determinar si un numero es par, impar o multiplo de otro.
def verificar_numero(num, multiplo_de=None):
    if num % 2 == 0:
        print(f"{num} es un número **par**.")
    else:
        print(f"{num} es un número **impar**.")

    if multiplo_de is not None:
        if num % multiplo_de == 0:
            print(f"{num} es **múltiplo de {multiplo_de}**.")
        else:
            print(f"{num} **no** es múltiplo de {multiplo_de}.")

# Solicitar datos al usuario
num = int(input("Ingrese un número: "))

# Preguntar si quiere verificar múltiplo de otro número
opcion = input("¿Quiere verificar si es múltiplo de otro número? (s/n): ").lower()

if opcion == 's':
    multiplo_de = int(input("Ingrese el número para verificar múltiplo: "))
    verificar_numero(num, multiplo_de)
else:
    verificar_numero(num)