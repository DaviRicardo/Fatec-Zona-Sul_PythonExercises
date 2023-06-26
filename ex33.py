"""
33. Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
"""

import os
from fractions import Fraction

os.system('cls')

soma = Fraction(0, 1)

n = int(input("Digite o número de termos da série: "))

for i in range(1, n + 1):
    termo = Fraction(1, i)
    soma += termo

print("\nO valor de H com", n, "termos é:")
print("Fração:", soma)
print("Decimal: ", float(soma))
