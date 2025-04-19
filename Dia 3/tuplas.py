print('*** Tuplas en Python ***')
nombres = ('Karla', 'Juan', 'Laura')
print(nombres)

# Tupla heterogenea
tupla_heterogenea = (100, True, 'Andrea')
print(tupla_heterogenea)

# Recorrer los elementos
for nombre in nombres:
    print(nombre, end=' ')
print()
numeros = (100, 200, 300, 400, 500)
print(f'Para el indice 0, el valor es: {numeros[0]}')
print(f'Para el indice 3, el valor es: {numeros[3]}')
print(f'Para el índice -1, el valor es: {numeros[-1]}')

numero_a_buscar = 200
if numero_a_buscar in numeros:
    print(f'El numero: {numero_a_buscar}, se encuentra en la tupla')
else:
    print(f'El número: {numero_a_buscar}, no se encuentra en la tupla')