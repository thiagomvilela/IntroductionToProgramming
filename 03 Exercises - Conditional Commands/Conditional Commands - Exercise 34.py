# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 34. Leia a nota e o número de faltas de um aluno, e escreva seu conceito.
# De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.

# NOTA                      CONCEITO (ATÉ 20 FALTAS)            CONCEITO (MAIS DE 20 FALTAS)
# 9.0 até 10.0                          A                                       B
# 7.5 até 8.9                           B                                       C
# 5.0 até 7.4                           C                                       D
# 4.0 até 4.9                           D                                       E
# 0.0 até 3.9                           E                                       E

print("")
nota = float(input("Digite a sua nota de 0 a 10: "))
if nota < 0 or nota > 10:
    print("Erro! Você digitou uma nota inválida")
else:
    faltas = int(input("Digite o numero de faltas: "))

    if nota == 0 or nota <= 3.39 and faltas <= 20:
        print("Sua classifição é: E")
    elif nota == 0 or nota <= 3.39 and faltas > 20:
        print("Sua classifição é: E")

    elif nota == 4 or nota <= 4.49 and faltas <= 20:
        print("Sua classifição é: D")
    elif nota == 4 or nota <= 4.49 and faltas > 20:
        print("Sua classifição é: E")

    elif nota == 5 or nota <= 7.4 and faltas <= 20:
        print("Sua classifição é: C")
    elif nota == 5 or nota <= 7.4 and faltas > 20:
        print("Sua classifição é: D")

    elif nota == 5 or nota <= 7.4 and faltas <= 20:
        print("Sua classifição é: C")
    elif nota == 5 or nota <= 7.4 and faltas > 20:
        print("Sua classifição é: D")

    elif nota == 7.5 or nota <= 8.9 and faltas <= 20:
        print("Sua classifição é: B")
    elif nota == 7.5 or nota <= 8.9 and faltas > 20:
        print("Sua classifição é: C")

    elif nota == 9 or nota <= 10 and faltas <= 20:
        print("Sua classifição é: A")
    elif nota == 9 or nota <= 10 and faltas > 20:
        print("Sua classifição é: B")