# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 33. Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.

lado = float(input("Digite o tamanho do lado de um quadrado em metros: "))
area = (lado ** 2)
print(f"A área do quadrado é de: {area:.0f} m²")