"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: IF, ELIF, ELSE

Questão
A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns
Barulho             Nível sonoro (dB)
Britadeira          130
Cortador de grama   106
Despertador         70
Cômodo em silêncio  40

Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. 
Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho. 
Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado está. 
Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo. 
"""

db = int(input("Digite o valor do nível sonoro em dB: "))

if db == 130:
    print("Barulho sonoro de uma Britadeira")
elif 130 > db > 106:
    print("Barulho sonoro entre Britadeira e Cortador de grama")
elif db == 106:
    print("Barulho sonoro de um Cortador de grama")
elif 106 > db > 70:
    print("Barulho sonoro entre Cortador de grama e Despertador")
elif db == 70:
    print("Barulho sonoro de um Despertador")
elif 70 > db > 40:
    print("Barulho sonoro entre um Despertador e Cômodo em silêncio")
elif db == 40:
    print("Barulho sonoro de um Cômodo em silêncio")
elif db < 40:
    print("Barulho sonoro menor que um Cômodo em silêncio")
else:
    print("Barulho sonoro maior que uma Britadeira")
