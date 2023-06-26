"""
2. Faça um programa que leia e valide as seguintes informações:
a.	Nome: maior que 3 caracteres;
b.	Idade: entre 0 e 150;
c.	Salário: maior que zero;
d.	Sexo: 'f' ou 'm';
e.	Estado Civil: 's', 'c', 'v', 'd';
"""

import os

os.system('cls')

while True:
    nome = input("Digite o nome (maior que 3 caracteres): ")
    if len(nome) <= 3:
        print("\nErro: O nome deve ter mais de 3 caracteres.\n")
        continue

    idade = int(input("Digite a idade (entre 0 e 150): "))
    if idade < 0 or idade > 150:
        print("\nErro: A idade deve estar entre 0 e 150.\n")
        continue

    salario = float(input("Digite o salário (maior que zero): "))
    if salario <= 0:
        print("\nErro: O salário deve ser maior que zero.\n")
        continue

    sexo = input("Digite o sexo (f/m): ")
    if sexo.lower() not in ['f', 'm']:
        print("\nErro: O sexo deve ser 'f' ou 'm'.\n")
        continue

    estado_civil = input("Digite o estado civil (s/c/v/d): ")
    if estado_civil.lower() not in ['s', 'c', 'v', 'd']:
        print("\nErro: O estado civil deve ser 's', 'c', 'v' ou 'd'.\n")
        continue

    # Todas as informações são válidas
    print("\nInformações válidas.")
    break
