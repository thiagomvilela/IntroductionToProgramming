# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 41. Faca um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.
# Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.

valor = float(input("Digite o valor da hora de trabalho em R$: "))
horas = float(input("Digite o número de horas trabalhadas no mês: "))
salario = (valor * horas) * 1.10
print(f"O valor a ser pago ao funcionário, com acréscimo de 10% é de: R$ {salario:.2f}")