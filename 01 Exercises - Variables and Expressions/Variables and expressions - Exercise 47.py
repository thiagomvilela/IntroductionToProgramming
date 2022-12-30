# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 47. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

segundos = int(input("Digite um valor inteiro em segundos: "))
horas = segundos // 3600 # Pegar apenas a parte inteira (saber quantas horas)
resto = segundos % 3600 # Resto da divisão (segundos)
minutos = resto // 60
resto_segundos = resto % 60
print(f"O valor digitado corresponde a: {horas}h:{minutos}m:{resto_segundos}s")

# Problema Resolvido - Converter segundos em horas minutos segundos
# https://youtu.be/3DAVPyIauvA
