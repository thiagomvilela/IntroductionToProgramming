# ADSPL.3: Introdução à Programação
# Docente: Rodrigo Cesar Lira da Silva
# Discente: Thiago da Mota Vilela (20211ADSPL0140)
# E-mail: tmv@discente.ifpe.edu.br
# Prova - Avaliação da 1ª Unidade - Data: 15 de junho de 2021
# 4ª Questão (2.5 pontos) - Parte 1 (while)

# Quais são os diferentes tipos de laços de repetição presentes na linguagem Python?
# Informe, com exemplos de código, em quais situações eles são indicados. (2,5 pontos)

# Laço de repetição: while
# São utilizadas para executar a mesma parte de um programa várias vezes, normalmente dependendo de uma condição.

# Exemplo 1: é indicado para imprimir a contagem regressiva de lançamento de um foguete.
# O programa deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela.
print("Exemplo 1")
print("Lançamento do foguete ocorrerá em:")
contador = 10
while contador >= 0:
    print(contador)
    contador = contador - 1
print("Fogo!")

# Exemplo 2: É indicado para exibir os resultados de uma tabuada de multiplição, escolhendo o início e o fim.
print("\nExemplo 2")
n = int(input("Qual número você deseja saber a Tabuada de Multiplicação: "))
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
x = inicio
while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1

# Exemplo 3: É indicado para um programa que pergunte o depósito inicial e a taxa de juros de uma poupança,
# exibindo o valores mês a mês e o total ganho.
print("\nExemplo 3")
print("Depósito e Taxa de Juros - Redimento Anual")
depósito = float(input("Digite o valor do depósito inicial em R$: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
mês = 1
saldo = depósito
while mês <= 12:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Saldo do mês {mês} é de R$ {saldo:.2f}")
    mês = mês + 1
print(f"O ganho obtido com a taxa de juros de {taxa:.2f}% foi: R$ {saldo-depósito:.2f}")