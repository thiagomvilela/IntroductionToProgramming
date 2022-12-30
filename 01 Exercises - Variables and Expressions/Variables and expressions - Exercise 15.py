# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 15. Leia um ângulo em radianos e apresente-o convertido em graus.
# A fórmula de conversão é: G = R * 180/Pi, sendo G o ângulo em graus e R em radianos e Pi = 3.14.

radianos = float(input("Digite o ângulo em radianos: "))
pi = 3.14
graus = radianos * (180 / pi)
print(f"O ângulo digitado convertido em graus é: {graus:.2f}º")