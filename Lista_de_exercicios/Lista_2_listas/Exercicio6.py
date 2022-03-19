"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Listas

Questão
Faça um programa que remova strings vazias de uma lista de strings. 
Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser
>>> [“Olá”, “meu”, “nome”, “é”, “facilitador”]

"""


lst = []

tamanho_lst = int(input("Digite o tamanho da lista: "))

count = 0

while count < tamanho_lst:
    lst.append(input("Digite qualquer coisa: "))

    count += 1

print(f"\nA lista criada é: {lst}\n")

for caracter in lst:
    if caracter == " ":
        lst.pop(lst.index(caracter))


print(f"A lista com o espaço em branco removido é: {lst}")
