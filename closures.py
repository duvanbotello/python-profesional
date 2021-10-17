'''Nested functions: Las funciones anidadas son simplemente funciones creadas dentro de otra función. 
Podemos hacer return de una función creada dentro de otra función 😵 y luego guardar esas funciones 
en variables que podemos utilizar.'''

'''

Como saber si es una clausura o no:

* Debemos tener una nested function
* La nedted function debe referenciar un valor de un scope superior.
* La funcion que envuielve a la nested function debe retornarla tambien
'''

def make_multiplier(x):

    def multuplier(n):
        return x * n
    
    return multuplier


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo puedes repetir cadenas'
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola'))

    times10 = make_multiplier(10)
    times4 = make_multiplier(4)

    print(times10(3))
    print(times4(5))
    print(times10(times4(2)))


if __name__ == '__main__':
    run()