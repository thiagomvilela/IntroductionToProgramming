# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
# hipotenusa = raiz quadrada de a² + b². Faça um programa que receba os valores de a e b
# e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação.

cateto_a = float(input("Digite o valor do cateto A do triângulo: "))
cateto_b = float(input("Digite o valor do cateto B do triângulo: "))
hipotenusa = ((cateto_a **2) + (cateto_b ** 2)) ** 0.5
print(f"A valor da hipotenusa do triângulo é de: {hipotenusa:.2f}")

# Raiz quadrada de numero é = ele elevado a 0.5