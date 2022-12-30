# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 18. Leia um valor de volume em metros cúbicos m3 e apresente-o convertido em litros.
# A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em metros cubicos.

cubicos = float(input("Digite o volume em m³: "))
print(f"Você digitou o volume de {cubicos:.2f} m³")
litros = cubicos * 1000
print(f"O volume convertido em Litros é: {litros:.2f} L")