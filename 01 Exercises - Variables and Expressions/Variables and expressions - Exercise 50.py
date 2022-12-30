# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 50. Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0,0).

x = float(input("Digite a coordenada x de ponto no R²: "))
y = float(input("Digite a coordenada y de ponto no R²: "))
distancia = (x ** 2) + (y ** 2) ** 0.05 # Cálculo da Hipotenusa
print(f"A distância da origem (0,0) é de: {distancia:.2f}")
















