# Ejemplo de una variable global

x = 50

def hazAlgo():
    global x
    print('x es:', x)
    x = 2
    print('variable global x cambiada a:', x)


hazAlgo()

print('Valor de x ahora es:', x)