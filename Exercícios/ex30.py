"""
30. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
	Atleta: Aparecido Parente
	Nota: 9.9
	Nota: 7.5
	Nota: 9.5
	Nota: 8.5
	Nota: 9.0
	Nota: 8.5
	Nota: 9.7
	
	Resultado final:
	Atleta: Aparecido Parente
	Melhor nota: 9.9
	Pior nota: 7.5
    Média: 9,04
"""

import os

os.system('cls')

def calcular_media(notas):
    notas_ordenadas = sorted(notas, reverse=True)
    
    notas_ordenadas = notas_ordenadas[1:-1]
    
    media = sum(notas_ordenadas) / len(notas_ordenadas)
    
    return media


nome_ginasta = input("Nome do ginasta: ")

notas = []
for i in range(7):
    nota = float(input("Nota: "))
    notas.append(nota)

media_final = calcular_media(notas)


print("\nAtleta:", nome_ginasta)
for nota in notas:
    print("Nota:", nota)
print("\nResultado final:")
print("Melhor nota:", max(notas))
print("Pior nota:", min(notas))
print("Média:", format(media_final, ".2f"))

