# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 18. Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo).
# O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando
# o resultado e saindo.

print("Menu com 4 opções de operações matemáticas:")
print("adição(+), subtração(-), multiplicação(*) e divisão(/)")
print("")
operacoes = input("Digite qual operação matemática você deseja utilizar: ").lower()
numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o primeiro valor: "))
if operacoes == "soma" or operacoes == "+":
    soma = numero1 + numero2
    print(f"Você escolheu a operação soma e o resultado é: {soma:.0f}")
elif operacoes == "subtracao" or operacoes == "subtração" or operacoes == "-":
    subtracao = numero1 - numero2
    print(f"Você escolheu a operação subtração e o resultado é: {subtracao:.0f}")
elif operacoes == "multiplicacao" or operacoes == "multiplicação" or operacoes == "*":
    multiplicacao = numero1 * numero2
    print(f"Você escolheu a operação multiplicação e o resultado é: {multiplicacao:.0f}")
elif operacoes == "divisao" or operacoes == "divisão" or operacoes == "/":
    divisao = numero1 / numero2
    print(f"Você escolheu a operação divisão e o resultado é: {divisao:.0f}")