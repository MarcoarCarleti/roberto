firstValue = float(input("Insira o primeiro número: "))
secondValue = float(input("Insira o segundo número: "))

operator = int(input('''1 - Adição
2 - Subtração
3 - Divisão 
4 - Multiplicação

'''))

addition = operator == 1

subtraction = operator == 2

division = operator == 3

multiplication = operator == 4

if addition: 
    totalValue = firstValue + secondValue
    print("Total: ", totalValue)
elif subtraction:
    totalValue = firstValue - secondValue
    print("Total: ", totalValue)
elif division:
    totalValue = firstValue / secondValue
    print("Total: ", totalValue)
elif multiplication: 
    totalValue = firstValue * secondValue
    print("Total: ", totalValue)
else:
    print("Insira uma operação válida")


