# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 12. Ler um número inteiro. Se o número lido for negativo, escreva a mensagem “Número inválido”.
# Se o número for positivo, calcular o logaritmo deste numero.

numero = int(input("Digite um número inteiro: "))
if numero < 0:
    print("Numéro inválido")
elif numero > 0:
    import math
    logaritmo = math.log10(numero)
    print(f"O logaritmo deste numero: {logaritmo:.0f}")