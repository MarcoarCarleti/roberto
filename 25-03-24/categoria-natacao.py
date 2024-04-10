age = int(input("Insira a idade do participante: "))


if age >= 5 and age <= 7:
    print("Idade: ", age, " \nCategoria: Infantil A")
elif age >= 8 and age <= 10:
    print("Idade: ", age, " \nCategoria: Infantil B")
elif age >= 11 and age <= 13:
    print("Idade: ", age, " \nCategoria: Juvenil A")
elif age >= 14 and age <= 17:
    print("Idade: ", age, " \nCategoria: Juvenil B")
elif age >= 18:
    print("Idade: ", age, " \nCategoria: Adulto")
else:
    print(
        "Idade: Inválida  \nCategoria: Não existe uma categoria para menores de 5 anos"
    )
