# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 23. Leia um valor de comprimento em metros e apresente-o convertido em jardas.
# A fórmula de conversão é: J = M 0 / 0.91 , sendo J o comprimento em jardas e M o comprimento em metros.

metros = float(input("Digite o comprimento em metros: "))
jardas = metros / 0.91
print(f"O valor do comprimento convertido em jardas é: {jardas:.2f} yd'")