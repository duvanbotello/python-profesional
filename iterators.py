'''
Un iterator es una estructura de datos para guardar datos infinitos 🤯. 
Para entenderlo, primero debemos saber que un iterable es todo aquel objeto 
que puedo recorrer en un ciclo (lista, strings, etc). Un iterable es divisible.

Cuando hacemos un ciclo, Python internamente no está recorriendo a ese iterable, 
si no más bien ese iterable se convierte internamente en un iterador, que si puede 
ser recorrido. 🤔

todos los iterables se pueden convertir en iteradores para poder ser recorridos posteriormente en el lenguaje

Para crear un iterador:
'''

# Creando un iterador
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)  # Se recibe un iterable

# Iterando un iterador
print(next(my_iter))
# Cuando no quedan datos, la excepción StopIteration es elevada

'''
Para que no se rompa el código, hacemos manejo de errores: 🧠

asi funciona un ciclo for

'''
# Creando un iterador
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# Iterando un iterador
while True: 
	try: 
		element = next(my_iter)
		print(element)
	except StopIteration:
		break


'''
Esta es una manera eficiente de extraer todos los elementos de un iterable. De hecho, 
esta es la manera en la que funciona un ciclo for, es la azúcar sintaxis de este código anterior 😍. 
El ciclo for en si mismo no existe.

¿Cómo construyo un iterador?. Una opción es castear desde un iterable. Para hacerlo 
desde cero, debemos usar el protocolo de los iteradores que contiene dos clases 
importantes __iter__ y __next__:
'''

class EvenNumbers:
	"""Calse que implementa un iterador de todos los
		 números pares, o los números pares hasta un máximo"""
	def __init__(self, max = None):
		self.max = max

	def __iter__(self):
		self.num = 0
		return self

	def __next__(self):
		if not self.max or self.num <= self.max:
			result = self.num
			self.num += 2
			return result
		else:
			raise StopIteration


'''
Las ventajas de usar iteradores: Nos ahorra recursos computacionales y de memoria, 
ya que tenemos una función matemática de como obtener los siguientes elementos, 
sin necesidad de guardarlos todos 👀.
'''