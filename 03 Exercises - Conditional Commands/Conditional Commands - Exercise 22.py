# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 22. Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
# As condições para aposentadoria são:
# Ter pelo menos 65 anos,
# Ou ter trabalhado pelo menos 30 anos,
# Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Digite sua idade em anos: "))
tempo = int(input("Digite o tempo de serviço em anos: "))
if idade >= 65:
    print("O status de sua aposentadoria é: concedida")
elif tempo >= 30:
    print("O status de sua aposentadoria é: concedida")
elif idade >= 60 and tempo >= 25:
    print("O status de sua aposentadoria é: concedida")
else:
    print("O status de sua aposentadoria é: não concedida")