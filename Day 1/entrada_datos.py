# Entrada de Datos por consola: input()

mensaje = input('Ingresa un mensaje: ')
print(f'El mensaje recibido es: {mensaje}')

numero1 = input('¿Cual es tú primer número?: ')
numero2 = input('¿Cual es tú segundo número?: ')
# Se debe de hacer la conversión a entero para poder hacer la suma, si no lo que hace es una concatenación
resultado_suma = int(numero1) + int(numero2)
print(f'El resultado de la suma es: {resultado_suma}')
