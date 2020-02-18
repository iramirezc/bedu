# Función que imprime el
# número máximo de 2 números
# o si son iguales.

# num1 y num2 son los parámetros
def max(num1, num2):
  if (num1 > num2):
    print(num1, 'es mayor que', num2)
  elif (num2 > num1):
    print(num2, 'es mayor que', num1)
  else:
    print(num1, 'es igual que', num2)

max(3, 5) # argumentos 3 y 5
max(10, 10) # argumentos 10 y 10
max(100, 20) # argumentos 100 y 20
