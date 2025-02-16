#18.    Resolver ecuaciones cuadraticas.
import math

def resolver_ecuacion_cuadratica(a, b, c):
    # Verificar que no sea una ecuación lineal
    if a == 0:
        return "No es una ecuación cuadrática. 'a' debe ser distinto de cero."
    
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c
    
    # Evaluar el discriminante
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Dos soluciones reales: x1 = {x1:.2f}, x2 = {x2:.2f}"
    
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Una solución real doble: x = {x:.2f}"
    
    else:
        # Soluciones complejas
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2*a)
        return (f"Dos soluciones complejas: x1 = {parte_real:.2f} + {parte_imaginaria:.2f}i, "
                f"x2 = {parte_real:.2f} - {parte_imaginaria:.2f}i")

# Solicitar coeficientes al usuario
try:
    a = float(input("Ingresa el coeficiente a: "))
    b = float(input("Ingresa el coeficiente b: "))
    c = float(input("Ingresa el coeficiente c: "))

    resultado = resolver_ecuacion_cuadratica(a, b, c)
    print(resultado)

except ValueError:
    print("Error: Ingresa valores numéricos válidos.")
