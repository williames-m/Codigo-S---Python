"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: IF, ELIF, ELSE

Questão
Faça um programa que imprima na tela se um dado ano é bissexto ou não de acordo com as regras na ordem abaixo:

    1. Um ano que é divisível por 400 é bissexto.
    2. Dos anos que não entram na regra 1, se o ano for divisível por 100 então ele não é bissexto.
    3. Dos anos que não entram na regra 2, se o ano for divisível por 4 então ele é um ano bissexto.
    4. Todos os outros anos não são bissextos
"""


ano = int(input("Digite um ano para verificar se é bissexto ou não: "))

if (ano % 400 == 0):
    print(f"O {ano} é bissexto")
elif ano % 100 == 0:
    print(f"O {ano} não é bissexto")
elif ano % 4 == 0:
    print(f"O {ano} é bissexto")
else:
    print(f"O {ano} não é bissexto")


