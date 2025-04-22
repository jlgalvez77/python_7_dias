print('***** Calculadora en Python con Funciones *****')
def mostrar_menu():
    print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = input('Escoje una opción: ')
    return opcion

def pedir_valores():
    pass

def ejecutar_operacion(opcion, salir):
    if opcion == '1':
        pass
    elif opcion == '2':
        pass
    elif opcion == '3':
        pass
    elif opcion == '4':
        pass
    elif opcion == '5':
        print('Saliendo, hasta pronto')
        salir = True

salir = False
while not salir:
    opcion = mostrar_menu()
    salir = ejecutar_operacion(opcion, salir)
