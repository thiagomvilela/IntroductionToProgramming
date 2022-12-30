# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 12. Leia uma distância em milhas e apresente-a convertida em quilômetros.
# A fórmula de conversão é: K = 1.61 * M, sendo K a distância em quilômetros e M em milhas.

milhas = float(input("Digite a distância em milhas: "))
quilometros = 1.61 * milhas
print(f"A distância digitada convertida em quilômetros é: {quilometros:.2f}")