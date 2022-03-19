"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas

Questão
Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão). 
Imprima na tela o elemento e sua respectiva posição na lista. 
Exemplo: para a lista [1, 3, 6, “H”, [7,7,7]] a saída deve ser:
>>> Elemento 1 na posição 0
>>> Elemento 3 na posição 1
>>> Elemento 6 na posição 2
>>> Elemento “H” na posição 3
"""

lista = ["carro", "bike", "jirafa", "H", [7,7,7]]

for pos in range(len(lista)):
    print(f"Elemento {lista[pos]} na posição {pos}")
