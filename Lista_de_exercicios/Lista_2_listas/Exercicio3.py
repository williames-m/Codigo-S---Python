"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas

Questão
Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições. Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser
>>> O maior elemento é 8 e está na posição 3
>>> O menor elemento é 3 e está na posição 4

Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.
"""

tamanho_lista = 6

lista = []

for pos in range(tamanho_lista):
    lista.append(int(input(f"Digite o {pos + 1}º numero: ")))


maior = max(lista)
menor = min(lista)

print(f"O maior elemento é {maior} está na posição {lista.index(maior)}.")
print(f"O menor elemento é {menor} está na posição {lista.index(menor)}.")
