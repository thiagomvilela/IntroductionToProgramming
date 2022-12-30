# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 40. O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos.
# A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo.
# Leia o custo de fábrica e escreva o custo ao consumidor.

# CUSTO DE FÁBRICA                    % DO DISTRIBUIDOR              % DOS IMPOSTOS
# até R$12.000,00                            5                           isento
# entre R$12.000,01 e 25.000,00             10                            15
# acima de R$25.000,00                      15                            20

print("")

fabrica = float(input("Digite o custo de fábrica do seu carro novo em R$: "))
if fabrica < 12000.00:
    distribuidor = 1.05
    consumidor = fabrica * distribuidor
    print(f"O preço final do seu veículo é de R$ {consumidor:.2f}")
elif fabrica >= 12000.00 and fabrica <= 25000.00:
    distribuidor = 10/100
    imposto = 15/100
    consumidor = fabrica + (fabrica * distribuidor) + (fabrica * imposto)
    print(f"O preço final do seu veículo é de R$ {consumidor:.2f}")
elif fabrica > 25000.00:
    distribuidor = 15/100
    imposto = 20/100
    consumidor = fabrica + (fabrica * distribuidor) + (fabrica * imposto)
    print(f"O preço final do seu veículo é de R$ {consumidor:.2f}")
