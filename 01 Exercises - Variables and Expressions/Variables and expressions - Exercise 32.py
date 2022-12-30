# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 32. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.

numero = int(input("Digite um número inteiro: "))
sucessor = (numero * 3) + 1
antecessor = (numero * 2) - 1
print(f"O seu tripo é: {numero * 3:.0f}")
print(f"O seu dobro é: {numero * 2:.0f}")
print(f"O sucessor de seu tripo é: {sucessor:.0f}")
print(f"O antecessor de seu dobro é: {antecessor:.0f}")
print(f"A soma do sucessor de seu triplo com o antecessor de seu dobro: {(sucessor + antecessor):.0f}")

