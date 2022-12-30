# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 20. Leia um valor de massa em quilogramas e apresente-o convertido em libras.
# A fórmula de conversão é: L = K / 0.45, sendo K a massa em quilogramas e L a massa em libras.

quilogramas = float(input("Digite o valor de massa em Kg: "))
libras = quilogramas / 0.45
print(f"O valor de massa convertido em libras é de: {libras:.2f} lb")