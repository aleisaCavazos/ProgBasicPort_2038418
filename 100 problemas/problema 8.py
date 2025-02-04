#8.	Calcular el ´area y la circunferencia de un c´ırculo.
import math

def calcular_area_y_circunferencia(radio):
    area = math.pi * radio ** 2  # Fórmula del área
    circunferencia = 2 * math.pi * radio  # Fórmula de la circunferencia
    return area, circunferencia

# Solicitar datos al usuario
radio = float(input("Ingrese el radio del círculo: "))

# Calcular y mostrar los resultados
area, circunferencia = calcular_area_y_circunferencia(radio)

print(f"El área del círculo con radio {radio} es: {area:.2f}")
print(f"La circunferencia del círculo con radio {radio} es: {circunferencia:.2f}")
