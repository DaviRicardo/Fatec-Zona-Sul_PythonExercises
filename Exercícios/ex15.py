"""
15. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.
"""

import os

os.system('cls')

num_turmas = int(input("Digite a quantidade de turmas: "))

total_alunos = 0

for turma in range(1, num_turmas + 1):
    while True:
        num_alunos = int(input("\nDigite a quantidade de alunos na turma {}: ".format(turma)))
        if num_alunos <= 40:
            total_alunos += num_alunos
            break
        else:
            print("\nUma turma não pode ter mais de 40 alunos. Tente novamente.")

media_alunos = total_alunos / num_turmas

print("\nO número médio de alunos por turma é:", media_alunos)

