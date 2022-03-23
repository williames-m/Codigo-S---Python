"""
How Bootcamps - Stone - /código[s]
Data: 12/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: LAÇOS - REPETIÇÃO

Questão
Um determinado zoológico cobra a entrada com base na idade do visitante.
 - Os visitantes com 2 anos de idade ou menos não pagam para entrar. 
 - Crianças entre 3 e 12 anos custa R$14,00. 
 - Idosos com 65 anos ou mais custam R$18,00. 
 - A entrada para todos os outros visitantes é de R$23,00. 
Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo, com uma idade inserida em cada linha.
O usuário digitará uma linha em branco para indicam que não há mais visitantes no grupo. 
Em seguida, seu programa deve exibir o custo de admissão para o grupo com uma mensagem apropriada.
O custo deve ser exibido usando duas casas decimais.
"""


def calcular_valor(lst: list) -> float:

    valores_pagar = []

    for valor in lst:
        if valor <= 2:
            valores_pagar.append(0.00)
        elif 3 <= valor < 13:
            valores_pagar.append(14.00)
        elif valor >= 65:
            valores_pagar.append(18.00)
        else:
            valores_pagar.append(23.00)
    
    return sum(valores_pagar)



idade_visitantes = []

idade = float(input("Digite a primeira idade: "))

idade_visitantes.append(idade)

count = 0

while idade != " ":

    if idade != " ":
        idade = input("Digite outra idade ou espaço em branco para sair: ")
        
        if idade == " ":
            break
        else:
            idade_visitantes.append(float(idade))
        
    else:
        idade = " "
        

print(f"O valor total a ser pago por {len(idade_visitantes)} pessoas é de R${calcular_valor(idade_visitantes):.2f}")
    
