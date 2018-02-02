"""
upper
lower
capitalize
swapcase
title

isupper
islower
replace(valor1, valor2)
strip
"""

texto = "curso de python 3"

resultado = texto.lower()

print(resultado)

curso = "Python"
version = "3"

#resultado1 = "Curso de %s %s" %(curso, version)
resultado1 = "Curso d {a} {b}".format(a=curso, b=version)
print(resultado1)