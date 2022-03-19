
#importando log10 da biblioteca math
from math import log10

"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: INT E FLOAT

Questão
Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
    • A soma de A e B;
    • A diferença quando se subtrai B de A;
    • O produto (multiplicação) entre A e B;
    • O quociente (parte inteira da divisão) quando se divide A por B;
    • O resto da divisão entre A e B;
    • O resultado de log10 de A;
    • O resultado de A elevado a B;
    
"""

def soma(a: int, b: int) -> int:
    """Soma de 2 numeros"""
    return a + b

def subtracao(a: int, b: int) -> int:
    """Subtração de 2 numeros"""
    return a - b

def produto(a: int, b: int) -> int:
    """Multiplicação de 2 numeros"""
    return a * b

def quociente(a: int, b: int) -> int:
    """Quociente da divisão (Parte inteira da divisão)"""
    return a / b

def resto_divisao(a: int, b: int) -> int:
    """Resto da divisão"""
    return a // b

def log(a: int, b: int) -> int:
    """Quociente da divisão (Parte inteira da divisão)"""
    return log10(a)

def expoente(a: int, b: int) -> int:
    """Quociente da divisão (Parte inteira da divisão)"""
    return a ** b

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo numero: \n"))


print(f"A soma de: {a} + {b} é {soma(a, b)}\n")
print(f"A diferença de: {a} - {b} é {subtracao(a, b)}\n")
print(f"O produto de: {a} * {b} é {produto(a, b)}\n")
print(f"O quociente da divisão: {a}/{b} é {round(quociente(a,b), 0)}\n")
print(f"O resto da divisão: {a}/{b} é {resto_divisao(a,b)}\n")
print(f"O logaritimo na base 10 de: log10^{a} é {log(a, b)}\n")
print(f"A exponenciação de: {a} ^ {b} é {expoente(a, b)}")
