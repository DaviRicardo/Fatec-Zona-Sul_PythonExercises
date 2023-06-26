"""
20. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes.
"""

import os

os.system('cls')

codigo_cliente_alto = 0
altura_cliente_alto = 0.0
codigo_cliente_baixo = 0
altura_cliente_baixo = float("inf")
codigo_cliente_gordo = ""
peso_cliente_gordo = 0.0
codigo_cliente_magro = ""
peso_cliente_magro = float("inf")


soma_alturas = 0.0
soma_pesos = 0.0
quantidade_clientes = 0

while True:
    print()
    codigo = input("Digite o código do cliente (0 para encerrar): ")
    if codigo == "0":
        break

    altura = float(input("Digite a altura do cliente (em metros): "))
    peso = float(input("Digite o peso do cliente (em kg): "))

    soma_alturas += altura
    soma_pesos += peso
    quantidade_clientes += 1

    # Verificar se o cliente é o mais alto
    if altura > altura_cliente_alto:
        codigo_cliente_alto = codigo
        altura_cliente_alto = altura

    # Verificar se o cliente é o mais baixo
    if altura < altura_cliente_baixo:
        codigo_cliente_baixo = codigo
        altura_cliente_baixo = altura

    # Verificar se o cliente é o mais gordo
    if peso > peso_cliente_gordo:
        codigo_cliente_gordo = codigo
        peso_cliente_gordo = peso

    # Verificar se o cliente é o mais magro
    if peso < peso_cliente_magro:
        codigo_cliente_magro = codigo
        peso_cliente_magro = peso

media_alturas = soma_alturas / quantidade_clientes
media_pesos = soma_pesos / quantidade_clientes

print()
print("Cliente mais alto:")
print("Código: {}".format(codigo_cliente_alto))
print("Altura: {:.2f} metros".format(altura_cliente_alto))
print()

print("Cliente mais baixo:")
print("Código: {}".format(codigo_cliente_baixo))
print("Altura: {:.2f} metros".format(altura_cliente_baixo))
print()

print("Cliente mais gordo:")
print("Código: {}".format(codigo_cliente_gordo))
print("Peso: {:.2f} kg".format(peso_cliente_gordo))
print()

print("Cliente mais magro:")
print("Código: {}".format(codigo_cliente_magro))
print("Peso: {:.2f} kg".format(peso_cliente_magro))
print()

print("Média das alturas: {:.2f} metros".format(media_alturas))
print("Média dos pesos: {:.2f} kg".format(media_pesos))


