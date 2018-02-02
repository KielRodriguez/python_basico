def suma(*args):
    total = 0
    for valor in args:
        total += valor

    return total



resultado = suma(10, 20, 30)
print(resultado)
