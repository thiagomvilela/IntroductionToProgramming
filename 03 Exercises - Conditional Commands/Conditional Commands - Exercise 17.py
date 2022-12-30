# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 17. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
# A = (basemaior + basemenor * altura) / 2

basemaior = float(input("Considerando o trapézio, digite o valor da base maior: "))
basemenor = float(input("Considerando o trapézio, digite o valor da base menor: "))
altura = float(input("Considerando o trapézio, digite o valor da altura: "))
area = (basemaior + basemenor * altura) / 2
print(f"A área do trapézio é: {area:.2f} m²")
