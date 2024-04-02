tagPrice = float(input("Insira o valor do produto: "))

paymentMethod = int(input("Insira o método de pagamento: "))

money = paymentMethod == 1

creditCard = paymentMethod == 2

threeTimes = paymentMethod == 3

fourTimes = paymentMethod == 4

if money:
    value = tagPrice - (tagPrice * 0.1)
    print("Valor: ", value)
elif creditCard:
    value = tagPrice - (tagPrice * 0.05)
    print("Valor: ", value)
elif threeTimes:
    print("Valor: ", tagPrice)
elif fourTimes:
    value = tagPrice + (tagPrice / 10) 
    print("Valor: ", value)
else:
    print("Insira  um método válido! ")