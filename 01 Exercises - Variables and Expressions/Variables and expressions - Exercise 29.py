# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 29. Leia quatro notas, calcule a média aritmética e imprima o resultado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média aritmétrica das notas é: {media:.2f}")