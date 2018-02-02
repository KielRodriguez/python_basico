def crear_mensaje(nombre):
    return "Hola {}, bienvenido al curso de python 3".format(nombre)

def suma(valor1, valor2, valor3):
    return valor1 + valor2 + valor3

def obtener_curso():
    return "Curso de python", "Basico", 3.6


nuevo_mensaje = crear_mensaje("Kiel")
print(nuevo_mensaje)

resultado = suma(10, 20, 30)
print(resultado)

curso, nivel, calificacion = obtener_curso()

print(curso)
print(nivel)
print(calificacion)