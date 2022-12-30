# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 21. Escreva o menu de opções abaixo. Leia a opções do usuário e execute a operação escolhida.
# Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
# 1- Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3- Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero).

print("Observe o menu de opções:")
print("1: Soma de 2 números")
print("2: Diferença entre 2 números (maior pelo menor)")
print("3: Produto entre 2 números")
print("4: Divisão entre 2 números (o denominador não pode ser zero)")
operacao = int(input("Digite de 1 a 4 a operação escolhida: "))
if operacao < 1 or operacao > 4:
    print("Erro: opção inválida!")
else:
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    if operacao == 1:
        soma = num1 + num2
        print(f"Opção 1: Soma de 2 números e o resultado é: {soma:.0f}")
    elif operacao == 2:
        if num1 > num2:
            diferenca1 = (num1 - num2)
            print(f"Opção 2: Diferença entre 2 números (maior pelo menor) e o resultado é: {diferenca1:.0f}")
        elif num2 > num1:
            diferenca2 = (num2- num1)
            print(f"Opção 2: Diferença entre 2 números (maior pelo menor) e o resultado é: {diferenca2:.0f}")
    elif operacao == 3:
        produto = num1 * num2
        print(f"Opção 3: Produto entre 2 números e o resultado é: {produto:.0f}")
    elif operacao == 4:
        if num2 == 0:
            print("O denominador não pode ser zero")
        elif num2 > 0:
            divisao = num1 / num2
            print(f"Opção 4: Divisão entre 2 números e o resultado é: {divisao:.0f}")