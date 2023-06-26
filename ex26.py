"""
26. Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

import os

os.system('cls')

cardapio = {
    100: {"item": "Cachorro Quente", "preco": 1.20},
    101: {"item": "Bauru Simples", "preco": 1.30},
    102: {"item": "Bauru com ovo", "preco": 1.50},
    103: {"item": "Hambúrguer", "preco": 1.20},
    104: {"item": "Cheeseburguer", "preco": 1.30},
    105: {"item": "Refrigerante", "preco": 1.00},
}

total_pedido = 0.0

while True:
    codigo = int(input("Digite o código do item (ou 0 para encerrar o pedido): "))
    if codigo == 0:
        break
    
    if codigo not in cardapio:
        print("Código inválido. Tente novamente.")
        continue
    
    quantidade = int(input("Digite a quantidade desejada: "))
    if quantidade <= 0:
        print("Quantidade inválida. Tente novamente.")
        continue
    
    item = cardapio[codigo]
    valor_item = item["preco"] * quantidade
    total_pedido += valor_item
    
    print(f"{quantidade}x {item['item']}: R${valor_item:.2f}")
    print()
    
print(f"Total do pedido: R${total_pedido:.2f}")

