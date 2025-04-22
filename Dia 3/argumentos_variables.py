# *args -> arguments -> tupla
# **kwargs -> keyword arguments -> diccionario
def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args}. Más info: {kwargs}')
    # for superpoder in arg:
    #    print(f'Superpoder: {superpoddder}')


# Llamamos a la función
superheroe_superpoderes('Spiderman', 'Instinto Aracnido', edad=25, empresa='Marvel')
superheroe_superpoderes('IronMan', 'Armadura', 'Genio', 'Playboy', 'Millonario', edad=45)

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi Vecino')
