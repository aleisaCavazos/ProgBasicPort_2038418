import requests
import re
import json
import os 
from dotenv import load_dotenv
from colorama import init, Fore, Style
from openpyxl import Workbook
from openpyxl.styles import Font

#NOTA IMPORTANTE: Instalar pip install 'algoliasearch>=4,<5'
#NOTA IMPORTANTE: Instalar pip install 'algoliasearch>=4,<5'
#El programa mismo ya crea el archivo JSON de favoritos y historial si no existen, por lo que no es necesario crearlos manualmente
#El ropa_500.json tiene la informacion de Algolia, siempre tenerlo ahi para que funcione el programa
# instalar tambien pip install openpyxl / pip install pandas / pip install matplotlib
# --- Inicializar colorama ---
init(autoreset=True)

# --- Cargar variables de entorno ---
load_dotenv()
CLARIFAI_API_KEY = "050f9bbbe935bf7d921fb60840a678b7"
ALGOLIA_APP_ID = "97VTQJZ1EI"
ALGOLIA_API_KEY = "41d4f973e4c722dd607118d4d55148f1"
NEWSDATA_API_KEY = "050f9bbbe935bf7d921fb60840a678b7"

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

def mostrar_error(mensaje):
    print(Fore.RED + f"❌ {mensaje}")

def mostrar_exito(mensaje):
    print(Fore.GREEN + f"✅ {mensaje}")

def mostrar_info(mensaje):
    print(Fore.CYAN + mensaje)

# --- Exportar a Excel ---
def exportar_a_excel(historial_path, favoritos_path, nombre_archivo="datos_ropa.xlsx"):
    historial = cargar_json(historial_path)
    favoritos = cargar_json(favoritos_path)

    wb = Workbook()
    ws1 = wb.active
    ws1.title = "Historial"
    ws1.append(["#", "Búsqueda"])
    for i, entrada in enumerate(historial, 1):
        ws1.append([i, entrada])
    for cell in ws1["1:1"]:
        cell.font = Font(bold=True)

    ws2 = wb.create_sheet(title="Favoritos")
    ws2.append(["#", "Producto y URL"])
    for i, item in enumerate(favoritos, 1):
        ws2.append([i, item])
    for cell in ws2["1:1"]:
        cell.font = Font(bold=True)

    wb.save(nombre_archivo)
    mostrar_exito(f"Archivo Excel guardado como '{nombre_archivo}'")

# --- Funciones API ---
def buscar_noticias():
    try:
        url = f"https://newsdata.io/api/1/latest?apikey={NEWSDATA_API_KEY}&q=ropa&country=us"
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        noticias = respuesta.json()
        mostrar_info("\n📰 Noticias recientes sobre moda:")
        for i, articulo in enumerate(noticias.get("results", [])[:5]):
            print(f"{i+1}. {articulo.get('title')}")
    except Exception as e:
        mostrar_error(f"Error al obtener noticias: {e}")

def buscar_por_imagen():
    try:
        mostrar_info("(Simulación) Analizando imagen con Clarifai...")

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
        response = requests.post(
            "https://api.clarifai.com/v2/models/general-image-recognition/outputs",
            headers=headers,
            json=body
        )
        response.raise_for_status()
        mostrar_exito("Imagen procesada exitosamente (simulado).")
    except Exception as e:
        mostrar_error(f"Error con la API de Clarifai: {e}")

def buscar_por_texto():
    query = input("\n🔍 Describe la prenda que buscas: ").strip()
    if not query:
        mostrar_error("La descripción no puede estar vacía.")
        return

    try:
        mostrar_info(f"Buscando '{query}' en Algolia...")

        url = f"https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/ropa_500/query"
        headers = {
            "X-Algolia-API-Key": ALGOLIA_API_KEY,
            "X-Algolia-Application-Id": ALGOLIA_APP_ID,
            "Content-Type": "application/json"
        }
        data = {
            "params": f"query={query}"
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        resultados = response.json()
        favoritos = cargar_json(FAVORITOS_PATH)

        if not resultados.get("hits"):
            mostrar_info("No se encontraron resultados.")
            return

        for i, item in enumerate(resultados.get("hits", [])[:5]):
            nombre = item.get('name', 'Producto sin nombre')
            url_producto = item.get('url', 'Sin enlace')
            print(f"{i+1}. {nombre} - {url_producto}")

            agregar = input("¿Agregar a favoritos? (s/n): ").lower()
            if agregar == "s":
                favoritos.append(f"{nombre} - {url_producto}")

        guardar_json(FAVORITOS_PATH, favoritos)

        historial = cargar_json(HISTORIAL_PATH)
        historial.append(query)
        guardar_json(HISTORIAL_PATH, historial)

        mostrar_exito("Búsqueda completada.")

    except Exception as e:
        mostrar_error(f"Error al buscar en Algolia: {e}")

# --- Funciones de Menú ---
def registrar_usuario():
    print(Fore.MAGENTA + "\n--- Registro de Usuario ---")
    correo = input("Correo electrónico: ")
    while not validar_correo(correo):
        mostrar_error("Correo no válido. Intenta de nuevo.")
        correo = input("Correo electrónico: ")
    mostrar_exito("Registro exitoso.\n")

def ver_historial():
    historial = cargar_json(HISTORIAL_PATH)
    if historial:
        mostrar_info("\n--- Historial de búsquedas ---")
        for i, item in enumerate(historial):
            print(f"{i+1}. {item}")
    else:
        mostrar_info("\nNo hay historial aún.")

def ver_favoritos():
    favoritos = cargar_json(FAVORITOS_PATH)
    if favoritos:
        mostrar_info("\n--- Productos favoritos ---")
        for i, item in enumerate(favoritos):
            print(f"{i+1}. {item}")
    else:
        mostrar_info("\nAún no tienes productos favoritos.")

# --- Menú Principal ---
def menu():
    while True:
        print(Fore.YELLOW + """
--- Menú Principal ---
1. Registrarse
2. Buscar ropa por descripción
3. Buscar ropa por imagen
4. Ver historial de productos
5. Ver favoritos
6. Ver noticias sobre moda
7. Salir
8. Exportar historial y favoritos a Excel
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
            mostrar_info("¡Hasta luego! 🛍️")
            break
        elif opcion == "8":
            exportar_a_excel(HISTORIAL_PATH, FAVORITOS_PATH)
        else:
            mostrar_error("Opción no válida. Intenta otra vez.")

# --- Ejecución ---
if __name__ == "__main__":
    menu()