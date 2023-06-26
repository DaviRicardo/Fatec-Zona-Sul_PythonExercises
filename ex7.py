"7. Faça um programa que leia 5 números e informe a soma e a média dos números."

import os

os.system('cls')

numeros = []

for i in range(1, 6):
    numeros.append(float(input("Digite o " + str(i) + " número: ")))
    print ()

soma = sum(numeros)
media = soma / len(numeros)

print("\nA soma dos números é:", soma)
print("A média dos números é:", media)
