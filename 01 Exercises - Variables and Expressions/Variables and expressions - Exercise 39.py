# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 39. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
# O primeiro ganhador receberá 46%; O segundo receberá 32%; O terceiro receberá o restante.
# Calcule e imprima a quantia ganha por cada um dos ganhadores.

premio = 780_000.00
primeiro = premio * 0.46
segundo = premio * 0.32
terceiro = premio - primeiro - segundo
print(f"A importância de R$ {premio:.2f} será dividida entre três ganhadores")
print(f"O primeiro ganhador receberá: R$ {primeiro:.2f}")
print(f"O segundo ganhador receberá:  R$ {segundo:.2f}")
print(f"O terceiro ganhador receberá: R$ {terceiro:.2f}")