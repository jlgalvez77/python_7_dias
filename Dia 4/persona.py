class Persona:
    # Constructor
    def __init__(self, nombre, apellido):
        self._nombre = nombre   # Atributo protegido
        self.__apellido = apellido  # Atributo privado

    def mostrar_persona(self):
        print(f'Persona: nombre = {self._nombre}, apellido = {self.__apellido}')

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido



# Codigo Principal
persona1 = Persona('José', 'Gálvez')
#persona1.mostrar_persona()
# Lectura de los Atributos
print(persona1.get_nombre())
print(persona1.get_apellido())

# Modificar los valores de los atributos
persona1.set_nombre('Jose2')
persona1.set_apellido('Galvez2')

# Accedemos a los atributos directamente (publicos)
#persona1.nombre = 'Juan'
#print(persona1._nombre) # Esto no es buena practica
#print(persona1.__apellido) # No podemos acceder al atributo privado
#persona1.apellido = 'Perez'
#persona1.mostrar_persona()