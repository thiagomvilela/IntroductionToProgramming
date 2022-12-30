# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 11. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos.
# Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1).
# Se o número lido não for maior do que zero, o programa terminará com a mensagem “Número inválido”.

numero = input("Digite um número inteiro: ")
if int(numero) < 0:
    print("Número inválido")
elif int(numero) > 0:
    soma = 0
    for digito in numero:
        soma += int(digito)
    print(f"a soma de todos os seus algarismos é {soma:.0f}")

# Ou pode ser resolvido da seguinte forma:

numero1 = input("Digite um número: ")
if int(numero1) < 0:
    print("Número inválido")
else:
    contador = 0
    soma1 = 0
    while contador < len(numero1):
        soma1 += int(numero1[contador])
        contador += 1
    print(f"a soma de todos os seus algarismos é {soma1:.0f}")