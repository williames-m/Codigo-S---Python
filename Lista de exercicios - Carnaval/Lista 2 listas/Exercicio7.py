"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas

Questão
Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro.

Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para str.
"""


lst = ["1", "7", "99", "15"]

for pos in range(len(lst)):
    lst[pos] = int(lst[pos])

print(f"Lista convertendo str para int ficou: {lst}")

for pos in range(len(lst)):
    lst[pos] = str(lst[pos])

print(f"Lista convertendo int para str ficou: {lst}")

