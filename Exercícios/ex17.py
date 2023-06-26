"""
17. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. 
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. 
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos.
"""

import os

os.system('cls')

valor_unitario = 1.99
quantidade_produto = 50

print("Loja Quase Dois - Tabela de Preços:\n")

for produto in range(1, quantidade_produto + 1):
    valor_total = produto * valor_unitario
    print("{} - R$ {:.2f}".format(produto, valor_total))
