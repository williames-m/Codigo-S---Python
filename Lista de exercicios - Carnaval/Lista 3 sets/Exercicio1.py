"""
How Bootcamps - Stone - /código[s]
Data: 03/03/2022
Autor: William Machado
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: SET DICIONARIOS

Questão
Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que existam alunos matriculados conforme abaixo:
    • Alunos matriculados em inglês:
        ◦ João Alves dos Santos
        ◦ Maria Magalhães
        ◦ Antônio da Silva Ferreira
        ◦ José Júnior Jarbas
        ◦ Henrique da Silva Sauro
        ◦ Joaquina Ferreira da Silva
        ◦ Fabiana Aparecida Bianco
        ◦ Marrone Gutierres
        ◦ Carlos Magno Farad
        ◦ Antônio da Silva Júnior Amaral

    • Alunos matriculados em francês:
        ◦ João Alves dos Santos
        ◦ Antônio da Silva Ferreira
        ◦ Fernanda Abdala Mohamed
        ◦ Abner Mignon Alib
        ◦ Alisson Figueiredo
        ◦ Henrique da Silva Sauro
        ◦ Maria Magalhães
        ◦ Marrone Gutierres
        ◦ Joaquina Ferreira da Silva

Faça um programa que responda as seguintes perguntas:

    1. Quantos alunos estão matriculados na escola, no total?
    2. Quantos e quais estão matriculados APENAS em INGLES?
    3. Quantos e quais estão matriculados APENAS em FRANCES?
    4. Quantos e quais estão matriculados EM AMBOS os cursos?
    5. Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?
"""

alunos_ingles = {"João Alves dos Santos",
              "Maria Magalhães",
              "Antônio da Silva Ferreira",
              "José Júnior Jarbas",
              "Henrique da Silva Sauro",
              "Joaquina Ferreira da Silva",
              "Fabiana Aparecida Bianco",
              "Marrone Gutierres",
              "Carlos Magno Farad",
              "Antônio da Silva Júnior Amaral"}

alunos_frances = {"João Alves dos Santos",
                "Antônio da Silva Ferreira",
                "Fernanda Abdala Mohamed",
                "Abner Mignon Alib",
                "Alisson Figueiredo",
                "Henrique da Silva Sauro",
                "Maria Magalhães",
                "Marrone Gutierres",
                "Joaquina Ferreira da Silva"}


total_alunos = alunos_ingles | alunos_frances

apenas_ingles = alunos_ingles - alunos_frances

apenas_frances = alunos_frances - alunos_ingles

ambos_cursos = alunos_ingles and alunos_frances

apenas_ing_apenas_franc = apenas_ingles | apenas_frances


print(f"\nQuestão 1 - Total de alunos: {len(total_alunos)}")

print("Os alunos são:")
for alunos in total_alunos:
    print(alunos)

print(f"\nQuestão 2 - Total de alunos matriculados apenas em Inglês são {len(apenas_ingles)}")
print("Os alunos são:")
for alunos in apenas_ingles:
    print(alunos)

print(f"\nQuestão 3 - Total de alunos matriculados apenas em Francês são {len(apenas_frances)}")
print("Os alunos são:")
for alunos in apenas_frances:
    print(alunos)

print(f"\nQuestão 4 - Total de alunos que estão matriculados em ambos cursos são {len(ambos_cursos)}")
print("Os alunos são:")
for alunos in ambos_cursos:
    print(alunos)

print(f"\nQuestão 5 - Total de alunos que estão matriculados somente em francês ou somete em inglês são {len(apenas_ing_apenas_franc)}")
print("Os alunos são:")
for alunos in apenas_ing_apenas_franc:
    print(alunos)
