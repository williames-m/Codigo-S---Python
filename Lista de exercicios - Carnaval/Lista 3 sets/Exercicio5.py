"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: SET DICIONARIOS

Questão
Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. Exemplo: dado o dicionário
>>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
A saída deve ser
>>> Nota máxima -> Júnior : 80
>>> Nota mínima -> Theodoro : 20
"""

notas = {"Theodoro": 20, "Márcia": 50, "Júnior": 80}

valores = list(notas.values())

# nomes = list(notas.keys())

maior = max(valores)
menor = min(valores)


indice_maior = valores.index(maior)
indice_menor = valores.index(menor)

# nome_maior_nota = nomes[indice_maior]
# nome_menor_nota = nomes[indice_menor]

# print(nome_maior_nota)
# print(nome_menor_nota)

print(f"A nota máxima -> {list(notas.keys())[indice_maior]} : {maior} ")
print(f"A nota minima -> {list(notas.keys())[indice_menor]} : {menor} ")
