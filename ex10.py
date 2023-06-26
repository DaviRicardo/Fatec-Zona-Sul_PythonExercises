"""
10. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1. 
"""

import os

os.system('cls')

numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print()
    print(numero, " não é um número primo.")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print()
            print(numero, "não é um número primo.")
            break
    else:
        print()
        print(numero, " é um número primo.")
