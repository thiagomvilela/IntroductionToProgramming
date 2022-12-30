# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
# A fórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

Celsius = float(input("Digite a temperatura em Celsius: "))
print(f"Você digitou a temperatura de: {Celsius:.0f}º Celsius.")
Fahrenheit = Celsius * (9 / 5) + 32
print(f"A temperatura convertida é de: {Fahrenheit:.0f}º Fahrenheit.")