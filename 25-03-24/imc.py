gender = input("Insira o seu gênero (H / M): ").upper()
height = float(input("Insira a sua altura (em m): "))

if gender == "H":
    imc = (72.7 * height) - 58
    print("Peso ideal: ", imc)
elif gender == "M":
    imc = (62.1 * height) - 44.7
    print("Peso ideal: ", imc)

# h: (72,7 * altura) - 58
# m: (62,1 * altura) - 44,7