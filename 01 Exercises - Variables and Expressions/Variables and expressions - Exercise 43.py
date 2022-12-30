# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 43. Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# o total a pagar com desconto de 10%; o valor de cada parcela, no parcelamento de 3x sem juros;
# a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
# a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

total = float(input("Digite o valor total da compra em R$: "))
desconto = 0.10 * total
total_desconto = total - desconto
parcelado = total / 3
comissao_avista = 0.05 * total_desconto
comissao_parcelada = 0.05 * total
print(f"O total a pagar com desconto de 10% é de R$: {total_desconto:.2f}")
print(f"O valor de cada parcela, no parcelamento de 3x sem juros é de R$: {parcelado:.2f}")
print(f"A comissão do vendedor, para a venda a vista (5% sobre o valor com desconto) R$: {comissao_avista:.2f}")
print(f"A comissão do vendedor, para a venda parcelada (5% sobre o valor total) R$: {comissao_parcelada:.2f}")