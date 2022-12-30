# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 23. Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400
# ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996

ano = int(input("Digite o ano com 4 dígitos: "))
bissexto = ano % 100
if bissexto == 0:
    print("O ano não é bissexto")
else:
    print("O ano é bissexto")