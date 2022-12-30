# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 21. Leia um valor de massa em libras e apresente-o convertido em quilogramas.
# A fórmula de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.

libras = float(input("Digite o valor de massa em lb: "))
quilogramas = libras * 0.45
print(f"O valor de massa convertido em quilogramas é de: {quilogramas:.2f} Kg")