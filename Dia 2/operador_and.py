print('*** Operador Logico and ***')
condicion1 = False
condicion2 = True

# Aplicamos el operador and
resultado = condicion1 and condicion2
print(f'Resultado {condicion1} and {condicion2}: {resultado}')

# Ejemplo if else con operador and
llueve = False
nublado = False
print(f'\n*** Revisión del Clima ***')
if llueve and nublado:
    print('Llevar paraguas e impermeable, llueve y está nublado')
elif llueve:
    print('Llevar paraguas, va a llover')
elif nublado:
    print('Llevar impermeable, solo está nublado')
else:
    print('Dejar paraguas e impermeable')
