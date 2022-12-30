# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 13. Leia uma distância em quilômetros e apresente-a convertida em milhas.
# A fórmula de conversão é: M = K / 1.61, sendo K a distância em quilômetros e M em milhas.

quilometros = float(input("Digite a distância em quilômetros: "))
milhas = quilometros / 1.61
print(f"A distância digitada convertida em milhas é: {milhas:.2f}")