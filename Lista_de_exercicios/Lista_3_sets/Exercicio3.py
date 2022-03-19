"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: SET DICIONARIOS

Questão
Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
>>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>>> {“química”: 87, “física”: 83, matemática”: 81}
"""

materias_notas = {"matemática": 81, "física": 83, "química": 87, "biologia":82}

print(f"Lista não ordenada {materias_notas}")

notas_ordenadas = sorted(materias_notas.items(), key = lambda nota:nota[1], reverse = True )

print(f"Lista ordenada {notas_ordenadas}")
