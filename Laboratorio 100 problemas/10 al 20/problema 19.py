#19. Generar numeros aleatorios con distintas distribuciones.
import random

# Generar un número aleatorio en el rango [a, b]
a = 1
b = 10
numero_uniforme = random.uniform(a, b)
print(f"Número aleatorio uniforme entre {a} y {b}: {numero_uniforme}")

import random

# Generar un número aleatorio con distribución normal
media = 0  # Media de la distribución
desviacion_estandar = 1  # Desviación estándar
numero_normal = random.gauss(media, desviacion_estandar)
print(f"Número aleatorio con distribución normal (media={media}, desviación={desviacion_estandar}): {numero_normal}")

import random

# Generar un número aleatorio con distribución binomial
n = 10  # Número de intentos
p = 0.5  # Probabilidad de éxito
numero_binomial = random.binomial(n, p)
print(f"Número aleatorio con distribución binomial (n={n}, p={p}): {numero_binomial}")

import random

# Generar un número aleatorio con distribución exponencial
lambda_ = 1  # Tasa de eventos
numero_exponencial = random.expovariate(lambda_)
print(f"Número aleatorio con distribución exponencial (lambda={lambda_}): {numero_exponencial}")
