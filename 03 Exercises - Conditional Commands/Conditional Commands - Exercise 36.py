# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 36. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor.
# Para calcular a comissão, considere a tabela abaixo:

# Venda mensal                                                          Comissão
# Maior ou igual a R$100.000,00                                 R$700,00 +16% das vendas
# Menor que R$100.000,00 e maior ou igual a R$80.000,00         R$650,00 +14% das vendas
# Menor que R$80.000,00 e maior ou igual a R$60.000,00          R$600,00 +14% das vendas
# Menor que R$60.000,00 e maior ou igual a R$40.000,00          R$550,00 +14% das vendas
# Menor que R$40.000,00 e maior ou igual a R$20.000,00          R$500,00 +14% das vendas
# Menor que R$20.000,00                                         R$400,00 +14% das vendas

print("")
venda = float(input("Digite o valor da sua venda em R$: "))
if venda >= 100_000.00:
    comissao = 700 + (venda * 16/100)
    print(f"O valor da comissão paga ao vendedor é de R$ {comissao:.2f}")

elif venda < 100_000.00 and venda >= 80_000.00:
    comissao = 650 + (venda * 14/100)
    print(f"O valor da comissão paga ao vendedor é de R$ {comissao:.2f}")

elif venda < 80_000.00 and venda >= 60_000.00:
    comissao = 600 + (venda * 14/100)
    print(f"O valor da comissão paga ao vendedor é de R$ {comissao:.2f}")

elif venda < 60_000.00 and venda >= 40_000.00:
    comissao = 550 + (venda * 14/100)
    print(f"O valor da comissão paga ao vendedor é de R$ {comissao:.2f}")

elif venda < 40_000.00 and venda >= 20_000.00:
    comissao = 500 + (venda * 14/100)
    print(f"O valor da comissão paga ao vendedor é de R$ {comissao:.2f}")

elif venda < 20_000.00:
    comissao = 400 + (venda * 14/100)
    print(f"O valor da comissão paga ao vendedor é de R$ {comissao:.2f}")