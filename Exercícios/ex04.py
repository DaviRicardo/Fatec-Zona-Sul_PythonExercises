"""
4. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
"""

import os

os.system('cls')

def calcular_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b):
    anos = 0

    while populacao_a < populacao_b:
        populacao_a += populacao_a * taxa_crescimento_a
        populacao_b += populacao_b * taxa_crescimento_b
        anos += 1

    return anos


while True:
    try:
        populacao_a = int(input("Informe a população do país A: "))
        taxa_crescimento_a = float(input("Informe a taxa de crescimento do país A (em decimal): "))
        populacao_b = int(input("Informe a população do país B: "))
        taxa_crescimento_b = float(input("Informe a taxa de crescimento do país B (em decimal): "))

        anos_necessarios = calcular_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b)

        print(f"\nLevará cerca de {anos_necessarios} anos para que a população do país A ultrapasse ou iguale a população do país B.")

        repetir = input("Deseja repetir a operação? (s/n): ")
        if repetir.lower() == "s":
            os.system('cls')
        else: 
            break

    except ValueError:
        print("Entrada inválida. Certifique-se de que os valores são numéricos.")
