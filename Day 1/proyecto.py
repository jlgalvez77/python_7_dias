import random

print('*** Sistema de Generador de ID Único ***')

nombre = input('¿Cual es tú nombre?: ')
apellido = input('¿Cual es tú apellido?: ')
nacimiento = input('¿Cual es tu año de nacimiento?(YYYY): ')
aleatorio = random.randint(1000, 9999)

letras_nombre = nombre[0:2]
letras_apellido = apellido[0:2]
cifras_nacimiento = nacimiento[2:4]
aleatorio_str = str(aleatorio)

print(f'Hola {nombre}, habitante de Gotham City')
print(f'Tu nuevo número de ID generado por el sistema es:')
print(f'{letras_nombre}{letras_apellido}{cifras_nacimiento}{aleatorio_str}')
