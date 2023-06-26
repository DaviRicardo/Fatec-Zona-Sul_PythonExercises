"""
25. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.
"""

import os

os.system('cls')

contador_intervalo_1 = 0  # [0-25]
contador_intervalo_2 = 0  # [26-50]
contador_intervalo_3 = 0  # [51-75]
contador_intervalo_4 = 0  # [76-100]

while True:
    numero = int(input("Digite um número positivo (ou negativo para sair): "))

    if numero < 0:
        break

    if numero >= 0 and numero <= 25:
        contador_intervalo_1 += 1
    elif numero >= 26 and numero <= 50:
        contador_intervalo_2 += 1
    elif numero >= 51 and numero <= 75:
        contador_intervalo_3 += 1
    elif numero >= 76 and numero <= 100:
        contador_intervalo_4 += 1

print("\nQuantidade de números nos intervalos:")
print("[0-25]:", contador_intervalo_1)
print("[26-50]:", contador_intervalo_2)
print("[51-75]:", contador_intervalo_3)
print("[76-100]:", contador_intervalo_4)
