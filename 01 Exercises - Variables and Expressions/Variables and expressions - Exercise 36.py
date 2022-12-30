# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro
# circular ´e calculado por meio da seguinte fórmula: V = pi * raio² * altura, onde pi = 3.141592.

altura = float(input("Digite o valor da altura de um cilindro circular: "))
raio = float(input("Digite o valor do raio de um cilindro circular: "))
pi = 3.141592
volume = pi * (raio ** 2) * altura
print(f"A valor do volume do cilindro circular é de: {volume:.2f} m³")