# Lista de Exercícios em Linguagem Python - Variáveis e Expressões (UFU-FACOM)
# 48. Faça um programa para leia o horário (hora, minuto e segundo) de inicio e a duração, em segundos, de uma
# experiência biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) do termino da mesma.

horas = int(input("Digite a hora: "))
minutos = int(input("Digite o minuto: "))
segundos = int(input("Digite o segundo: "))
print(f"O horário de início da experiência é: {horas}h:{minutos}m:{segundos}s")
duracao = int(input("Digite o tempo de duração, em segundos: "))

segundo_final = (segundos + duracao) % 60                      # resto dos segundos
minuto_final = (minutos + (segundos + duracao) // 60) % 60     # (segundos + duração) // 60  (parte inteira de segundos)
hora_final = (horas + (minutos + (segundos + duracao) // 60) // 60) % 24 # (minutos + (segundos + duracao) // 60) (parte inteira dos minutos)

print(f"O horário de término da experiência é: {hora_final}h:{minuto_final}m:{segundo_final}s")

















