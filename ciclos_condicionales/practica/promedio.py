calificaciones = { "matematicas": 9.0, "español": 8.0, "historia":9.0, "geografia": 10.0}

contador = 0
for materia in calificaciones:
    contador += calificaciones[materia]

print("promedio: %f" %(contador / len(calificaciones) ) )
print("menor promedio: %f" %( min(list(calificaciones.values()) ) ) )