"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: SET DICIONARIOS

Questão
Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dada o dicionário
>>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
A saída deverá ser
>>> {1: 8, 2: 4, 3: 6}
"""

cores = {1: "vermelho", 2: "azul", 3: "marrom"}

saida = dict()

for chave, valor in cores.items():
    saida[chave] = len(valor)

print(saida)



