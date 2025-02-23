#29. Generar y analizar datos estadısticos.
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Generar datos aleatorios (por ejemplo, 1000 números con distribución normal)
datos = np.random.normal(loc=50, scale=10, size=1000)  # media=50, desviación estándar=10, tamaño=1000

# Calcular estadísticas descriptivas
media = np.mean(datos)
mediana = np.median(datos)
desviacion_estandar = np.std(datos)
varianza = np.var(datos)
percentil_25 = np.percentile(datos, 25)
percentil_75 = np.percentile(datos, 75)
rango = np.ptp(datos)  # Rango = max(datos) - min(datos)

# Mostrar estadísticas
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion_estandar}")
print(f"Varianza: {varianza}")
print(f"Percentil 25: {percentil_25}")
print(f"Percentil 75: {percentil_75}")
print(f"Rango: {rango}")

# Analizar la distribución (por ejemplo, la distribución de los datos)
# Histograma
plt.hist(datos, bins=30, edgecolor='black')
plt.title("Histograma de los Datos Generados")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

# Análisis adicional con scipy.stats (como la distribución normal)
kurtosis = stats.kurtosis(datos)  # Medida de la "altitud" de los picos de la distribución
asimetria = stats.skew(datos)  # Medida de la asimetría de la distribución

print(f"Asimetría: {asimetria}")
print(f"Kurtosis: {kurtosis}")
