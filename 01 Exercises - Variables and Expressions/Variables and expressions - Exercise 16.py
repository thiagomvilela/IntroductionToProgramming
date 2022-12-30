# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 16. Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
# A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.

polegadas = float(input("Digite o comprimento em polegadas: "))
centimetros = polegadas * 2.54
print(f"O comprimento convertido em centímetros: {centimetros:.2f} cm")