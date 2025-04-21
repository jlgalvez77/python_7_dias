print('*** Función con argumentos por nombre ***')

def crear_persona(nombre, apellido, edad):
    print(f'Persona: nombre = {nombre}, apellido: {apellido}, edad: {edad}')

# Llamamos a la función
#crear_persona('Ricardo', 'Cruz', '29')

# Llamar a la función usando argumentos por nombre
crear_persona(edad=29, nombre='Ricardo', apellido='Cruz')