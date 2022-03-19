"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: INT E FLOAT

Questão
Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos. Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 3+1+4+1
"""

def somar_digitos(num):
    num_list = []
    for digito in range(len(num)):
        num_list.append(int(num[digito]))

    return sum(num_list)



numero = input("Digite um numero de 4 dígitos: ")

print(f"A soma dos digitos do numéro: {numero} é: {somar_digitos(numero)}")