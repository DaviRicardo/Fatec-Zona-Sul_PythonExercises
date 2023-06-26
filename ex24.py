"""
24. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
	Os juros e a quantidade de parcelas seguem a tabela abaixo
	Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
a.	1       0
b.	3       10
c.	6       15
d.	9       20
e.  12      25
"""

import os

os.system('cls')

valor_divida = float(input("Digite o valor da dívida: "))

print("\nValor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")
print("--------------------------------------------------------------------------")

parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]

for i in range(len(parcelas)):
    valor_juros = valor_divida * juros[i] / 100
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / parcelas[i]

    print("{:.2f}           | {:.2f}            | {:2d}                      | {:.2f}".format(valor_total, valor_juros, parcelas[i], valor_parcela))
