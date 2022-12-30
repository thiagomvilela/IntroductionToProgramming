# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 26. Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso,
# calcule o consumo em Km=l e escreva uma mensagem de acordo com a tabela abaixo:
# CONSUMO       (Km/l)      Mensagem
# menor que     8           Venda o carro!
# entre         8 e 14      Econômico!
# maior que     14          Super econômico!

distancia = float(input("Digite a distância percorrida em Km: "))
litros = float(input("Digite o consumo em litros: "))
consumo = distancia / litros
if consumo < 8:
    print(f"O seu consumo é: {consumo} km/l - Venda o carro!")
elif consumo == 8 or consumo < 14:
    print(f"O seu consumo é: {consumo} km/l - Econômico!")
elif consumo > 14:
    print(f"O seu consumo é: {consumo} km/l - Super econômico!")
