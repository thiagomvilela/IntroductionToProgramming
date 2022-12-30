# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 14. Leia um ângulo em graus e apresente-o convertido em radianos.
# A fórmula de conversão é: R = G * Pi/180, sendo G o ângulo em graus e R em radianos e Pi = 3.14.

graus = float(input("Digite o ângulo em graus: "))
pi = 3.14
radianos = graus * (pi / 180)
print(f"O ângulo digitado convertido em radianos é: {radianos:.2f}")