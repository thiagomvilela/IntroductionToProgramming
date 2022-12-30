# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 45. Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
# Gere outro número formado pelos dígitos invertidos do número lido. Exemplo: NúmeroLido = 123; NúmeroGerado = 321

numero = int(input("Digite um número inteiro positivo de três dígitos (de 100 a 999): "))
if numero < 100 or numero > 999:
    print("Você digitou o número errado, tente novamente!")
else:
    numero = str(numero)
    print(f"O número gerado pelos dígitos invertidos é: {numero[2]}{numero[1]}{numero[0]}")

