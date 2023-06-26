"""
31. Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
	Exemplo:
	12376489
 => 98467321
"""

import os

os.system('cls')

numero = int(input("Digite um número inteiro positivo: "))

numero_str = str(numero)

numero_invertido_str = numero_str[::-1]

numero_invertido = int(numero_invertido_str)

print("\nNúmero invertido:", numero_invertido)
