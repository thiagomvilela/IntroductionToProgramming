# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.

salario = float(input("Digite o valor do salário em R$: "))
aumento = 1.25 * salario
print(f"O valor do seu salário com 25% de aumento é de: R$ {aumento:.2f}")