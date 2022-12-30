# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 30. Faça um programa que receba três números e mostre-os em ordem crescente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 < num2 < num3:
    print(f"O números digitados em ordem crescente são: {num1}, {num2} e {num3}")
elif num1 < num3 < num2:
    print(f"O números digitados em ordem crescente são: {num1}, {num3} e {num2}")
elif num2 < num1 < num3:
    print(f"O números digitados em ordem crescente são: {num2}, {num1} e {num3}")
elif num2 < num3 < num1:
    print(f"O números digitados em ordem crescente são: {num2}, {num3} e {num1}")
elif num3 < num1 < num2:
    print(f"O números digitados em ordem crescente são: {num3}, {num1} e {num2}")
elif num3 < num2 < num1:
    print(f"O números digitados em ordem crescente são: {num3}, {num2} e {num1}")