# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 31. Faça um programa que receba a altura e o peso de uma pessoa.
# De acordo com a tabela a seguir, verifique e mostra qual a classificação dessa pessoa.
# Altura                                        Peso
#                           Até 60      Entre 60 e 90 (Inclusive)       Acima de 90
# Menor que 1,20              A                    D                          G
# De 1,20 a 1,70              B                    E                          H
# Maior que 1,70              C                    F                          I

altura = int(input("Digite a sua altura em cm: "))
peso = int(input("Digite o seu peso em Kg: "))
altura_cm = altura / 100

if altura_cm < 1.20 and peso <= 60:
    print("Sua classifição é: A")
elif altura_cm < 1.20 and peso > 60 and peso < 90:
    print("Sua classifição é: D")
elif altura_cm < 1.20 and peso > 90:
    print("Sua classifição é: G")

elif altura_cm == 1.20 or altura_cm <= 1.70 and peso <= 60:
    print("Sua classifição é: B")
elif altura_cm == 1.20 or altura_cm <= 1.70 and peso > 60 and peso < 90:
    print("Sua classifição é: E")
elif altura_cm == 1.20 or altura_cm <= 1.70 and peso > 90:
    print("Sua classifição é: H")

elif altura_cm > 1.70 and peso <= 60:
    print("Sua classifição é: C")
elif altura_cm > 1.70 and peso > 60 and peso < 90:
    print("Sua classifição é: F")
elif altura_cm > 1.70 and peso > 90:
    print("Sua classifição é: I")