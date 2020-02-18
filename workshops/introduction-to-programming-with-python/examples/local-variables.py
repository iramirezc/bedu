# Ejemplo de una variable local

x = 5

def hazAlgo(x):
  print('x es:', x)
  x = 10
  print('x ahora es:', x)

hazAlgo(x)

print('x sigue siendo:', x)
