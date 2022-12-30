# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 19. Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.

numero = int(input("Digite um número inteiro: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("O número digitado é divisível por 3 ou 5 simultaneamente")
elif numero % 3 == 0:
    print("O número digitado é divisível por 3")
elif numero % 5 == 0:
    print("O número digitado é divisível por 5")
else:
    print("O número digitado é não é divisível por 3 ou 5")
