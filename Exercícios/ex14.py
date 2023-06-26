"""
14. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

import os

os.system('cls')

num_eleitores = int(input("Digite o número total de eleitores: "))

candidato1 = 0
candidato2 = 0
candidato3 = 0

for eleitor in range(num_eleitores):
    print ()
    voto = int(input("Eleitor {}, digite o número do candidato (1, 2 ou 3): ".format(eleitor + 1)))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print("\nVoto inválido!")

print()
print("\nResultado da eleição:")
print("\nCandidato 1:", candidato1, "voto(s)")
print("\nCandidato 2:", candidato2, "voto(s)")
print("\nCandidato 3:", candidato3, "voto(s)")
