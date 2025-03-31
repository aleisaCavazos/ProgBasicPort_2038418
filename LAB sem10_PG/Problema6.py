# EJERCICIO 6
# Clase Vehiculo (clase base)
class Vehiculo:
    def __init__(self, marca, modelo, ano, precio):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precio = precio

    # Método para mostrar la información del vehículo
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.ano}")
        print(f"Precio: ${self.precio}")

# Subclase Automovil (hereda de Vehiculo)
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, ano, precio, numero_puertas):
        super().__init__(marca, modelo, ano, precio)
        self.numero_puertas = numero_puertas

    # Método para mostrar la información del automóvil
    def mostrar_informacion(self):
        super().mostrar_informacion()  # Mostrar información base
        print(f"Número de puertas: {self.numero_puertas}")

# Subclase Motocicleta (hereda de Vehiculo)
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, ano, precio, cilindrada):
        super().__init__(marca, modelo, ano, precio)
        self.cilindrada = cilindrada

    # Método para mostrar la información de la motocicleta
    def mostrar_informacion(self):
        super().mostrar_informacion()  # Mostrar información base
        print(f"Cilindrada: {self.cilindrada} cc")

# Crear instancias de los vehículos
auto = Automovil("Toyota", "Corolla", 2020, 20000, 4)
moto = Motocicleta("Harley-Davidson", "Sportster", 2021, 15000, 1200)

# Mostrar información de los vehículos
print("Información del automóvil:")
auto.mostrar_informacion()

print("\nInformación de la motocicleta:")
moto.mostrar_informacion()
