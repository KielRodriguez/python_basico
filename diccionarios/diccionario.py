diccionario = { }

diccionario["nombre"] = "Kiel"

valor = diccionario["nombre"]
not_found = diccionario.get("null", "default")
diccionario.setdefault("z", {})
print(diccionario)


values = diccionario.items()

print( values )
print( valor )
print( not_found )
print( diccionario["z"])
