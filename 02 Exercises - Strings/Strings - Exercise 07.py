# Lista de Exercícios em Linguagem Python - Strings (UFU-FACOM)
# 7. Ler nome, sexo e idade. Se sexo for feminino e idade menor que 25, imprime o nome da pessoa e a palavra “ACEITA”,
# caso contrário imprimir “NÃO ACEITA”.

nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo: ").lower()
idade = int(input("Digite o seu idade: "))
if sexo == "feminino" and idade < 25:
    print(f"O seu nome é: {nome}")
    print("Sua condição é: ACEITA")
elif sexo == "feminino" and idade > 25:
    print("Sua condição é: NÃO ACEITA")
else:
    print("Sua condição é: ACEITA")