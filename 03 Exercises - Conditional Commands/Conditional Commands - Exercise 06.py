# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença
# existente entre ambos.

num1 = int(input("Digite o primeiro valor, número inteiro: "))
num2 = int(input("Digite o segundo valor, número inteiro: "))
if num1 > num2:
    print(f"O maior número digitado foi: {num1:.0f}")
    diferenca = num1 - num2
    print(f"A diferença entre eles é de: {diferenca:.0f}")
else:
    print(f"O maior número digitado foi: {num2:.0f}")
    subtracao = num2 - num1
    print(f"A diferença entre eles é de: {subtracao:.0f}")