'''
   Decorador: Es una funcion que recibe como parametro otra funcion, le añade cosas y retorna una funcion diferente.
   -> Una funcion que le añade super poderes a otra funcion.
'''

def decorador(func):
    def envoltura():
        print('Esto se añade a mi funcion original')
        func()
    return envoltura

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura


@decorador
def saludo():
    print('Hola')

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibistes un mensaje'

saludo()
print(mensaje('duvan'))

