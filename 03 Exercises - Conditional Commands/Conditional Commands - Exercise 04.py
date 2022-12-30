# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# O número digitado ao quadrado e a raiz quadrada do número digitado

numero = float(input("Digite um número: "))
if numero < 0:
    print("Você digitou um número inválido")
else:
    quadrado = numero ** 2
    print(f"O número digitado elevado ao quadrado é: {quadrado}")
    raiz = numero ** 0.5
    print(f"A raiz quadrada do número digitado é: {raiz}")
