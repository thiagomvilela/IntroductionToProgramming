# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 29. Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100.
# Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b,
# onde a e b são os números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas
# e as respostas corretas, além de quantas vezes o aluno acertou.
print("")
contador = 1
acertos = 0
erros = 0
while contador <= 5:
    import random
    a = random.randrange(1, 101)
    print(f"O primeiro número escolhido aleatoriamente foi: {a}")
    b = random.randrange(1, 101)
    print(f"O segundo número escolhido aleatoriamente foi: {b}")
    soma = a + b
    pergunta = int(input("Informe o valor da soma dos números apresentados: "))
    if pergunta != soma:
        erros += 1
        print(f"A resposta correta é {soma} - Você errou!")
        print("")
    elif pergunta == soma:
        acertos += 1
        print(f"A resposta correta é {soma} - Você acertou!")
        print("")
    contador += 1
percentual_acertos = (acertos * 100) / 5
percentual_erros = (erros * 100) / 5
print(f"O número de respostas certas é de:  {acertos} ({percentual_acertos:.0f} %)")
print(f"O número de respostas erradas é de: {erros} ({percentual_erros:.0f} %)")