sin_parametros = lambda : True
con_valores = lambda val, val1=10, val2=10 : val + val1 + val2


con_asterisco = lambda *args : args[0]
con_doble_asterisco = lambda **kwargs : args[0]
con_asteriscos = lambda *args, **kwargs : kwargs.get('key', False)


print( sin_parametros())
print( con_valores(10, 20, 30 ))
print( con_asterisco( "Kiel", False) )
 