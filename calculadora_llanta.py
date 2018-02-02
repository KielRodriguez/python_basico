"""
Descripcion: Calcula cuantas vueltas gira
una llanta en un kilometro dado que el diametro
es de 50 cm
"""

def rodada(kms):
    DIAMETRO = 50
    centimetros = kms * 1000 * 100
    return centimetros / DIAMETRO


print("La llanta giro", rodada(1), "veces") 