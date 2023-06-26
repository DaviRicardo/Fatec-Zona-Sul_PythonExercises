""" 
9. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes...
e limitando o fatorial a números inteiros positivos e menores que 16. 
"""

import os

os.system('cls')

def calcular_fatorial(numero):
    fatorial = 1

    if numero < 0 or numero >= 16:
        return None

    elif numero == 0:
        return 1

    else:
        for i in range(1, numero + 1):
            fatorial *= i

        return fatorial


while True:
    entrada = input("\nDigite um número inteiro positivo menor que 16 (ou 'sair' para encerrar): ")

    if entrada.lower() == "sair":
        print("\nEncerrando o programa...")
        break

    else:
        try:
            numero = int(entrada)
            resultado = calcular_fatorial(numero)

            if resultado is not None:
                print("\nO fatorial de ", numero, " é ", resultado)
            else:
                print("\nO número deve ser um inteiro positivo menor que 16.\n")
                print()

        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido ou 'sair' para encerrar.")

