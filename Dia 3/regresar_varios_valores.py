print('*** Regresar una tupla de valores desde una función ***')

# Definición de la función
def persona_mayusculas(nombre, apelllido, edad):
    print('Esta función regresa varis valores (tupla)')
    return (nombre.upper(), apelllido.upper(), edad)

# Programa principal
nombre, apellido, edad = persona_mayusculas('Andrea', 'Trabanco', 47)
print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')