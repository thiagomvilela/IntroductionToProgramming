# ADSPL.3: Introdução à Programação
# Docente: Rodrigo Cesar Lira da Silva
# Discente: Thiago da Mota Vilela (20211ADSPL0140)
# E-mail: tmv@discente.ifpe.edu.br
# Prova - Avaliação da 1ª Unidade - Data: 15 de junho de 2021
# 2ª Questão (2.5 pontos):

# O escrete de ouro da rádio jornal quer fazer uma enquete entre os seus ouvintes para saber qual o melhor jogador
# de futebol de cada partida transmitida. Para isto, faz-se necessário o desenvolvimento de um programa, que será
# utilizado pelas telefonistas da rádio, para a computação dos votos. Você foi contratado para desenvolver este programa
# utilizando a linguagem de programação Python. Para computar cada voto, a telefonista apenas digitará um número, entre
# 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi
# encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e
# voltando a pedir outro número. Após o final da votação, o programa deverá exibir (2.5 pontos):

# 1. O total de votos computados;
# 2. Os números e respectivos votos de todos os jogadores que receberam votos;
# 3. O percentual de votos de cada um destes jogadores;
# 4. Um texto final com o número do jogador escolhido como o melhor jogador da partida, com o número de votos e o
# percentual de votos dados a ele.

# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo
# número do jogador. O programa deve fazer uso de listas na sua execução. Abaixo segue uma tela de exemplo. A disposição
# das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do
# programa.

lista_jogadores = [" 1 - Marcos           	    ", " 2 - Cafú             	    ", " 3 - Lúcio            	    ", " 4 - Roque Júnior     	    ",
                   " 5 - Edmílson         	    ", " 6 - Roberto Carlos   	    ", " 7 - Ricardinho       	    ", " 8 - Gilberto Silva   	    ",
                   " 9 - Ronaldo          	    ", "10 - Rivaldo          	    ", "11 - Ronaldinho Gaúcho	    ", "12 - Dida             	    ",
                   "13 - Belletti         	    ", "14 - Anderson Polga   	    ", "15 - Kléberson        	    ", "16 - Júnior           	    ",
                   "17 - Denílson         	    ", "18 - Vampeta          	    ", "19 - Juninho Paulista 	    ", "20 - Edilson          	    ",
                   "21 - Luizão           	    ", "22 - Rogério Ceni     	    ", "23 - Kaká             	    "]

print("Bem-vindo(a) ao Escrete de Ouro da Rádio Jornal.\n"
      "Enquete: Quem foi o melhor jogador da partida?\n")

contador = 0
votos = -1
votos_qtde = [0]*23
votos_validos = 0

for k in range(len(lista_jogadores)):
    print(f"{lista_jogadores[k]}")
    contador += 1
print("")
while votos != 0:
    votos = int(input("Dentre as opções acima, digite um número entre 1 e 23 ou 0 para sair: "))
    if not (0 < votos < 24):
        print("\nOpção inválida, tente novamente.")
        continue
    if votos == 0:
        break
    votos_qtde[votos - 1] += 1
    votos_validos += 1

print(f"\nResultado da votação:\n"
      f"Foram computados {votos_validos} voto(s).\n")

maisvotado = 0
contador = 0

print("	Jogador	          Votos          %")
for k in range(len(lista_jogadores)):
    print(f"{lista_jogadores[contador]}{votos_qtde[contador]:.0f}{(votos_qtde[contador]/float(votos_validos)*100):15.2f}%")
    if votos_qtde[contador] > votos_qtde[maisvotado]:
        maisvotado = contador
    contador += 1

print(f"\nO melhor jogador da partida foi o número {lista_jogadores[maisvotado]}\n"
      f"com {votos_qtde[maisvotado]} votos, correspondendo a {(votos_qtde[maisvotado]/float(votos_validos)*100):.2f}% do total de votos.")