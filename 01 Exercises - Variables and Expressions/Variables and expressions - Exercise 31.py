# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 31. Leia um número inteiro e imprima o seu antecessor e o seu sucessor.

numero = int(input("Digite um número inteiro: "))
antecessor = numero - 1
sucessor = numero + 1
print(f"O número antecessor é: {antecessor:.0f}")
print(f"O número sucessor é: {sucessor:.0f}")