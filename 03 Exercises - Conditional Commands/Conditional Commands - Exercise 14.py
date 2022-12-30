# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 14. A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10,
# respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
# A média das três as notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2;
# Avaliação Semestral: 3 e Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado
# (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.

trabalho = float(input("Digite de 0 a 10 a sua nota do trabalho de laboratório: "))
avaliacao = float(input("Digite de 0 a 10 a sua nota da avaliação semestral: "))
exame = float(input("Digite de 0 a 10 a sua nota do exame final: "))
peso_trabalho = 2
peso_avaliacao = 3
peso_exame = 5
media = ((trabalho * peso_trabalho + avaliacao * peso_avaliacao + exame * peso_exame) / (peso_trabalho + peso_avaliacao + peso_exame))
if media <= 2.9:
    print(f"A sua média foi: {media:.1f} - Você foi reprovado.")
elif media > 3 and media <= 4.9:
    print(f"A sua média foi: {media:.1f} - Você fará a recuperação.")
else:
    print(f"A sua média foi: {media:.1f} - Você foi aprovado.")