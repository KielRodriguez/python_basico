def crear_usuario(nombre='', apellido='', edad=10):
    return {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': "{} {}".format(nombre, apellido),
        'edad': edad
    }

usuario = crear_usuario("Kiel", "Rodriguez", 28)

print(usuario['nombre'])
print(usuario['apellido'])
print(usuario['edad'])