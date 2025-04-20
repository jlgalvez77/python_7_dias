print('*** Funciones en Python ***')

# 1. Definir la función
def saludar(parametro):
    print(f'Mensaje recibido: {parametro}')
    return  'Termina la función'

# 2. Llamamos a la función
argumento = input('Mensaje a enviar: ')
valor_devuelto = saludar(argumento)
print(f'Vslor devuelto de la función: {valor_devuelto}')