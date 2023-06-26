"""
19. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
"""

import os

os.system('cls')

print ("Lojas Tabajaras\n")

while True:
    total_compra = 0.0

    while True:
        preco = float(input("Digite o preço da mercadoria (0 para encerrar): "))
        if preco == 0:
            break

        total_compra += preco

    print("\nTotal da compra: R$ {:.2f}".format(total_compra))

    print()
    valor_pago = float(input("Digite o valor pago em dinheiro pelo cliente: "))

    troco = valor_pago - total_compra
    print("\nTroco: R$ {:.2f}".format(troco))

    print()
    opcao = input("Deseja registrar uma nova compra? (S/N): ")
    if opcao.lower() == "s":
        os.system('cls')
        print ("Lojas Tabajaras\n")
    else:
        break
