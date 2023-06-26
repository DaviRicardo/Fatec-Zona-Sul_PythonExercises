"""
23. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
a.	Código da cidade;
b.	Número de veículos de passeio (em 1999);
c.	Número de acidentes de trânsito com vítimas (em 1999). 
    Deseja-se saber:
a.	Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
b.	Qual a média de veículos nas cinco cidades juntas;
c.	Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""

cidades = 5  
maior_indice = float('-inf')  
menor_indice = float('inf')  
soma_veiculos = 0  
soma_acidentes_menos_2000 = 0  
contador_cidades_menos_2000 = 0 

for i in range(cidades):
    codigo = input("Digite o código da cidade: ")
    veiculos = int(input("Digite o número de veículos de passeio em 1999: "))
    acidentes = int(input("Digite o número de acidentes de trânsito com vítimas em 1999: "))
    
    # Verifica se o índice de acidentes é maior que o maior índice atual
    if acidentes > maior_indice:
        maior_indice = acidentes
        cidade_maior_indice = codigo
    
    # Verifica se o índice de acidentes é menor que o menor índice atual
    if acidentes < menor_indice:
        menor_indice = acidentes
        cidade_menor_indice = codigo
    
    soma_veiculos += veiculos
    
    if veiculos < 2000:
        soma_acidentes_menos_2000 += acidentes
        contador_cidades_menos_2000 += 1

media_veiculos = soma_veiculos / cidades
media_acidentes_menos_2000 = soma_acidentes_menos_2000 / contador_cidades_menos_2000

print("==========================================================================")
print(f"Maior índice de acidentes: {maior_indice} na cidade {cidade_maior_indice}")
print(f"Menor índice de acidentes: {menor_indice} na cidade {cidade_menor_indice}")
print(f"Média de veículos nas cinco cidades juntas: {media_veiculos}")
print(f"Média de acidentes de trânsito em cidades com menos de 2000 veículos: {media_acidentes_menos_2000}")