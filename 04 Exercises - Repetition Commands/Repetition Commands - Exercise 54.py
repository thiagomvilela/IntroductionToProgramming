# Lista de Exercícios em Linguagem Python - Comandos de Repetição (UFU-FACOM)
# 54. Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não.

print("")
import os
print("Número primo é aquele que é divisível apenas por um e por ele mesmo.")
numero = int(input("Digite um número inteiro maior que 1: "))
contador = 0
while contador < 1:
    if numero <= 1:
        print("Erro! Você digitou um número inválido, tente novamente")
        numero = int(input("Digite um número inteiro maior que 1: "))
        contador += 0
        os.system("cls")
    elif numero > 1:
        break
contador_resto = 0
for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        contador_resto += 1
if contador_resto == 2:
    print(f"O número {numero} é divisível apenas por 1 ou {numero}, sendo assim é número primo.")
else:
    print(f"O número {numero} é divisível por {contador_resto} números, sendo assim NÃO é número primo.")