# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 10. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
# utilizando as seguintes fórmulas (onde 'h' corresponde 'a' à altura):
# Homens: (72.7 * h) - 58 e Mulheres: (62.1 * h) - 44.7

altura = float(input("Digite o valor de sua altura em cm: "))
sexo = (input("Digite o seu sexo: ")).lower()
if sexo == "masculino":
    peso_homem = (72.7 * altura/100) - 58
    print(f"O seu peso ideal é de: {peso_homem:.2f}")
elif sexo == "feminino":
    peso_mulher = (62.1 * altura/100) - 44.7
    print(f"O seu peso ideal é de: {peso_mulher:.2f}")