# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
# Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.

salario = float(input("Digite o valor de seu salário em R$: "))
prestacao = float(input("Digite o valor da prestação em R$: "))
if prestacao > (salario * 0.2):
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")