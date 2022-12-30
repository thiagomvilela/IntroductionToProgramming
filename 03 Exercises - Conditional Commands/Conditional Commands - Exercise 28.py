# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 28. Faça um programa que leia três números inteiros positivos e efetue
# o cálculo de uma das seguintes médias de acordo com um valor numérico digitado pelo usuário:
# (a) Geométrica: raiz cúbica de x * y * z
# (b) Ponderada: (x + 2 * y + 3 * z) / 6
# (c) Harmônica: (1) / (1 / x) + (1 / y) + (1 / z)
# (d) Aritmética: (x + y + z) / 3

x = int(input("Digite o primeiro número inteiro positivo: "))
if x < 0:
    print("Erro! Você precisa digitar um número maior que zero")
elif x >= 0:
    y = int(input("Digite o segundo número inteiro positivo: "))
    if y < 0:
        print("Erro! Você precisa digitar um número maior que zero")
    elif x >= 0 and y >= 0:
        z = int(input("Digite o terceiro número inteiro positivo: "))
        if z < 0:
            print("Erro! Você precisa digitar um número maior que zero")
        elif x >= 0 and y >= 0 and z >= 0:
            print("Médias disponíveis:")
            print("(a) Geométrica")
            print("(b) Ponderada")
            print("(c) Harmônica")
            print("(d) Aritmética")
            media = input("Digite qual média você deseja utilizar: a, b, c ou d: ").lower()
            if media != "a" and media != "b" and media != "c" and media != "d":
                print("Erro! Você precisa digitar: a, b, c ou d")
            elif media == "a":
                geometrica = (x * y * z) ** (1/3)
                print(f"O valor da média geométrica é: {geometrica:.2f}")
            elif media == "b":
                ponderada = (x + 2 * y + 3 * z) / 6
                print(f"O valor da média geométrica é: {ponderada:.2f}")
            elif media == "c":
                harmonica = (1) / ((1 / x) + (1 / y) + (1 / z))
                print(f"O valor da média geométrica é: {harmonica:.2f}")
            elif media == "d":
                aritmetica = (x + y + z) / 3
                print(f"O valor da média geométrica é: {aritmetica:.2f}")