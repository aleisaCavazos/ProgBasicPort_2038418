#28. Simular una cuenta bancaria con depositos y retiros.
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Has depositado {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Has retirado {cantidad}. Nuevo saldo: {self.saldo}")
            else:
                print("Saldo insuficiente para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def consultar_saldo(self):
        print(f"El saldo actual de {self.titular} es: {self.saldo}")

# Función para interactuar con la cuenta
def menu():
    # Crear la cuenta
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    cuenta = CuentaBancaria(titular)
    
    while True:
        print("\n--- Menú de la Cuenta Bancaria ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            cuenta.consultar_saldo()
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == "3":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()
