"""
12. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

import os

os.system('cls')

N = int(input("Digite um número inteiro: "))

numeros_primos = []
num_divisoes = 0

if N <= 1:
    print()
    print(N, " não é um número primo.")
    exit(0)

for numero in range(2, N + 1):
    for i in range(2, numero):
        num_divisoes += 1
        if numero % i == 0:
            break
    else:
        numeros_primos.append(numero)

print("\nNúmeros primos entre 1 e", N, ":")
print(numeros_primos)
print("\nNúmero total de divisões realizadas:", num_divisoes)
