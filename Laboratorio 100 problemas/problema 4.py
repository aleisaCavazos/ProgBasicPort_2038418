#4.	Generar la secuencia de Fibonacci hasta un numero dado de terminos.

num = int(input("Ingrese el número de términos: "))

if num <= 0:
    print("Ingrese un número mayor que 0.")
else:
    fibonacci = [0, 1]  # Inicializamos los primeros dos términos
    for i in range(2, num):
        siguiente = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(siguiente)
    
    print(f"Secuencia de Fibonacci con {num} términos: {fibonacci[:num]}")
