"""
32. Faça um programa que mostre os N termos da série a seguir:
	S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
    Imprima no final a soma da série.
"""

import os
from fractions import Fraction

os.system('cls')

soma = 0
m = 1

n = int(input("Digite o número de termos da série: "))

print("\nTermos da série: ")

for i in range(1, n + 1):   
    termo = Fraction(i, m)
    soma += termo
    m += 2
    print(f"+ {termo} ", end = "")

print()
print("\n====Soma da Série====")
print("Fração:", soma)
print("Decimal: ", float(soma))