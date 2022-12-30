# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
# A fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

Celsius = float(input("Digite a temperatura em Kelvin: "))
print(f"Você digitou a temperatura de: {Celsius:.0f}º Celsius.")
Kelvin = Celsius + 273.15
print(f"A temperatura convertida é de: {Kelvin:.0f}º Kelvin.")