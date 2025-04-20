print('*** Listas y Diccionarios ***')

personas = [{
    'nombre': 'Andrea',
    'apellido': 'Trabanco',
    'edad': 47
} , {
    'nombre': 'Jose',
    'apellido': 'Galvez',
    'edad': 48
}]

print(personas)

# Acceder a un diccionario (persona)
print(personas[0])

# Acceder a un valor (llave) nombre del primer elemento
print(personas[0].get('nombre'))

print(personas[1].get('edad'))

# Recorrer los elementos de la lista (elemento = diccionario)
for contador, persona in enumerate(personas):
    print(f'Persona: {contador}: {persona.get('nombre')}')