import pandas as pd
from collections import Counter

# --- Paso 1: Cargar datos desde el Excel ---
excel_path = "datos_ropa.xlsx"  # Asegúrate de que esté en la misma carpeta

# Leer las hojas "Historial" y "Favoritos"
historial_df = pd.read_excel(excel_path, sheet_name="Historial")
favoritos_df = pd.read_excel(excel_path, sheet_name="Favoritos")

# --- Paso 2: Procesar datos ---

# Extraer solo la columna de búsquedas
busquedas = historial_df["Búsqueda"].dropna().str.lower().tolist()

# Contar frecuencia de términos buscados
conteo_busquedas = Counter(busquedas)

# Extraer solo la columna de productos favoritos
favoritos = favoritos_df["Producto y URL"].dropna().tolist()

# Contar frecuencia de productos favoritos
conteo_favoritos = Counter(favoritos)

# --- Mostrar conteo como prueba ---
print("\n--- Conteo de Búsquedas ---")
for prenda, cantidad in conteo_busquedas.items():
    print(f"{prenda}: {cantidad} vez/veces")

print("\n--- Conteo de Favoritos ---")
for producto, cantidad in conteo_favoritos.items():
    print(f"{producto}: {cantidad} vez/veces")
import matplotlib.pyplot as plt

# --- Paso 3: Crear gráfica de barras de búsquedas más comunes ---

# Tomar los 5 términos más buscados
top_busquedas = conteo_busquedas.most_common(5)

# Separar etiquetas y valores
etiquetas = [item[0] for item in top_busquedas]
valores = [item[1] for item in top_busquedas]

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.bar(etiquetas, valores, color='skyblue')
plt.title("Top 5 prendas más buscadas")
plt.xlabel("Prenda")
plt.ylabel("Cantidad de búsquedas")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# --- Gráfica de pastel: distribución de las prendas más buscadas ---

# Usamos los mismos 5 términos más buscados
labels = [item[0] for item in top_busquedas]
sizes = [item[1] for item in top_busquedas]

# Crear la gráfica
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Distribución de prendas más buscadas")
plt.axis("equal")  # Hace que el pastel sea redondo
plt.tight_layout()
plt.show()
# --- Gráfica de barras horizontal: productos más agregados a favoritos ---

# Tomar los 5 productos más favoritos
top_favoritos = conteo_favoritos.most_common(5)
nombres = [item[0] for item in top_favoritos]
cantidades = [item[1] for item in top_favoritos]

# Crear la gráfica
plt.figure(figsize=(9, 6))
plt.barh(nombres, cantidades, color='lightgreen')
plt.title("Top 5 productos favoritos")
plt.xlabel("Cantidad de veces guardado")
plt.ylabel("Producto")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# --- Gráfico de dispersión: longitud de término vs frecuencia de búsqueda ---

# Crear listas para el gráfico
x_longitudes = [len(palabra) for palabra, _ in conteo_busquedas.items()]
y_frecuencias = [frecuencia for _, frecuencia in conteo_busquedas.items()]

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.scatter(x_longitudes, y_frecuencias, color='orange', edgecolors='black')
plt.title("Longitud del término vs frecuencia de búsqueda")
plt.xlabel("Longitud del término (número de letras)")
plt.ylabel("Frecuencia de búsqueda")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
