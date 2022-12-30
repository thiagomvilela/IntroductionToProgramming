# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
# A fórmula de conversão é: C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

Kelvin = float(input("Digite a temperatura em Kelvin: "))
print(f"Você digitou a temperatura de: {Kelvin:.0f}º Kelvin.")
Celsius = Kelvin - 273.15
print(f"A temperatura convertida é de: {Celsius:.0f}º Celsius.")