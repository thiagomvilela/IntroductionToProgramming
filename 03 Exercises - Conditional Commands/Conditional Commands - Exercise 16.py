# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 16. Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este numero. Isto é,
# janeiro se 1, fevereiro se 2, e assim por diante.

numero = int(input("Digite um inteiro entre 1 e 12: "))
if numero == 1:
    print("O mês correspondente a este numero é: janeiro")
elif numero == 2:
    print("O mês correspondente a este numero é: fevereiro")
elif numero == 3:
    print("O mês correspondente a este numero é: março")
elif numero == 4:
    print("O mês correspondente a este numero é: abril")
elif numero == 5:
    print("O mês correspondente a este numero é: maio")
elif numero == 6:
    print("O mês correspondente a este numero é: junho")
elif numero == 7:
    print("O mês correspondente a este numero é: julho")
elif numero == 8:
    print("O mês correspondente a este numero é: agosto")
elif numero == 9:
    print("O mês correspondente a este numero é: setembro")
elif numero == 10:
    print("O mês correspondente a este numero é: outubro")
elif numero == 11:
    print("O mês correspondente a este numero é: novembro")
elif numero == 12:
    print("O mês correspondente a este numero é: dezembro")
else:
    print("Você digitou um número inválido!")