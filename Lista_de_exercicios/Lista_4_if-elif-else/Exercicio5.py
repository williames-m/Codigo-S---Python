"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: IF, ELIF, ELSE

Questão
Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo) com três letras, um traço e quatro números. 
Exemplos: 
    • Dada a entrada ABT-1234 o programa deveria exibir True
    • Dada a entrada JKL9999 o programa deveria exibir False
    • Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False 
"""


placa = input("Digite o nome da placa: ")




if len(placa) != 8:
    placa_valida = False

else:
    letras = placa[:3]
    numero = placa[-4:]
    traço = placa[3]

    if (
        letras.isalpha()
        and letras.isupper()
        and numero.isdigit()
        and traço == "-"
    ):
        placa_valida = True

    else:
        placa_valida = False

print(f"A {placa} é: {placa_valida}")