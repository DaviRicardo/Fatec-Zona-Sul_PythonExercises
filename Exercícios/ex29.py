"""
29. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
	Atleta: Rodrigo Curvêllo
	
	Primeiro Salto: 6.5 m
	Segundo Salto: 6.1 m
	Terceiro Salto: 6.2 m
	Quarto Salto: 5.4 m
	Quinto Salto: 5.3 m
	
	Melhor salto:  6.5 m
	Pior salto: 5.3 m
	Média dos demais saltos: 5.9 m
	
	Resultado final:
    Rodrigo Curvêllo: 5.9 m
"""

import os

os.system('cls')

while True:
    nome_atleta = input("Digite o nome do atleta (ou deixe em branco para encerrar): ")

    if nome_atleta == "":
        break

    saltos = []
    for i in range(1, 6):
        distancia = float(input(f"Digite a distância do salto {i}: "))
        saltos.append(distancia)

    melhor_salto = max(saltos)
    pior_salto = min(saltos)
    saltos.remove(melhor_salto)
    saltos.remove(pior_salto)

    media_saltos = sum(saltos) / len(saltos)

    print("--------------------")
    print("Resultado do Atleta")
    print("--------------------")
    print(f"Atleta: {nome_atleta}")

    for i, salto in enumerate(saltos, start=1):
        print(f"Salto {i}: {salto} m")

    print(f"\nMelhor salto: {melhor_salto} m")
    print(f"Pior salto: {pior_salto} m")
    print(f"Média dos demais saltos: {media_saltos} m")

    print("\nResultado final:")
    print(f"{nome_atleta}: {media_saltos} m")


