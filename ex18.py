"""
18. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. 
Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário
"""

import os

os.system('cls')

preco_pao = float(input("Preço do pão: "))

quantidade_paes = 50

print("\nPanificadora Pão de Ontem - Tabela de preços\n")

for quantidade in range(1, quantidade_paes + 1):
    valor_total = quantidade * preco_pao
    print("{} - R$ {:.2f}".format(quantidade, valor_total))
