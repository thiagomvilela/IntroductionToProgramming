# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 26. Leia um valor de área em metros quadrados m2 e apresente-o convertido em hectares.
# A fórmula de conversão é: H = M * 0.0001, sendo M a área em metros quadrados e H a área em hectares.

metros = float(input("Digite a área em m²: "))
hectares = metros * 0.0001
print(f"O valor da área convertido em hectares é: {hectares:.2f} ha")