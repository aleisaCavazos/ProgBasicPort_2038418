#6.	Calcular el interes compuesto dado un capital, tasa y tiempo.
def interes_compuesto(P, r, n, t):
    A = P * (1 + r / n) ** (n * t)
    return A

# Solicitar datos al usuario
P = float(input("Ingrese el capital inicial: "))
r = float(input("Ingrese la tasa de interés anual (en %): ")) / 100  # Convertimos a decimal
n = int(input("Ingrese el número de veces que se capitaliza por año (mensual = 12, anual = 1, etc.): "))
t = float(input("Ingrese el tiempo en años: "))

# Calcular y mostrar el resultado
monto_final = interes_compuesto(P, r, n, t)
print(f"El monto final después de {t} años será: {monto_final:.2f}")