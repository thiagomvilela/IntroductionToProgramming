# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 3. Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o número ao quadrado.

num = float(input("Digite um número real: "))
if num >= 0:
    raiz = num ** 0.5
    print(f"O número é positivo e sua raiz quadrada é: {raiz:.2f}")
else:
    quadrado = num ** 2
    print(f"O número é negativo e o mesmo elevado ao quadrado é: {quadrado}")