# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 27. Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
# Categoria     Idade
# Infantil A    5 a 7
# Infantil B    8 a 10
# Juvenil A     11 a 13
# Juvenil B     14 a 17
# Sênior        maiores de 18 anos

idade = int(input("Digite a sua idade em anos: "))
if idade < 5:
    print("Não existe categoria para classificar nadadores com idade abaixo de 5 anos")
elif idade == 5 or idade <=7:
    print(f"Sua idade: {idade} anos e sua categoria é: Infantil A")
elif idade == 8 or idade <=10:
    print(f"Sua idade: {idade} anos e sua categoria é: Infantil B")
elif idade == 11 or idade <=13:
    print(f"Sua idade: {idade} anos e sua categoria é: Juvenil A")
elif idade == 14 or idade <=17:
    print(f"Sua idade: {idade} anos e sua categoria é: Juvenil B")
elif idade > 18:
    print(f"Sua idade: {idade} anos e sua categoria é: Sênior")