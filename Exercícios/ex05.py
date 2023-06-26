"""
5. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""

import time
import os

os.system('cls')

numeros = []

for i in range(1, 21):
    print(i) 
    numeros.append(i)

time.sleep(8)
os.system('cls')

print (numeros)
