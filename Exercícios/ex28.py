"""
28. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
a.	Maior e Menor Acerto;
b.	Total de Alunos que utilizaram o sistema;
c.	A Média das Notas da Turma.
d.	Gabarito da Prova:
	01 - A
	02 - B
	03 - C
	04 - D
	05 - E
	06 - E
	07 - D
	08 - C
	09 - B
    10 - A
Após concluir isto, pode-se opcionalmente incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
"""

import os

os.system('cls')

gabarito = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "E",
    7: "D",
    8: "C",
    9: "B",
    10: "A"
}

total_alunos = 0
soma_notas = 0
maior_acerto = 0
menor_acerto = 10

continuar = "sim"

while continuar.lower() == "sim":
    total_alunos += 1
    acertos = 0
    
    print("Respostas do Aluno:")
    for i in range(1, 11):
        resposta = input(f"Questão {i}: ")
        if resposta.upper() == gabarito[i]:
            acertos += 1
    
    soma_notas += acertos
    
    if acertos > maior_acerto:
        maior_acerto = acertos
    if acertos < menor_acerto:
        menor_acerto = acertos
    
    continuar = input("\nOutro aluno vai utilizar o sistema? (sim/não): ")

media_notas = soma_notas / total_alunos

print("--------------------")
print("Resultado Final")
print("--------------------")
print(f"Maior Acerto: {maior_acerto} questões")
print(f"Menor Acerto: {menor_acerto} questões")
print(f"Total de Alunos: {total_alunos}")
print(f"Média das Notas da Turma: {media_notas:.2f}")
print("--------------------")
print("Gabarito da Prova:")
for i in range(1, 11):
    print(f"{i:02d} - {gabarito[i]}")
