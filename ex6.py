"6. Faça um programa que leia 5 números e informe o maior número."

import os

os.system('cls')

numeros = []
maior_valor = 0

for i in range (1, 6):
    numeros.append(float(input("Digite o " + str(i) + " número: ")))
    print ("")

maior_valor = max(numeros)

print ("O maior número é: " + str(maior_valor))