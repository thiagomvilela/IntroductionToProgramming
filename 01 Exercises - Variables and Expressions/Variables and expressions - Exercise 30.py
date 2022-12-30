# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 30. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.

real = float(input("Digite o valor em R$: "))
cotacao = float(input("Digite a cotação do dólar US$: "))
dolar = real / cotacao
print(f"O valor convertido em Dólar: {dolar:.2f} US$")