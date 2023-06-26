"""
1. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

import os

os.system('cls')

while True:
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if username == password:
        print("Erro: A senha não pode ser igual ao nome de usuário.")
    else:
        print("\nLogin bem-sucedido!")
        break


