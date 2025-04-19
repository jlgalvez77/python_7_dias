print('*** Operador lógico or ***')
condicion1 = False
condicion2 = True
resultado = condicion1 or condicion2
print(f'El resultado de {condicion1} or {condicion2} es: {resultado}')

dia_descanso = True
vacaciones = False
if vacaciones or dia_descanso:
    print('Puede ir al partido.')
else:
    print('No puede ir al partido.')
