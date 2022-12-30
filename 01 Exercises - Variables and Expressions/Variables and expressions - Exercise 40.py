# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 40. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados
# pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.

print("Uma empresa contrata um encanador a R$ 30,00 por dia")
dias = float(input("Digite o número de dias trabalhados pelo encanador: "))
valor = 30 * (1-0.08)
valor_liquido = dias * valor
print(f"A quantia líquida, já descontado o 8% do Imposto de Renda é de: R$ {valor_liquido:.2f}")