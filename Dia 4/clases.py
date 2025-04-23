# Clase de contacto
class Contacto:
    def inicializar_contact(self, nombre, apellido, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email


    def mostrar_contacto(self):
        print(f'''Contacto:
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Telefono: {self.telefono}
            Email: {self.email}''')
        print(f'Dirección de Memoria self: {id(self)}')
        print(f'Dirección de Memoria Hexadecimal self: {hex(id(self))}')

# Codigo Principal
print('*** Clases y Objetos ***')

# Crear un primer objeto
contacto1 = Contacto()
contacto1.inicializar_contact('José', 'Gálvez', 123456789, 'galvez@mail.com')
contacto1.mostrar_contacto()
print(f'Dirección de Memoria: {id(contacto1)}')
print(f'Dirección de Memoria Hexadecimal: {hex(id(contacto1))}')

# Creamos un segundo objeto
contacto2 = Contacto()
contacto2.inicializar_contact('Carlos', 'Gomez', 987654321, 'carlos@mail.com')
contacto2.mostrar_contacto()
print(f'Dirección de Memoria: {id(contacto2)}')
print(f'Dirección de Memoria Hexadecimal: {hex(id(contacto2))}')