# EJERCICIO 4
import math

# Función para calcular las estadísticas
def calculadora_estadisticas(*args):
    # Calcular el promedio usando lambda
    promedio = lambda numeros: sum(numeros) / len(numeros)
    
    # Calcular la mediana
    def mediana(numeros):
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        if n % 2 == 1:
            return numeros_ordenados[n // 2]
        else:
            return (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2
    
    # Calcular la desviación estándar
    def desviacion_estandar(numeros, prom):
        return math.sqrt(sum((x - prom) ** 2 for x in numeros) / len(numeros))
    
    # Calcular estadísticas
    prom = promedio(args)
    med = mediana(args)
    desviacion = desviacion_estandar(args, prom)
    
    # Mostrar los resultados
    print(f"Promedio: {prom}")
    print(f"Mediana: {med}")
    print(f"Desviación estándar: {desviacion}")

# Solicitar al usuario una lista de números
entrada = input("Ingresa una lista de números separados por espacios: ")
numeros = [float(x) for x in entrada.split()]

# Llamar a la función de estadísticas
calculadora_estadisticas(*numeros)
