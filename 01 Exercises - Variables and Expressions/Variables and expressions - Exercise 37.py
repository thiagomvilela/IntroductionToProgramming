# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 37. Faça um programa que leia o valor de um produto e imprima o valor com desconto,
# tendo em vista que o desconto foi de 12%

valor = float(input("Digite o valor do produto em R$: "))
desconto = 0.12 * valor
preco = valor - desconto
print(f"A valor do produto com 12% de desconto é de: R$ {preco:.2f}")