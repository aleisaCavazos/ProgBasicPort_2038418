import json
import random

# Algunas categorías y nombres básicos para generar variedad
tipos_prenda = [
    "Camisa", "Pantalón", "Vestido", "Falda", "Chaqueta", "Suéter",
    "Blusa", "Short", "Abrigo", "Traje", "Sudadera", "Leggings",
    "Chamarra", "Top", "Camiseta", "Jeans", "Overol", "Blazer",
    "Chaleco", "Pijama", "Bermuda", "Mono", "Bata", "Capa", "Cardigan"
]
colores = [
    "rojo", "azul", "verde", "negro", "blanco", "gris", "amarillo",
    "rosado", "morado", "naranja", "beige", "marrón", "turquesa"
]
materiales = ["algodón", "seda", "poliéster", "lana", "cuero", "denim", "lino"]

# Generar 500 prendas distintas
ropa = []
for i in range(1, 501):
    tipo = random.choice(tipos_prenda)
    color = random.choice(colores)
    material = random.choice(materiales)
    nombre = f"{tipo} {color} de {material}"
    url = f"https://ejemplo.com/producto/{i}"
    prenda = {"objectID": i, "name": nombre, "url": url}
    ropa.append(prenda)

# Guardar en archivo JSON
output_path = "C:\\Users\\Asael\\Desktop\\ropa_500.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(ropa, f, indent=4, ensure_ascii=False)

output_path
