"""
How Bootcamps - Stone - /código[s]
Data: 12/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: LAÇOS - REPETIÇÃO

Questão
Neste exercício, você criará um programa que calcula a média de uma coleção de valores inseridos pelo usuário e imprime-a na tela.
O usuário digitará 0 como um valor para indicar que nenhum outro valor será fornecido. 
Seu programa deve exibir uma mensagem de erro se o primeiro valor inserido pelo usuário for 0.
"""

valores = []

entrada = int(input("Digite o primeiro valor: "))

valores.append(entrada)

count = 0

while entrada != 0:

    if valores[count] != 0:
        valores.append(int(input("Digite outro valor: ")))
    else:
        entrada = 0
    
    count += 1
    
if (len(valores) == 1) and (valores[0] == 0):
    print("Primeiro valor digitado foi 0, valor inválido")
else:
    #removendo o ultimo elemento 0
    valores.pop()
    #calculando méda
    media = sum(valores) / len(valores)
    print(f"A média é {media}")
