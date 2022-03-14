"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: INT E FLOAT

Questão
Faça um programa que receba a base e altura de um triângulo e imprima a área dele.
"""

def area_triangulo(b:float, h:float) -> float:
    """Calcula a área de um triângulo"""
    return (b * h) / 2

b = float(input("Digite a base do triângulo: "))
h = float(input("Digite a altura do triângulo: "))

print(f"A área do triangulo é: {area_triangulo(b,h)}")