class Usuario:
    pass

    def saluda(self, nombre):
        print("Hola, soy un usuario {}".format(nombre))

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)
    
    def crear_nombre(self, nombre):
        self.nombre = nombre


codi = Usuario()
codi.username = "codi"
codi.correo = "codigo@gmail.com"
facilito = Usuario()
facilito.username= "facilito"
facilito.correo = "facilito@gmail.com"

print( type(codi))
print( type(facilito))
codi.saluda("codi")
codi.crear_nombre("nuevo nombre")
codi.mostrar_nombre()
facilito.saluda("facilito")