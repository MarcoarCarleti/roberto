# Desenvolva um algoritmo para calcular a área da esfera, dada por 4 Pi R2 e o seu volume, dado por (4 Pi R3)/3, onde R é o raio e Pi uma constante equivalente a 3,1416. O valor de R deverá ser fornecido pelo usuário. #

PI = 3.14

r = float(input("qual o valor de r? "))

a = (4 * PI * r**3) / 3

print("A área da esfera é: ", a)
