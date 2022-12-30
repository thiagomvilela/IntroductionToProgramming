# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 25. Leia um valor de área em acres e apresente-o convertido em metros quadrados m2.
# A fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a área em acres.

acres = float(input("Digite a área em acres: "))
metros = acres * 4048.58
print(f"O valor da área convertido em m² é: {metros:.2f}")