"""
How Bootcamps - Stone - /código[s]
Data: 20/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: LAÇOS - REPETIÇÃO

Questão
Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.
"""


termos = int(input("Digite digite quantos termos serão: "))

H = 1

valor = 1

for n in range(termos):

    H += 1 / (valor + 1)

    valor +=1

print(f"H com {termos} termos é : {H:.2f}")
