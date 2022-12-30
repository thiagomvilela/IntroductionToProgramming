# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 19. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m3.
# A fórmula de conversão é: M = L / 1000 , sendo L o volume em litros e M o volume em metros cúbicos.

litros = float(input("Digite o volume em L: "))
print(f"Você digitou o volume de {litros:.2f} L")
cubicos = litros / 1000
print(f"O volume convertido em metros cúbicos é: {cubicos:.2f} m³")