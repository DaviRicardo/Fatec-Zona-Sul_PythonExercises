"""
22. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

import os

os.system('cls')

aluno_mais_alto = 0
altura_mais_alta = 0

aluno_mais_baixo = 0
altura_mais_baixa = float('inf')

for i in range(1, 11):
    numero_aluno = int(input("Digite o número do aluno {}: ".format(i)))
    altura_aluno = float(input("Digite a altura do aluno {} (em cm): ".format(i)))

    if altura_aluno > altura_mais_alta:
        aluno_mais_alto = numero_aluno
        altura_mais_alta = altura_aluno

    if altura_aluno < altura_mais_baixa:
        aluno_mais_baixo = numero_aluno
        altura_mais_baixa = altura_aluno

print("\nAluno mais alto: número {}, altura {}cm".format(aluno_mais_alto, altura_mais_alta))
print("\nAluno mais baixo: número {}, altura {}cm".format(aluno_mais_baixo, altura_mais_baixa))
