"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: INT E FLOAT

Questão
Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário.
"""

def imc(peso: float, altura: float) -> float:
    return peso / (altura ** 2)

peso = float(input("Digite o peso em Kg: "))
altura = float(input("Digite a altura em mts: "))

print(f"O IMC com o peso: {peso} e altura: {altura} é {imc(peso, altura):.2f}")