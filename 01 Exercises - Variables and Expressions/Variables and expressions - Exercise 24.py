# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 24. Leia um valor de área em metros quadrados m2 e apresente-o convertido em acres.
# A fórmula de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e A a área em acres.

metros = float(input("Digite a área em m²: "))
acres = metros * 0.000247
print(f"O valor da área convertido em acres é: {acres:.2f}")