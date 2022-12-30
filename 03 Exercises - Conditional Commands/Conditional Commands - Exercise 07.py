# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 7. Faça um programa que receba dois números e mostre o maior.
# Se por acaso, os dois números forem iguais, imprima a mensagem Números iguais.

num1 = int(input("Digite o primeiro valor, número inteiro: "))
num2 = int(input("Digite o segundo valor, número inteiro: "))
if num1 > num2:
    print(f"O maior número digitado foi: {num1:.0f}")
elif num1 < num2:
    print(f"O maior número digitado foi: {num2:.0f}")
else:
    print("Os números são iguais")