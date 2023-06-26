"8. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120"

import os

os.system('cls')

numero = int(input("Digite um número inteiro: "))

fatorial = 1

if numero < 0:
    print("\nO fatorial não está definido para números negativos.")
    exit(0)
elif numero == 0:
    print("\nO fatorial de 0 é 1.")
    exit(0)
else:
    for i in range(1, numero + 1):
        fatorial *= i

print("\nO fatorial de ", numero, " é:", fatorial)
