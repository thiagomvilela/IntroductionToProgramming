# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 13. Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova tem peso 1
# e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
# A nota para aprovação deve ser igual ou superior a 60 pontos.

nota1 = float(input("Digite a sua nota da primeira prova: "))
nota2 = float(input("Digite a sua nota da segunda prova: "))
nota3 = float(input("Digite a sua nota da terceira prova: "))
peso1 = 1 # nota 1
peso2 = 1 # nota 2
peso3 = 2 # nota 3

media = ((nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)) * 10
if media < 60:
    print(f"A sua média foi: {media:.0f} pontos: Você foi reprovado")
elif media >= 60:
    print(f"A sua média foi: {media:.0f} pontos: Você foi aprovado")