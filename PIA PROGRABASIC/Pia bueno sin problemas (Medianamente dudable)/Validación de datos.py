def validar_datos_para_visualizacion():
    """
    Valida que los datos en historial.json y favoritos.json sean correctos,
    no estén vacíos, duplicados ni mal formateados.
    """
    HISTORIAL_PATH = "historial.json"
    FAVORITOS_PATH = "favoritos.json"
    def cargar_json(path):
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            return json.load(f)

    import os
    import json

    def guardar_json(path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    historial = cargar_json(HISTORIAL_PATH)
    favoritos = cargar_json(FAVORITOS_PATH)

    historial_valido = []
    favoritos_validos = []

    # Validar entradas del historial
    for entrada in historial:
        if isinstance(entrada, str) and entrada.strip():
            historial_valido.append(entrada.strip().lower())  # Limpieza básica

    # Validar entradas de favoritos
    for favorito in favoritos:
        if isinstance(favorito, str) and " - " in favorito:
            nombre, url = favorito.split(" - ", 1)
            if nombre.strip() and url.startswith("http"):
                favoritos_validos.append(favorito.strip())

    # Eliminar duplicados
    historial_valido = list(set(historial_valido))
    favoritos_validos = list(set(favoritos_validos))

    # Guardar los datos validados nuevamente
    guardar_json(HISTORIAL_PATH, historial_valido)
    guardar_json(FAVORITOS_PATH, favoritos_validos)

    print("Datos validados exitosamente para visualización.")

