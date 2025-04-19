print('*** Cajero Automatico ***')
saldo = 1000

while True:
    print('''Operaciones que puedes realizar:
    1. Consultar saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = input('Escoje una opción: ')

    if opcion == '1':
        print(f'Tu saldo es: {saldo}')
    elif opcion == '2':
        retirar = float(input('Indica el saldo a retirar: '))
        if retirar > saldo:
            print('Saldo insuficiente.')
        else:
            saldo -= retirar
            print(f'Tu nuevo saldo es: {saldo}')
    elif opcion == '3':
        deposito = float(input('Introduce la cantidad a depositar: '))
        saldo += deposito
        print(f'Tu nuevo saldo es: {saldo}')
    elif opcion == '4':
        print('Hasta pronto...')
        break
    else:
        print('Opción no valida.')
