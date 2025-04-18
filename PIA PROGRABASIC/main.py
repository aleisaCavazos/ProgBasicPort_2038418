import requests
import re
import json
import os

# --- Configuración Inicial ---
CLARIFAI_API_KEY = "TU_API_KEY"
ALGOLIA_APP_ID = "TU_APP_ID"
ALGOLIA_API_KEY = "TU_API_KEY"
NEWSDATA_API_KEY = "TU_API_KEY"

# --- Rutas de Archivos JSON ---
HISTORIAL_PATH = "historial.json"
FAVORITOS_PATH = "favoritos.json"

# --- Funciones Utilitarias ---
def validar_correo(correo):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo)

def guardar_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def cargar_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

# --- Funciones API de ejemplo ---
def buscar_noticias():
    url = f"https://newsdata.io/api/1/latest?apikey={NEWSDATA_API_KEY}&q=ropa&country=us"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        noticias = respuesta.json()
        print("\nNoticias recientes sobre moda:")
        for i, articulo in enumerate(noticias.get("results", [])[:5]):
            print(f"{i+1}. {articulo.get('title')}")
    else:
        print("Error al obtener noticias.")

def buscar_por_imagen():
    print("(Simulación) Aquí iría la lógica para analizar imagen con Clarifai.")
    print("(Por ahora es solo un ejemplo para mostrar el uso de la API Clarifai)")

    headers = {
        "Authorization": f"Key {CLARIFAI_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "inputs": [
            {
                "data": {
                    "image": {
                        "url": "https://samples.clarifai.com/metro-north.jpg"
                    }
                }
            }
        ]
    }
    response = requests.post("https://api.clarifai.com/v2/models/general-image-recognition/outputs", headers=headers, json=body)
    if response.status_code == 200:
        print("Resultado: Imagen procesada exitosamente (simulado).")
    else:
        print("Error con la API de Clarifai.")

def buscar_por_texto():
    query = input("\nDescribe la prenda que buscas: ")
    print(f"(Simulación) Buscando '{query}' en Algolia")
    url = f"https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/ropa/query"
    headers = {
        "X-Algolia-API-Key": ALGOLIA_API_KEY,
        "X-Algolia-Application-Id": ALGOLIA_APP_ID,
        "Content-Type": "application/json"
    }
    data = {
        "params": f"query={query}"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        resultados = response.json()
        print("\nResultados simulados:")
        favoritos = cargar_json(FAVORITOS_PATH)
        for i, item in enumerate(resultados.get("hits", [])[:5]):
            nombre = item.get('name', 'Producto sin nombre')
            url = item.get('url', 'Sin enlace')
            print(f"{i+1}. {nombre} - {url}")
            agregar = input("¿Agregar a favoritos? (s/n): ")
            if agregar.lower() == "s":
                favoritos.append(f"{nombre} - {url}")
        guardar_json(FAVORITOS_PATH, favoritos)
    else:
        print("Error al buscar con Algolia.")

    historial = cargar_json(HISTORIAL_PATH)
    historial.append(query)
    guardar_json(HISTORIAL_PATH, historial)

# --- Funciones de Menú ---
def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    correo = input("Correo electrónico: ")
    while not validar_correo(correo):
        print("Correo no válido. Intenta de nuevo.")
        correo = input("Correo electrónico: ")
    print("Registro exitoso ✔️\n")

def ver_historial():
    historial = cargar_json(HISTORIAL_PATH)
    if historial:
        print("\n--- Historial de búsquedas ---")
        for i, item in enumerate(historial):
            print(f"{i+1}. {item}")
    else:
        print("\nNo hay historial aún.")

def ver_favoritos():
    favoritos = cargar_json(FAVORITOS_PATH)
    if favoritos:
        print("\n--- Productos favoritos ---")
        for i, item in enumerate(favoritos):
            print(f"{i+1}. {item}")
    else:
        print("\nAún no tienes productos favoritos.")

# --- Menú Principal ---
def menu():
    while True:
        print("""
--- Menú Principal ---
1. Registrarse
2. Buscar ropa por descripción
3. Buscar ropa por imagen
4. Ver historial de productos
5. Ver favoritos
6. Ver noticias sobre moda
7. Salir
""")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            buscar_por_texto()
        elif opcion == "3":
            buscar_por_imagen()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            ver_favoritos()
        elif opcion == "6":
            buscar_noticias()
        elif opcion == "7":
            print("Hasta luego! 🛍️")
            break
        else:
            print("Opción no válida. Intenta otra vez.")

# --- Ejecución ---
if __name__ == "__main__":
    menu()