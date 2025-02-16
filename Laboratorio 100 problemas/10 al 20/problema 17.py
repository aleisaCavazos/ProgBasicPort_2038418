#17.	Implementar estructuras de datos ba´sicas: pila, cola y lista enlazada.
# Definición de la clase Pila
class Pila:
	def __init__(self):
		self.items = []

	def apilar(self, item):
		self.items.append(item)

	def desapilar(self):
		if not self.esta_vacia():
			return self.items.pop()

	def ver_tope(self):
		if not self.esta_vacia():
			return self.items[-1]

	def esta_vacia(self):
		return len(self.items) == 0

# Usando Pila
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print(pila.desapilar())  # Debería imprimir 3
print(pila.ver_tope())   # Debería imprimir 2

# Definición de la clase Cola
class Cola:
	def __init__(self):
		self.items = []

	def encolar(self, item):
		self.items.insert(0, item)

	def desencolar(self):
		if not self.esta_vacia():
			return self.items.pop()

	def ver_frente(self):
		if not self.esta_vacia():
			return self.items[-1]

	def esta_vacia(self):
		return len(self.items) == 0

# Usando Cola
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print(cola.desencolar())  # Debería imprimir 1
print(cola.ver_frente())  # Debería imprimir 2

# Definición de la clase ListaEnlazada
class Nodo:
	def __init__(self, dato):
		self.dato = dato
		self.siguiente = None

class ListaEnlazada:
	def __init__(self):
		self.cabeza = None

	def agregar_al_final(self, dato):
		if not self.cabeza:
			self.cabeza = Nodo(dato)
		else:
			actual = self.cabeza
			while actual.siguiente:
				actual = actual.siguiente
			actual.siguiente = Nodo(dato)

	def eliminar_primero(self):
		if self.cabeza:
			self.cabeza = self.cabeza.siguiente

	def mostrar_lista(self):
		actual = self.cabeza
		while actual:
			print(actual.dato, end=" -> ")
			actual = actual.siguiente
		print("None")

# Usando Lista Enlazada
lista = ListaEnlazada()
lista.agregar_al_final(1)
lista.agregar_al_final(2)
lista.agregar_al_final(3)
lista.mostrar_lista()  # Debería imprimir: 1 -> 2 -> 3 -> None
lista.eliminar_primero()
lista.mostrar_lista()  # Debería imprimir: 2 -> 3 -> None
