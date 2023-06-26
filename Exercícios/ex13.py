"""
13. Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""

import os

os.system('cls')

n = int(input("Digite o número de pessoas: "))

idades = []
soma_idades = 0

for i in range(n):
    print()
    idade = int(input("Digite a idade da pessoa {}: ".format(i + 1)))
    idades.append(idade)
    soma_idades += idade

media_idades = soma_idades / n

if media_idades >= 0 and media_idades <= 25:
    print ()
    print("\nA turma é considerada jovem.")
elif media_idades >= 26 and media_idades <= 60:
    print ()
    print("\nA turma é considerada adulta.")
else:
    print ()
    print("\nA turma é considerada idosa.")
