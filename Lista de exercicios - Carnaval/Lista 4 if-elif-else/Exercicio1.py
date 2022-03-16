"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: IF, ELIF, ELSE

Questão
Escreva um programa que diga se um número dado pelo usuário é par ou ímpar
"""

numero = int(input("Digite um número qualquer: "))

if (numero % 2 ) == 0:
    print(f"O numero {numero} é par")
else:
    print(f"O numero {numero} é impar")
