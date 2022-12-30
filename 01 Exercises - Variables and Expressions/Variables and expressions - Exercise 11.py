# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 11. Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
# (quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade em km/h e M em m/s.

metros = float(input("Digite a velocidade em m/s: "))
quilometros = metros * 3.6
print(f"A velocidade digitada convertida em km/h é: {quilometros:.0f}")