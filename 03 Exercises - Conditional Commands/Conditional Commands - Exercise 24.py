# Lista de Exercícios em Linguagem Python - Comandos Condicionais (UFU-FACOM)
# 24. Uma empresa vende o mesmo produto para quatro diferentes estados.
# Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%).
# Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final
# do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.

estado = input("Digite seu estado (MG, SP, RJ ou MS): ").lower()
if estado != "mg" and estado != "sp" and estado != "rj" and estado != "ms":
    print("Erro! O estado digitado não é válido.")
else:
    valor = float(input("Digite o valor do produto em R$: "))
if estado == "mg":
    imposto = valor * 1.07
    print(f"O valor do seu produto com imposto (7%) é de: R$ {imposto:.2f}")
elif estado == "sp":
    imposto = valor * 1.12
    print(f"O valor do seu produto com imposto (12%) é de: R$ {imposto:.2f}")
elif estado == "rj":
    imposto = valor * 1.15
    print(f"O valor do seu produto com imposto (15%) é de: R$ {imposto:.2f}")
elif estado == "ms":
    imposto = valor * 1.08
    print(f"O valor do seu produto com imposto (8%) é de: R$ {imposto:.2f}")