# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 51. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada
# deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio,
# e imprima quanto cada um ganharia do prêmio com base no valor investido.

premio = float(input("Digite o valor do prêmio em R$: "))
apostador1 = float(input("Digite o valor do apostador 1 em R$: "))
apostador2 = float(input("Digite o valor do apostador 2 em R$: "))
apostador3 = float(input("Digite o valor do apostador 3 em R$: "))

total = apostador1 + apostador2 + apostador3

percentual1 = (apostador1 * 100) / total
percentual2 = (apostador2 * 100) / total
percentual3 = (apostador3 * 100) / total

premio1 = premio * (percentual1 / 100)
premio2 = premio * (percentual2 / 100)
premio3 = premio * (percentual3 / 100)

print(f"O apostador 1 receberá {percentual1:.2f} % do prêmio, o equivalente em R$: {premio1:.2f}")
print(f"O apostador 2 receberá {percentual2:.2f} % do prêmio, o equivalente em R$: {premio2:.2f}")
print(f"O apostador 3 receberá {percentual3:.2f} % do prêmio, o equivalente em R$: {premio3:.2f}")















