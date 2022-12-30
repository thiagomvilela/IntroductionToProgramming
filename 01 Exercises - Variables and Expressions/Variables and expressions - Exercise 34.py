# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 34. Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
# A área do círculo é Pi * raio², considere Pi = 3.141592.

raio = float(input("Digite o valor do raio de um círculo: "))
pi = 3.141592
area = pi * (raio ** 2)
print(f"A área do quadrado é de: {area:.2f}")