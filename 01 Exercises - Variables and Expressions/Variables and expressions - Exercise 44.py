# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
# Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.

altura_degrau = float(input("Digite a altura do degrau de uma escada: "))
altura_escada = float(input("Digite a altura que você deseja alcançar subindo a escada: "))
degraus = altura_escada / altura_degrau
print(f"O número de degraus você deverá subir para atingir seu objetivo é de: {degraus:.0f}")