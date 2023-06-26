"11. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível."

import os

os.system('cls')

numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print()
    print(numero, " não é um número primo.")
else:
    divisores = []
    for i in range(2, numero):
        if numero % i == 0:
            divisores.append(i)

    if len(divisores) == 0:
        print()
        print(numero, " é um número primo.")
    else:
        print()
        print(numero, " não é um número primo. É divisível por:", divisores)
