# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 10. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
# (metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.

quilometros = float(input("Digite a velocidade em km/h: "))
metros = quilometros / 3.6
print(f"A velocidade digitada convertida em m/s é: {metros:.0f}")