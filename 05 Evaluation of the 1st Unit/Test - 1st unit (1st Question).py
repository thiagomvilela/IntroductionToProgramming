0# ADSPL.3: Introdução à Programação
# Docente: Rodrigo Cesar Lira da Silva
# Discente: Thiago da Mota Vilela (20211ADSPL0140)
# E-mail: tmv@discente.ifpe.edu.br
# Prova - Avaliação da 1ª Unidade - Data: 15 de junho de 2021
# 1ª Questão (2.5 pontos):

# Faça um programa de perguntas e respostas em Python no estilo do show do milhão.
# Com os seguintes requisitos mínimos (2.5 pontos):

# Usar estrutura de repetição.
# Deve ter no mínimo cinco rodadas de perguntas com perguntas de múltiplas escolhas.
# O quantitativo de perguntas (banco de perguntas) deve ser no mínimo 2x a quantidade de rodadas.
# As perguntas devem ser sorteadas e não podem se repetir ao longo de um mesmo jogo
# A cada questão correta, o usuário deve ganhar 100 pontos.
# Se o usuário errar uma questão, ele deve finalizar o jogo.
# Ao final do jogo deve ser exibida a pontuação do jogador.

# Dicas:
# 1. Usar Dicionário/Lista para o banco de perguntas
# 2. Usar biblioteca random (randint, choice…) para sortear as perguntas.

import os
import random
banco_perguntas = ["Qual a capital do Brasil?\n 1 - São Paulo\n 2 - Rio de Janeiro\n 3 - Brasília\n",                        # Posição 0
                   "No futebol quem pode pegar a bola com as mãos?\n 1 - Goleiro\n 2 - Atacante\n 3 - Zagueiro\n",           # Posição 1
                   "Qual maior estado da região nordeste?\n 1 - Pernambuco \n 2 - Bahia\n 3 - Ceará\n",                      # Posição 2
                   "Em que país nasceu Carmem Miranda?\n 1 - Brasil\n 2 - Portugal\n 3 - Argentina\n",                       # Posição 3
                   "Qual é o coletivo de cães?\n 1 - Matilha\n 2 - Manada\n 3 - Alcateia\n",                                 # Posição 4
                   "Qual bicho trasmite Doença de Chagas?\n 1 - Abelha\n 2 - Pulga\n 3 - Barbeiro\n",                        # Posição 5
                   "Qual é o triângulo que tem todos os lados diferentes?\n 1 - Escaleno\n 2 - Isóceles\n 3 - Equilátero\n", # Posição 6
                   "Qual é o antônimo de malograr?\n 1 - Fracassar\n 2 - Conseguir\n 3 - Desprezar\n",                       # Posição 7
                   "O adjetivo venoso está relacionado a:\n 1 - Vela\n 2 - Vento\n 3 - Veia\n",                              # Posição 8
                   "Em que parte do corpo se encontra a epiglote?\n 1 - Boca\n 2 - Estômago\n 3 - Pâncreas\n",               # Posição 9
                   "A compensação por perda é chamada de:\n 1 - Déficit\n 2 - Indenização\n 3 - Indexãção\n"]                # Posição 10

respostas_corretas = [3, 1, 2, 2, 1, 3, 1, 2, 3, 1, 2] # [P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]

contador = 1
pontos = 0
rodada = 1
print("Bem-vindo(a) ao programa Show do Milhão.")
while contador <= 5:
    pergunta_sorteada = random.randint(0,len(banco_perguntas)-1)
    print(f"\n{rodada}ª Rodada:")
    print(banco_perguntas[pergunta_sorteada])
    resposta_usuario = int(input("Digite a alternativa correta: "))
    os.system("cls")
    if resposta_usuario == respostas_corretas[pergunta_sorteada]:
        pontos = pontos + 100
        print(f"Respostas corretas, você fez {pontos} pontos.")
        del banco_perguntas[pergunta_sorteada]
        del respostas_corretas[pergunta_sorteada]
        rodada = rodada + 1
        contador = contador + 1
    else:
        print(f"Resposta errada! Você está eliminado, sua pontuação foi de {pontos} ponto(s).")
        break