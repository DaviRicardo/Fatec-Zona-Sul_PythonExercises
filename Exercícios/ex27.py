"""
27. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
a.	1 , 2, 3, 4  - Votos para os respectivos candidatos (deve-se montar a tabela,  ex: 1 - Jose/ 2- João/etc)
b.	5 - Voto Nulo
c.	6 - Voto em Branco
    Faça um programa que calcule e mostre:
a.	O total de votos para cada candidato;
b.	O total de votos nulos;
c.	O total de votos em branco;
d.	A percentagem de votos nulos sobre o total de votos;
e.	A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
"""

import os

os.system('cls')


candidatos = {
    1: "José",
    2: "João",
    3: "Maria",
    4: "Ana"
}

votos_candidatos = {
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

votos_nulos = 0
votos_em_branco = 0
total_votos = 0

while True:
    voto = int(input("Digite o código do candidato (ou 0 para encerrar a votação): "))
    
    if voto == 0:
        break
    
    if voto in candidatos:
        votos_candidatos[voto] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_em_branco += 1
    else:
        print("Voto inválido. Tente novamente.")
        continue
    
    total_votos += 1

print("\nResultado da Eleição")
print("--------------------")
print("Candidatos:")
for codigo, nome in candidatos.items():
    print(f"{codigo}: {nome} - {votos_candidatos[codigo]} votos")
    
print(f"Nulos: {votos_nulos} votos")
print(f"Em Branco: {votos_em_branco} votos")
print("--------------------")
print(f"Total de Votos: {total_votos}")

percentual_nulos = (votos_nulos / total_votos) * 100
percentual_em_branco = (votos_em_branco / total_votos) * 100

print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"Percentual de votos em branco: {percentual_em_branco:.2f}%")
