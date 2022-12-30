# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 52. Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),
# bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.

comprimento = float(input("Digite o comprimento do terreno em m: "))
largura = float(input("Digite o a largura do terreno em m: "))
preco_tela = float(input("Digite o preço do metro de tela em R$: "))

dimensao = (2 * comprimento) + (2 * largura)
custo = dimensao * preco_tela
print(f"O comprimento linear do terreno é de: {dimensao:.2f} m")
print(f"O custo para cercar este mesmo terreno com tela é de R$: {custo:.2f}")
