# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 20. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem,
# se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
# O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
# Chama-se equilátero o triângulo que tem três lados iguais.
# Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
# Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

numA= float(input("Digite o valor do lado A: "))
numB= float(input("Digite o valor do lado B: "))
numC= float(input("Digite o valor do lado C: "))
if numA == numB == numC:
    print("O triângulo tem três lados iguais: equilátero")
elif numA == numB or numA == numC or numB == numC:
    print("O triângulo que tem o comprimento de dois lados iguais: isósceles")
elif numA != numB and numA != numC and numB != numC:
    print("O triângulo que tem os três lados diferentes: escaleno")