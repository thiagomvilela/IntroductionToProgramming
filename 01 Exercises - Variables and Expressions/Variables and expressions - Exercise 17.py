# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 17. Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
# A fórmula de conversão é: P = C / 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.

centimetros = float(input("Digite o comprimento em centímetros: "))
polegadas = centimetros / 2.54
print(f'O comprimento convertido em polegadas: {polegadas:.2f}"')