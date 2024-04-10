from math import sqrt


firstValue = float(input("Valor de a: "))
secondValue = float(input("Valor de b: "))
thirdValue = float(input("Valor de c: "))
x = float(input("Valor de x: "))

totalValue = (firstValue * x**2) + (secondValue * x) + thirdValue

print("Resultado da equação: ", totalValue)
print("Raiz quadrada do resultado da equação: ", sqrt(totalValue))
