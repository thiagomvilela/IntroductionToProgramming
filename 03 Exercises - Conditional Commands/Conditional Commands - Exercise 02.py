# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 2. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

num = float(input("Digite um número: "))
if num >= 0:
    raiz = num ** 0.5
    print(f"O número é positivo e sua raiz quadrada é: {raiz:.2f}")
else:
    print("Você digitou um número inválido!")