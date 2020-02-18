# Función que retorna el
# número máximo de 2 números
# o si son iguales.

def max(num1, num2):
  if (num1 > num2):
    return num1
  elif (num2 > num1):
    return num2
  else:
    return 'numeros iguales'

print(max(3, 5))
print(max(10, 10))
print(max(100, 20))
