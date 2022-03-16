"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: IF, ELIF, ELSE

Questão
Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.
"""

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 % numero2 == 0:
    print(f"O numero {numero1} é divisível por {numero2}")
else:
    print(f"O numero {numero1} não é divisível por {numero2}")
