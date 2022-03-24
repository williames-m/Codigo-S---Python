"""
How Bootcamps - Stone - /código[s]
Data: 20/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: LAÇOS - REPETIÇÃO

Questão
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, 
conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informadas ordenadas. 
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""

atletas = dict()

qtd_atleta = int(input("Digite quantos atletas serão: "))

cont_nome = 1

for _ in range(qtd_atleta):
    nome = input(f"Digite o nome {cont_nome}º atleta: ")

    atletas[nome] = []

    cont_nota = 1

    print("Digite a nota dos 7 juris")
    for _ in range(7):
        nota = float(input(f"Nota {cont_nota}: "))

        atletas[nome].append(nota)

        cont_nota += 1
    
    #salvando maior e menor nota
    maiornota = max(atletas[nome])
    menornota = min(atletas[nome])

    #removendo maior e menor nota
    atletas[nome].remove(max(atletas[nome]))
    atletas[nome].remove(min(atletas[nome]))

    # print(f"Atleta: {nome}")

    soma = 0
    i = 0

    for _ in range(len(atletas[nome])):
        soma += atletas[nome][i]
        # print(f"Nota {i+1}: {atletas[nome][i]}")
        i+=1
    media = soma/len(atletas[nome])

    print(f"\nResultado Final")
    print(f"Atleta: {nome}")
    print(f"Melhor nota: {maiornota}")
    print(f"Pior nota: {menornota}")
    print(f"Média: {media:.2f}")
    
    cont_nome +=1
