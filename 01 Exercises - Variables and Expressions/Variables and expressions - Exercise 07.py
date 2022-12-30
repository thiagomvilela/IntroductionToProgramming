# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# A fórmula de conversão é: C = 5.0*(F-32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.

Fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
print(f"Você digitou a temperatura de: {Fahrenheit:.0f}º Fahrenheit.")
Celsius = 5 * (Fahrenheit - 32) / 9
print(f"A temperatura convertida é de: {Celsius:.0f}º Celsius.")