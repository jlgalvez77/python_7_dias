print('*** Sistema de Administración de Cuentas ***')

while True:
    print('''Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir''')
    opcion = input('Escoje una opción: ')

    if opcion == '1':
        print('Creando cuenta...')
    elif opcion == '2':
        print('Eliminando cuenta...')
    elif opcion == '3':
        print('Saliendo...')
        break
    else:
        print('Selección no valida.')
