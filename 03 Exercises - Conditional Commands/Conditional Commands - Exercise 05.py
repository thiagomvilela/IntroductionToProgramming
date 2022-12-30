# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 5. Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.

num = int(input("Digite um número inteiro: "))
par = num % 2
if par == 0:
    print(f"O número digitado é: par")
else:
    print(f"O número digitado é: ímpar")


#

numero = int(input("Digite um número inteiro: "))
resultado = "par" if numero % 2 == 0 else "ímpar"
print(f"O número digitado é: {resultado}")

numero = int(input("Digite um número inteiro: "))
resultado = "par" if numero % 2 == 0 else "ímpar"
print(f"O número digitado é: {resultado}")