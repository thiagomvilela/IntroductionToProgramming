# Lista de Exercícios em Linguagem Python - Strings (UFU-FACOM)
# 4. Crie um programa que compara duas strings.

string1 = input("Digite a primeira String: ")
string2 = input("Digite a segunda String: ")

comparacao = string1 == string2
if comparacao == True:
    print(f"As duas strings digitadas são iguais")
else:
    print(f"As duas strings digitadas são diferentes")