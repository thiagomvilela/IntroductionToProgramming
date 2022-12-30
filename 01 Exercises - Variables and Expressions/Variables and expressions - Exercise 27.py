# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 27. Leia um valor de área em hectares e apresente-o convertido em metros quadrados m2.
# A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.

hectares = float(input("Digite a área em hectares: "))
metros = hectares * 10000
print(f"O valor da área convertido em metros é: {metros:.2f} m²")