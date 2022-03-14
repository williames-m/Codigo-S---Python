"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas

Questão
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso).
Exemplo de saída:
>>> Meses com temperatura acima da média anual de 35,5°:
>>> 1 – janeiro
>>> 3 – março
>>> 6 – junho
"""


lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
               "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temp_meses = []

for mes in lista_meses:
    temp_meses.append(float(input(f"Digite a temperatura do mes {mes}: ")))

media_anual = sum(temp_meses) / len(temp_meses)

print(f"Meses com a temperatura acima da média anual de {media_anual:.1f}ºC: ")

for temperatura in temp_meses:
    if temperatura > media_anual:
        print(f"\nMes {lista_meses[temp_meses.index(temperatura)]}, com a temperatura {temperatura}ºC")
