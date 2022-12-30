# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 25. Calcule as raízes da equação de 2º grau. Lembrando que: x = (-b +- raiz ▲) 2a, onde ▲ = B² - 4ac
# E ax² + bx + c = 0 representa uma equação de 2º grau.
# A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem “Não é equação de segundo grau".
# Se ▲ < 0, não existe real. Imprima a mensagem Não existe raiz.
# Se ▲ = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única.
# Se ▲ >= 0, imprima as duas raízes reais.

a = int(input("Digite o valore da variável 'a': "))
if a == 0:
    print("Não é equação de segundo grau.")
else:
    b = int(input("Digite o valore da variável 'b': "))
    c = int(input("Digite o valore da variável 'c': "))
    delta = (b ** 2 - 4 * a * c)
    if delta < 0: # não existe real
        print("Não existe raiz")
    elif delta == 0: # existe uma raiz real
        raiz = (-b + delta ** 0.05) / 2 * a
        print(f"A raiz da equação de 2º é: {raiz} : Raiz única")
    elif delta >= 0: # duas raízes reais.
        raiz1 = (-b + delta ** 0.05) / 2 * a
        print(f"A raiz da equação de 2º é: {raiz1} : Primeira raiz")
        raiz2 = (-b - delta ** 0.05) / 2 * a
        print(f"A raiz da equação de 2º é: {raiz2} : Segunda raiz")