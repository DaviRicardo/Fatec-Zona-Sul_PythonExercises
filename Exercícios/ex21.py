"""
21. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a.	Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b.	Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c.	A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""

import os
import time

os.system('cls')

ano_inicial = 1995
salario_inicial = 1000.0
percentual_aumento = 0.015

ano_atual = 2023
salario_atual = salario_inicial

for ano in range(ano_inicial, ano_atual + 1):
    salario_atual += salario_atual * percentual_aumento

    if ano == 1997:
        percentual_aumento *= 2

print("Salário atual do funcionário em {}: R$ {:.2f}".format(ano_atual, salario_atual))

time.sleep (6)
os.system('cls')
percentual_aumento = 0.015

salario_inicial = float(input("Digite o salário inicial do funcionário: R$ "))

salario_atual = salario_inicial

for ano in range(ano_inicial, ano_atual + 1):
    salario_atual += salario_atual * percentual_aumento
    
    if ano == 1997:
        percentual_aumento *= 2

print("\nSalário atual do funcionário em {}: R$ {:.2f}".format(ano_atual, salario_atual))


