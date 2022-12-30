# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 32. Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade.
# O programa deve calcular o valor a ser pago por aquele lanche.
# Considere que a cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão abaixo:
# Especificação     Código      Preço
# Cachorro Quente   100         1.20
# Bauru Simples     101         1.30
# Bauru com Ovo     102         1.50
# Hamburguer        103         1.20
# Cheeseburguer     104         1.70
# Suco              105         2.20
# Refrigerante      106         1.00

print("Cardápio da Lanchonete")
print("")
print("Código   Especificação       Preço")
print("100      Cachorro Quente     R$ 1.20")
print("101      Bauru Simples       R$ 1.30")
print("102      Bauru com Ovo       R$ 1.50")
print("103      Hamburguer          R$ 1.20")
print("104      Cheeseburguer       R$ 1.70")
print("105      Suco                R$ 2.20")
print("105      Refrigerante        R$ 1.00")
print("")
cachorro_quente = 1.20
bauru_simples = 1.30
bauru_ovo = 1.5
hamburguer = 1.20
cheeseburguer = 1.70
suco = 2.20
refrigerante = 1.00

codigo = int(input("Digite o código do item escolhido: "))
quantidade = int(input("Digite a quantidade do item escolhido: "))

if codigo == 100:
    valor = cachorro_quente * quantidade
elif codigo == 101:
    valor = bauru_simples * quantidade
elif codigo == 102:
    valor = bauru_ovo * quantidade
elif codigo == 103:
    valor = hamburguer * quantidade
elif codigo == 104:
    valor = cheeseburguer * quantidade
elif codigo == 105:
    valor= suco * quantidade
elif codigo == 106:
    valor = refrigerante * quantidade
print(f"O total do seu pedido é: R$ {valor:.2f}")