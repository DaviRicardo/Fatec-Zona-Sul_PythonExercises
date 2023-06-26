"""
16. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""

import os

os.system('cls')

num_cds = int(input("Digite a quantidade de CDs na coleção: "))

total_investido = 0

for cd in range(1, num_cds + 1):
    print()
    valor_cd = float(input("Digite o valor do CD {}: ".format(cd)))
    total_investido += valor_cd

media_gasto = total_investido / num_cds

print()
print("\nValor total investido na coleção: R$ {:.2f}".format(total_investido))
print("\nValor médio gasto em cada CD: R$ {:.2f}".format(media_gasto))


