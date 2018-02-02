lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"

separador = "; "

resultado = lenguajes.split( separador )

nuevo_string = separador.join( resultado )

texto = """Este es un texto
con
saltos
de

línea"""

print( resultado )
print( nuevo_string )
print( texto.splitlines() )    