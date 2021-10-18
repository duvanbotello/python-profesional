'''

Un pequeño resumen:

Los sets son una estructura de datos muy similares a las listas en cuanto a su forma, pero presentan ciertas características particulares:
*Los sets son inmutables
*Cada elemento del set es único, esto es que no se admiten duplicados, aun si durante la definición del set se agregan elementos repetidos pyhton solo guarda un elemento
*los sets guardan los elementos en desorden
*Para declararlos se utilizan los {} parecido a los diccionarios solo que carece de la composición de conjunto {a:b, c:d}


'''

# set de enteros
my_set = {1, 3, 5}
print(my_set)

# set de diferentes tipos de datos
my_set = {1.0, "Hi", (1, 4, 7)}
print(my_set)

'''
Los sets no pueden ser leídos como las listas o recorridos a través de slices, 
esto debido a que no tienen un criterio de orden. Sin embargo si podemos agregar 
o eliminar items de los sets utilizando métodos:

add(): nos permite agregar elementos al set, si se intenta agregar un elemento existente simplemente python los ignorara
update(): nos permite agregar múltiples elementos al set
remove(): permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python elevará un error
discard(): permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python dejará el set intacto, sin elevar ningún error.
pop(): permite eliminar un elemento del set, pero lo hará de forma aleatoria.
clear(): Limpia completamente el set, dejándolo vació.

'''

# ejemplo de operaciones sobre sets
my_set = {1, 2, 3}
print(my_set)  # Output {1, 2, 3}

# añadiendo un elemento al set
my_set.add(4)
print(my_set)  # Output {1, 2, 3, 4}

# añadiendo varios elementos al set, python ignorará elementos repetidos
my_set.update([1, 5, 6])
print(my_set)  # Output {1, 2, 3, 4, 5, 6}

# eliminado elementos del set
my_set.discard(1)
print(my_set)  # Output {2, 3, 4, 5, 6}

# borrando un elemento aleatorio
my_set.pop()
print(my_set)  # Output el set menos un elemento aleatorio

# limpiar el set
my_set.clear()
print(my_set)  # Output set()


'''
Podemos utilizar estructuras de datos existentes 
para transformarlas a sets utilizando el método set:
'''
# usando listas para crear sets
my_list = [1, 2, 3, 3, 4, 5]
my_set = set(my_list)
print(my_set)  # output {1, 2, 3, 4, 5}

# usando tuplas para crear sets
my_tuple = ('hola', 'hola', 1, 2)
my_set2: set(my_tuple)
print(my_set2)  # Output {'hola', 1}


'''
Operaciones con Sets

Unión

Resultado de juntar todos los elementos que tienen ambos, combinar ambos sets

'''

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 | set_2 #  -> {1, 2, 3, 4, 5}

# O de forma mas explicita
set_1.union(set_2) #  -> {1, 2, 3, 4, 5}

'''
Intersección
Los que se repiten en ambos sets
'''

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 & set_2 #  -> {3}

# O de forma mas explicita
set_1.intersection(set_2) #  -> {3}

'''
Diferencia
Tomar dos sets y de uno quitarle todos los elementos que tiene el otro
'''

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 - set_2 #  -> {1, 2}

# O de forma mas explicita
set_1.difference(set_2) #  -> {1, 2}

'''
Diferencia Simétrica
Tomar todos los elementos exceptos los que se repiten
'''

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1 ^ set_2 #  -> {1, 2, 4, 5}

# O de forma mas explicita
set_1.symmetric_difference(set_2) #  -> {1, 2, 4, 5}