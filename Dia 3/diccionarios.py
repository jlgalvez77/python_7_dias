print('*** Diccionarios en Python ***')
# Un diccionario almacena sus elementos en forma de llave: valor y ademas
# no se pueden duplicar sus elementos
diccionario = {
    'nombre': 'Rodrigo',
    'apellido': 'Cervantes',
    'edad': 30
}

# Acceder a los elementos
print(f'Nombre: {diccionario['nombre']}')
print(f'Apellido: {diccionario['apellido']}')
print(f'Edad: {diccionario.get('edad')}')

# El largo de un diccionario
print(f'El largo del diccionario: {len(diccionario)}')

# Agregar un nuevo elemento
diccionario['telefono'] = 123456789
print(f'Diccionario modificado: {diccionario}')

# Obtener una lisa de las llaves del diccionario
print(f'Lista de las llaves del diccionario: {diccionario.keys()}')

# Obtener una lista de los valores del diccionario
print(f'Lista de los valores del diccionario: {diccionario.values()}')

# Obtener los elementos del diccionario (items)
print(f'Lista de los elementos del diccionario: {diccionario.items()}')

# Revisar si existe una llave en el diccionario
llave_a_buscar = 'nombre'
if llave_a_buscar in diccionario:
    print(f'La llave {llave_a_buscar} SI existe en el diccionario.')
else:
    print(f'La llave {llave_a_buscar} NO existe en el diccionario.')

# Actualizar un elemento del diccionario
diccionario['edad'] = 29
print(f'Nuevo diccionario: {diccionario}')

# Eliminar un elemento del diccionario
diccionario.pop('telefono')
print(f'Nuevo diccionario: {diccionario}')

# Recorrer las llaves de un diccionario (keys)
for llave in diccionario.keys():
    print(llave, end=' ')
print()

# Recorrer los valores de un diccionario (values)
for valor in diccionario.values():
    print(valor, end=' ')
print()

# Recorrer los elementos de un diccionario como tupla
for llave, valor in diccionario.items():
    print(f'Llave: {llave}, valor: {valor}')

# Limpiar el diccionario
diccionario.clear()
print(f'Diccionario limpio: {diccionario}')