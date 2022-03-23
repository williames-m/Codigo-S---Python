"""
How Bootcamps - Stone - /código[s]
Data: 12/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: LAÇOS - REPETIÇÃO

Questão
Uma aproximação para o valor de pi pode ser calculado a partir da fórmula abaixo (uma série infinita):

pi = 3 + (4 / (2 * 3 * 4)) - (4 / (4*5*6)) - (4 / (6*7*8)) - (4 / (8*9*10)) - (4 / (10*11*12)) - (4 / (12*13*14)) ...

Escreva um programa que calcule o número pi com 15 aproximações. 
A primeira aproximação deve considerar apenas o primeiro termo da série, ou seja 3. A segunda aproximação deve considerar a soma até o segundo termo, e assim por diante!
"""






# def calc_pi() -> float:
#     i = 2
#     pi = 3
#     j = 2
#     print(f"Pi1: {pi}")
#     for _ in range(7):
#         pi1 = (4/(i*(i+1)*(i+2)))
#         print(f"Pi{j}: {pi1}")
#         pi2 = -(4/((i+2)*(i+3)*(i+4)))
#         print(f"Pi{j+1}: {pi2}")
#         pi += (pi1 + pi2)
#         i += 4
#         j += 2
#     return(pi)


# print(f"Pi com 15 aproximações: {calc_pi()}")

pi = 3

for i in range(1, 15):
    f = i * 2
    valor = (4 / ((f) * (f + 1) * (f + 2)))
    print(pi)
    if i % 2 == 0:
        pi -= valor
    else:
        pi += valor

print(f'\nO valor aproximado de pi é {pi}')
