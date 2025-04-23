print('***** Calculadora en Python con Funciones *****')


def mostrar_menu():
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Escoje una opción: '))
    return opcion


def pedir_valores():
    valor1 = float(input('Introduce el primer valor: '))
    valor2 = float(input('Introduce el segundo valor: '))
    return valor1, valor2


def ejecutar_operacion(opcion, salir):
    if opcion == 1:
        valor1, valor2 = pedir_valores()
        resultado = valor1 + valor2
        print(f'El resultado de la suma es: {resultado}\n')
    elif opcion == 2:
        valor1, valor2 = pedir_valores()
        resultado = valor1 - valor2
        print(f'El resultado de la resta es: {resultado}\n')
    elif opcion == 3:
        valor1, valor2 = pedir_valores()
        resultado = valor1 * valor2
        print(f'El resultado de la multiplicación es: {resultado}\n')
    elif opcion == 4:
        valor1, valor2 = pedir_valores()
        if valor2 == 0:
            print('No se puede dividir por cero.')
        else:
            resultado = valor1 / valor2
            print(f'El resultado de la división es: {resultado}\n')
    elif opcion == 5:
        print('Saliendo, hasta pronto')
        salir = True
    else:
        print('Opción no valida.\n')
        return salir
    return salir


# Codigo principal
salir = False
while not salir:
    opcion = mostrar_menu()
    salir = ejecutar_operacion(opcion, salir)
