# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 41. Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:

# IMC                   Classificação
# < 18,5                Abaixo do Peso
# 18,6 - 24,9           Saudável
# 25,0 - 29,9           Peso em excesso
# 30,0 - 34,9           Obesidade Grau I
# 35,0 - 39,9           Obesidade Grau II(severa)
# >= 40,0               Obesidade Grau III(mórbida)

print("")
peso = float(input("Digite o seu peso em kg: "))
altura = int(input("Digite a sua altura em cm: "))
altura_m = altura / 100
imc = peso / (altura_m **2)
if imc < 18.5:
    print(f"O seu IMC é de {imc:.1f} e sua classificação é: Abaixo do peso")
elif imc >= 18.6 and imc <= 24.9:
    print(f"O seu IMC é de {imc:.1f} e sua classificação é: Saudável")
elif imc >= 25 and imc <= 29.9:
    print(f"O seu IMC é de {imc:.1f} e sua classificação é: Peso em excesso")
elif imc >= 30 and imc <= 34.9:
    print(f"O seu IMC é de {imc:.1f} e sua classificação é: Obesidade Grau I")
elif imc >= 35 and imc <= 39.9:
    print(f"O seu IMC é de {imc:.1f} e sua classificação é: Obesidade Grau II(severa)")
elif imc >= 40:
    print(f"O seu IMC é de {imc:.1f} e sua classificação é: Obesidade Grau III(mórbida)")
