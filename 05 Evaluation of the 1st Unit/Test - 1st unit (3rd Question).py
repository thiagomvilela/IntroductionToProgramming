# ADSPL.3: Introdução à Programação
# Docente: Rodrigo Cesar Lira da Silva
# Discente: Thiago da Mota Vilela (20211ADSPL0140)
# E-mail: tmv@discente.ifpe.edu.br
# Prova - Avaliação da 1ª Unidade - Data: 15 de junho de 2021
# 3ª Questão (2.5 pontos):

# Escreva um programa que simula uma bilheteria de cinema. O operador do programa (usuário do programa) pode deve
# realizar as seguintes operações (2,5 pontos):

# 1. Exibir a situação atual da sala de cinema.
# 2. Mudar o status de uma poltrona, sendo os status possíveis: ocupada, disponível e indisponível.
# 3. Impedir a utilização de uma coluna ou fila (linha) de cadeiras em uma única operação (status = indisponível).
# A operação será feita por questões de manutenção/distanciamento social.
# 4. Criar um relatório final de utilização da sala. Com a informação detalhada de cada cadeira e também um resumo
# de utilização (quantidade de cadeiras ocupadas, disponíveis, e indisponíveis, além da média de ocupação do cinema)

# No início é necessário que o operador informe a quantidade de filas (A,B,C.) e a quantidade de colunas (1,2,3…)
# que a sala do cinema possui. Essa sala deve iniciar sempre vazia.

import os
cadeiras_cinema = [["A01","A02","A03","A04","A05","A06","A07","A08","A09","A10","A11","A12","A13","A14","A15"],
                   ["B01","B02","B03","B04","B05","B06","B07","B08","B09","B10","B11","B12","B13","B14","B15"],
                   ["C01","C02","C03","C04","C05","C06","C07","C08","C09","C10","C11","C12","C13","C14","C15"],
                   ["D01","D02","D03","D04","D05","D06","D07","D08","D09","D10","D11","D12","D13","D14","D15"],
                   ["E01","E02","E03","E04","E05","E06","E07","E08","E09","E10","E11","E12","E13","E14","E15"],
                   ["F01","F02","F03","F04","F05","F06","F07","F08","F09","F10","F11","F12","F13","F14","F15"],
                   ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10","G11","G12","G13","G14","G15"],
                   ["H01","H02","H03","H04","H05","H06","H07","H08","H09","H10","H11","H12","H13","H14","H15"],
                   ["I01","I02","I03","I04","I05","I06","I07","I08","I09","I10","I11","I12","I13","I14","I15"],
                   ["J01","J02","J03","J04","J05","J06","J07","J08","J09","J10","J11","J12","J13","J14","J15"]]

print("Olá, seja bem-vindo(a) ao Cinemark Cinemas.\n")
# definir tamanho da sala de cinema (Máximo 10 x 15) - Conforme imagem da prova.
qtde_linha = 0
qtde_coluna = 0

contador = True
while contador == True:
    qtde_linha = int(input("Informe a quantidade de filas: (A,B,C...) (Capacidade Máxima: 10): "))
    if qtde_linha > 10 or qtde_linha <= -0:
        print("Você digitou um valor inválido, por favor tente novamente.\n")
        contador = True
    else:
        contador = False
print("")
contador = True
while contador == True:
    qtde_coluna = int(input("Informe a quantidade de colunas: (1,2,3...) (Capacidade Máxima: 15): "))
    if qtde_coluna > 15 or qtde_coluna <= 0:
        print("Você digitou um valor inválido, por favor tente novamente.\n")
        contador = True
    else:
        contador = False
os.system("cls")
print("")

# Definir cores dos lugares
for linha in range (qtde_linha): # percorrendo as linhas
    for coluna in range (qtde_coluna): # percorrendo as colunas
        if(coluna%2 == 0):
            cadeiras_cinema[linha][coluna] = '\033[32m'+ cadeiras_cinema[linha][coluna] +'\033[1;32m'
        else:
            cadeiras_cinema[linha][coluna] = '\033[90m'+ cadeiras_cinema[linha][coluna] +'\033[1;90m'

# Selecionando assentos:
while True:
    for linha in range (qtde_linha):
        for coluna in range (qtde_coluna):
            print(cadeiras_cinema[linha][coluna] + " ", end="")
        print("")

    print("\n\033[0m                   T     E     L     A\033[0;0m")
    print("Legenda:")
    print("\033[32mDisponível\033[1;32m")
    print("\033[31mOcupado\033[1;31m")
    print("\033[90mIndisponível\033[1;90m")
    print("\033[0;0m")

    escolhido = input("Selecione o assento, letra e número (exemplo: A01) ou digite (S) para sair: ").upper()
    if escolhido == "S":
        print("\nObrigado pela participação.\n")
        break

    contador = 0
    for linha in range (qtde_linha):
        for coluna in range (qtde_coluna):
            if escolhido in cadeiras_cinema[linha][coluna]:
                if not (coluna%2 == 0):
                    print(f"Você selecionou: {escolhido}, este assento está indisponível por questões de manutenção/distanciamento social.\n")
                    break
                else:
                    cadeiras_cinema[linha][coluna] = ""
                    cadeiras_cinema[linha][coluna] = '\033[31m'+ escolhido +'\033[1;31m'
                    contador = 1

qtde_disponiveis = 0
qtde_ocupadas = 0
qtde_indisponiveis = 0

for linha in range (qtde_linha):
    for coluna in range (qtde_coluna):
        valor = cadeiras_cinema[linha][coluna]
        if '1;32m' in valor:
            qtde_disponiveis += 1
        elif '1;31m' in valor:
            qtde_ocupadas += 1
        elif '1;90m' in valor:
            qtde_indisponiveis += 1

print("Relatório Final de Utilização da Sala:\n")

qtde_total_sala = qtde_linha * qtde_coluna
media_ocupacao = (qtde_ocupadas * 100) / qtde_total_sala   # considerando a quantidade total de cadeiras da sala.

print(f"Quantidade total de cadeiras da sala: {qtde_total_sala}")
print(f"Quantidade de cadeiras ocupadas: {qtde_ocupadas:.0f}")
print(f"Quantidade de cadeiras disponíveis: {qtde_disponiveis:.0f}")
print(f"Quantidade de cadeiras indisponíveis: {qtde_indisponiveis:.0f}")
print(f"Média de ocupação da sala do cinema: {media_ocupacao:.2f} %")

print("")