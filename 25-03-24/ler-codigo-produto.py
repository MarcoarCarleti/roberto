code = int(input("Insira o código do produto: "))

if code == 1:
    print("Código: ", code, " \nClassificação: Alimento não perecível")
elif code >= 2 and code <= 4:
    print("Código: ", code, " \nClassificação: Alimento perecível")
elif code == 5 or code == 6:
    print("Código: ", code, " \nClassificação: Vestuário")
elif code == 7:
    print("Código: ", code, " \nClassificação: Higiene Pessoal")
elif code >= 8 and code <= 15:
    print("Código: ", code, " \nClassificação: Higiene Pessoal")
else:
    print("Código: Não encontrado  \nClassificação: Não Encontrado")
