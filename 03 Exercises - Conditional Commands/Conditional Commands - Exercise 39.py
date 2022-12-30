# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 39. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o salário atual e
# o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente maior do
# que os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um
# bônus adicional de salário. Faça um programa que leia:

# o valor do salário atual do funcionário;
# o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).

# Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final
# reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

# Salário Atual             Reajuste(%)                 Tempo de Serviço                Bônus
# Até 500,00                    25%                     Abaixo de 1 ano               Sem bônus
# Até 1000,00                   20%                     De 1 a 3 anos                   100,00
# Até 1500,00                   15%                     De 4 a 6 anos                   200,00
# Até 2000,00                   10%                     De 7 a 10 anos                  300,00
# Acima de 2000,00          Sem reajuste                Mais de 10 anos                 500,00

print("")
salario = float(input("Digite o seu salário atual em R$: "))
tempo = int(input("Digite o tempo de serviço na empresa em anos: "))
if salario <= 500 and tempo < 1:
    reajuste = 1.25
    aumento = salario * reajuste
    print(f"O salário final com reajuste é de: R$ {aumento:.2f}")

elif salario <= 1000 and tempo >=1 and tempo <=3:
    reajuste = 1.20
    bonus = 100
    aumento = (salario * reajuste) + bonus
    print(f"O salário final com reajuste e bônus é de: R$ {aumento:.2f}")

elif salario <= 1500 and tempo >=4 and tempo <=6:
    reajuste = 1.15
    bonus = 200
    aumento = (salario * reajuste) + bonus
    print(f"O salário final com reajuste e bônus é de: R$ {aumento:.2f}")

elif salario <= 2000 and tempo >=7 and tempo <=10:
    reajuste = 1.10
    bonus = 300
    aumento = (salario * reajuste) + bonus
    print(f"O salário final com reajuste e bônus é de: R$ {aumento:.2f}")

elif salario > 2000 and tempo >10:
    bonus = 500
    aumento = salario + bonus
    print(f"O salário final sem reajuste e com bônus é de: R$ {aumento:.2f}")

else:
    print("Mensagem: Você não tem direito a nenhum aumento, nem bônus.")