print('*** Calculadora en Python ***')

while True:
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Escoje una opción: '))

    if opcion in range(1, 5):
        valor1 = float(input('Introduce el primer valor: '))
        valor2 = float(input('Introduce el segundo valor: '))
        if opcion == 1:
            resultado = valor1 + valor2
            print(f'El resultado de la suma es: {resultado}')
        if opcion == 2:
            resultado = valor1 - valor2
            print(f'El resultado de la resta es: {resultado}')
        if opcion == 3:
            resultado = valor1 * valor2
            print(f'El resultado de la multiplicación es: {resultado}')
        if opcion == 4:
            if valor2 == 0:
                print('No se puede dividir por cero.')
            else:
                resultado = valor1 / valor2
                print(f'El resultado de la división es: {resultado}')
    elif opcion == 5:
        print('Saliendo de la calculadora...')
        break
    else:
        print('Opción no valida.')
