year = int(input("Insira o ano em que você nasceu: "))
birthday = str(input("Você já fez aniversário (S / N)? ")).upper()

if birthday == "S":
  age = (2024 - year)
  print ("Sua idade: ", age)
  if age >= 16:
     print("Você já pode votar!")
  if age >= 18:
     print("Você já pode tirar carteira!")
     
elif birthday == "N":
  age = (2023 - year)
  print ("Sua idade: ", age)
  if age >= 16:
     print("Você já pode votar!")
  if age >= 18:
     print("Você já pode tirar carteira!")
