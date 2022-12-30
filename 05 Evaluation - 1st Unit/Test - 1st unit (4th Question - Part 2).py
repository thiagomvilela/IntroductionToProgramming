# ADSPL.3: Introdução à Programação
# Docente: Rodrigo Cesar Lira da Silva
# Discente: Thiago da Mota Vilela (20211ADSPL0140)
# E-mail: tmv@discente.ifpe.edu.br
# Prova - Avaliação da 1ª Unidade - Data: 15 de junho de 2021
# 4ª Questão (2.5 pontos) - Parte 2 (for)

# Quais são os diferentes tipos de laços de repetição presentes na linguagem Python?
# Informe, com exemplos de código, em quais situações eles são indicados. (2,5 pontos)

# Laço de repetição: for
# É uma estrutura simples e compacta para percorrer todos elementos das coleções ou estruturas que contenham listas de objetos.

# Exemplo 1 : Imprimir todos os itens de uma lista.
print("Exemplo 1")
print("Percorrer a lista 'nome' e exibir seu conteúdo:")
nome = ["Thiago", "da Mota", "Vilela"]
for valor in nome:
    print(valor)

# Exemplo 2: Pode ser utilizado para verificar se um item consta na lista, conforme exemplo a seguir.
print("\nExemplo 2")
numeros = [7, 9, 10, 12]
p = int(input("Digite um número a pesquisar na lista 'números': "))
for e in numeros:
    if e == p:
        print("Elemento encontrado!")
        break
else:
    print("Elemento não encontrado!")

# Exemplo 3: Inserir números em uma lista ainda sem tamanho definido, quando finalizar imprimir os itens da lista.
print("\nExemplo 3")
print("Inserir números em uma lista ainda sem tamanho definido")
lista = []
while True:
    numero = int(input("Digite um número ou '0' para sair: "))
    if numero == 0:
        break
    lista.append(numero)
for c in lista: # Após o break ('0'), utiliza-se o for para percorrer os números adicionados na 'lista'.)
    print(c)
# O primeiro while não pôde ser convertido em for porque o número de repetições é desconhecido no início.