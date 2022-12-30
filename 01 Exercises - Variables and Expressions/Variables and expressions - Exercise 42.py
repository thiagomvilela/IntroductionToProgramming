# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 42. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário
# tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.

salario_base = float(input("Digite o valor de seu salário base em R$: "))
gratificacao = 0.05 * salario_base
imposto = 0.07 * salario_base
salario = salario_base + gratificacao - imposto
print(f"O valor da gratificação de 5% sobre o salário base é de:   R$ {gratificacao:.2f}")
print(f"O valor do imposto de 7% sobre o salário base é de:        R$ {imposto:.2f}")
print(f"O valor do salário líquido a ser pago ao funcionário é de: R$ {salario:.2f}")