# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 15. Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número.
# Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

numero = int(input("Digite um inteiro entre 1 e 7: "))
if numero == 1:
    print("O dia da semana é domingo")
elif numero == 2:
    print("O dia da semana é segunda")
elif numero == 3:
    print("O dia da semana é terça")
elif numero == 4:
    print("O dia da semana é quarta")
elif numero == 5:
    print("O dia da semana é quinta")
elif numero == 6:
    print("O dia da semana é sexta")
elif numero == 7:
    print("O dia da semana é sábado")
else:
    print("Você digitou um número inválido!")