# Lista de Exercícios em Linguagem Python - Strings (UFU-FACOM)
# 3. Faça um programa para converter uma letra maiúscula em letra minúscula.
#  Use a tabela ASCII para resolver o problema.

maiuscula = (input("Digite uma letra maiúscula: "))
conversao = ord(maiuscula) + 32
convertida = chr(conversao)
print(f"A letra maiúscula convertida em minúscula é: {convertida}")

minuscula = (input("Digite uma letra minuscula: "))
conversao_1 = ord(minuscula) - 32
convertida_1 = chr(conversao_1)
print(f"A letra minúscula convertida em maiúscula é: {convertida_1}")

# Cada letra corresponde a um número,
# a diferença entre maiúscula e minúscula é 32.

# Tabela ASCII
# A = 65	a = 97
# B = 66	b = 98
# C = 67	c = 99
# D = 68	d = 100
# E = 69	e = 101
# F = 70	f = 102
# G = 71	g = 103
# H = 72	h = 104
# I = 73	i = 105
# J = 74	j = 106
# K = 75	k = 107
# L = 76	l = 108
# M = 77	m = 109
# N = 78	n = 110
# O = 79	o = 111
# P = 80	p = 112
# Q = 81	q = 113
# R = 82	r = 114
# S = 83	s = 115
# T = 84	t = 116
# U = 85	u = 117
# V = 86	v = 118
# W = 87	w = 119
# X = 88	x = 120
# Y = 89	y = 121
# Z = 90	z = 122

#minu_conv_maiu =

