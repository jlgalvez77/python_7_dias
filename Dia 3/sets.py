from os import remove

print('*** Sets en Python ***')
# Un set es un conjunto de datos NO ordenados
# Sus elementos no se pueden repetir
conjunto = {'Andrea', 100, 'Jose', True, 'Andrea'}
print(conjunto)

for elemento in conjunto:
    print(elemento, end=' ')
print()
numero_a_buscar = 100
if numero_a_buscar in conjunto:
    print(f'Si existe {numero_a_buscar} en el conjunto.')
else:
    print(f'No existe {numero_a_buscar} en el conjunto')

largo = len(conjunto)
print(f'La cantidad de elementos en mi set es de: {largo}')

# Eliminar un elemento
conjunto.remove(100)
print(conjunto)

# Agregar un elemento
conjunto.add(600)
print(conjunto)