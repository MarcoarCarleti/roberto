firstValue = int(input("Insira o primeiro valor: "))
secondValue = int(input("Insira o segundo valor: "))
thirdValue = int(input("Insira o terceiro valor: "))

allValuesInCrescentOrder = []

if firstValue >= secondValue and secondValue >= thirdValue:
    allValuesInCrescentOrder.append(thirdValue)
    allValuesInCrescentOrder.append(secondValue)
    allValuesInCrescentOrder.append(firstValue)
    
elif secondValue >= firstValue and secondValue >= thirdValue:
    allValuesInCrescentOrder.append(thirdValue)
    allValuesInCrescentOrder.append(firstValue)
    allValuesInCrescentOrder.append(secondValue)
    
elif thirdValue >= firstValue and firstValue >= secondValue:
    allValuesInCrescentOrder.append(secondValue)
    allValuesInCrescentOrder.append(firstValue)
    allValuesInCrescentOrder.append(thirdValue)
    
elif thirdValue >= secondValue and secondValue >= firstValue:
    allValuesInCrescentOrder.append(firstValue)
    allValuesInCrescentOrder.append(secondValue)
    allValuesInCrescentOrder.append(thirdValue)
    
elif secondValue >= firstValue and firstValue <= thirdValue:
    allValuesInCrescentOrder.append(secondValue)
    allValuesInCrescentOrder.append(thirdValue)
    allValuesInCrescentOrder.append(firstValue)
    
# numbersArray = [firstValue, secondValue, thirdValue]

# allValuesInCrescentOrder = sorted(numbersArray)1

print(allValuesInCrescentOrder)
