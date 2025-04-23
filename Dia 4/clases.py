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

# Codigo Principal
print('*** Clases y Objetos ***')

# Crear un primer objeto
contacto1 = Contacto()
contacto1.inicializar_contact('José', 'Gálvez', 123456789, 'galvez@mail.com')
contacto1.mostrar_contacto()