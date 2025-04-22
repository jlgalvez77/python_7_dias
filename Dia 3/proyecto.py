print('*** Maquina de snacks ***')

snacks = [
    {'id': 0,
     'nombre': 'Patatas',
     'precio': 300},
    {'id': 1,
     'nombre': 'Refresco',
     'precio': 50},
    {'id': 2,
     'nombre': 'Sandwich',
     'precio': 120}
]

ticket = []

while True:
    print('''Menú:
    1. Comprar snack
    2. Mostrar ticket
    3. Salir''')
    opcion = input('Escoge una opción: ')

    if opcion == '1':
        pass
    if opcion == '2':
        pass
    if opcion == '3':
        print('Saliendo, hasta pronto.')
        break


    def comprar_snack():
        snack_elegido = input('¿Qué snack quieres (id)?')


    def mostrar_ticket():
        pass
