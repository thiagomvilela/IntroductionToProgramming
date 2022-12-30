# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 46. Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.

numero = int(input("Digite um número inteiro de 4 dígitos (de 1000 a 9999): "))
if numero < 1000 or numero > 9999:
    print("Você digitou o número errado, tente novamente!")
else:
    numero = str(numero)
    print(f"Digito: {numero[0]}")
    print(f"Digito: {numero[1]}")
    print(f"Digito: {numero[2]}")
    print(f"Digito: {numero[3]}")