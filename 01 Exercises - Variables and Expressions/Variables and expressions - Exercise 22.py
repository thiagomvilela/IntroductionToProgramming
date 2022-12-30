# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 22. Leia um valor de comprimento em jardas e apresente-o convertido em metros.
# A fórmula de conversão é: M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento em metros.

jardas = float(input("Digite o comprimento em jardas: "))
metros = 0.91 * jardas
print(f"O valor do comprimento convertido em metros é: {metros:.2f} m")