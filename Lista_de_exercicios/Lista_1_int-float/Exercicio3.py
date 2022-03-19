from math import sqrt

"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: INT E FLOAT

Questão
No exercício 2 você calculou a área de um triângulo a partir da sua base e altura. 
Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área. 
Compare a resposta com o exercício 2, dada das mesmas entradas. Os resultados devem ser idênticos.
"""

def area_pelo_lado(a: float, b: float, c: float) -> float:
    """Calcula a área do triangulo pelos 3 lados"""
    s = (a + b + c) / 2
    return sqrt(s * (s-a) * (s-b) * (s-c))

a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))

print(f"A área do triangulo com os lados: {a}, {b} e {c} é {area_pelo_lado(a, b, c):.2f}")