# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 33. Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo,
# e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela).
# PREÇO ANTIGO            PERCENTUAL DE AUMENTO
# atÉ R$ 50                        5%
# entre R$ 50 e R$ 100            10%
# acima de R$ 100                 15%

antigo = float(input("Digite o preço antigo do produto em R$: "))
if antigo <= 50:
    preco = antigo * 1.05
elif antigo == 50 or antigo <= 100:
    preco = antigo * 1.10
elif antigo > 100:
    preco = antigo * 1.15
print(f"O preço do seu produto com reajuste é de: R$ {preco:.2f}")