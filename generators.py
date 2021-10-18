'''Es lo mismo que un iterador pero escrito de forma más elegante.

Los generadores son azúcar sintáctica para los Iteradores. 
Son básicamente funciones que guardan un estado, a diferencia de los iteradores, 
que son clases.

Ejemplo:

'''

def my_gen():

  """un ejemplo de generadores"""

  print('Hello world!')
  n = 0
  yield n # es exactamente lo mismo que return pero detiene la función, cuando se vuelva a llamar a la función, seguirá desde donde se quedó

  print('Hello heaven!')
  n = 1
  yield n

  print('Hello hell!')
  n = 2
  yield n


a = my_gen()
print(next(a)) # Hello world!
print(next(a)) # Hello heaven!
print(next(a)) # Hello hell!
print(next(a)) StopIteration


# Generator expression

my_list = [0, 1, 4, 7, 9, 10]

my_second_list = [x*2 for x in my_list] # List comprehension
my_second_gen = (x*2 for x in my_list)  # Generator expression

'''
    Generator expression. 🤯 Se trae un elemento a la vez, y no ocupa toda la memoria 😯.
    Los generadores ahorran memoria y tiempo de ejecución al obtener los elementos de 
    la estructura (iterador) solo cuando se le solicite.
'''