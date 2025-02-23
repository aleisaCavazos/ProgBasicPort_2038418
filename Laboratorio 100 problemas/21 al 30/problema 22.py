# 22. Simular el lanzamiento de un dado y una moneda.
import random

def simular_dado_moneda():
    dado = random.randint(1, 6)
    moneda = random.choice(["Cara", "Cruz"])
    print(f"Resultado del dado: {dado}")
    print(f"Resultado de la moneda: {moneda}")

simular_dado_moneda()