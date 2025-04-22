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
print('*** Maquina de snacks ***')
print('Snacks disponibles:')
for snack in snacks:
    print(f'\tId: {snack['id']} -> {snack['nombre']} - Precio: {snack['precio']}')


def comprar_snack():
    snack_elegido = input('¿Qué snack quieres (id)?: ')
    if snack_elegido == '0':
        print(f'Snack agregado: {snacks[0]}')
        ticket.append(snacks[0])
    if snack_elegido == '1':
        print(f'Snack agregado: {snacks[1]}')
        ticket.append(snacks[1])
    if snack_elegido == '2':
        print(f'Snack agregado: {snacks[2]}')
        ticket.append(snacks[2])


def mostrar_ticket():
    total = 0
    print('*** Ticket de Venta ***')
    for item in ticket:
        print(f'- {item['nombre']} - ${item['precio']}')
        total += item['precio']
    print(f'TOTAL -> ${total}')

while True:
    print('''Menú:
    1. Comprar snack
    2. Mostrar ticket
    3. Salir''')
    opcion = input('Escoge una opción: ')

    if opcion == '1':
        comprar_snack()
    elif opcion == '2':
        mostrar_ticket()
    elif opcion == '3':
        print('Saliendo, hasta pronto.')
        break
    else:
        print('Opción invalida.')



