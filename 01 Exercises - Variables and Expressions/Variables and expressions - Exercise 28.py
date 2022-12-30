# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 28. Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))
soma = (num1**2) + (num2**2) + (num3**2)
print(f"O valor da soma dos quadrados dos valores digitados é: {soma:.2f}")