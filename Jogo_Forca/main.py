"""
How Bootcamps - Stone - /código[s]
Data: 31/03/2022
Autor: Henrique Junqueira Branco
Enunciado: Construa um jogo da forca!
A palavra secreta é representada por uma linha de traços em cada letra da palavra. 
Esta pode vir de uma variável ou arquivo, como achar melhor.
Se o jogador que adivinha sugerir uma letra que ocorre na palavra, o programa a escreve em todas as posições corretas. 
Se a letra sugerida for incorreta, o programa deve mostrar isso de alguma forma (desenho, mensagem, etc.).
As tentativas (acertos e erros) são definidas em variáveis.
Quando se esgotarem as tentativas, o programa finaliza dizendo que o jogador perdeu e mostra a palavra correta.
Algumas funções, importações e variáveis foram pré-definidas para auxiliá-los!
"""

from random import choice
from string import octdigits
# from random import randrange
from util import WORDS, STATUS


def get_secret_word(words: list) -> str:
    """Devolve uma palavra aleatória de uma lista."""
    return choice(words).upper()

# segundo modo de fazer a escolha da palavra
# def get_secret_word():
#     """Devolve uma palavra aleatória de uma lista."""
#     archive = open("word.txt", "r")
#     word = []

#     for line in archive:
#         line = line.strip()
#         word.append(line)

#     archive.close()

#     number = random.randrange(0, len(word))
#     secret_word = word[number].upper()
#     return secret_word
    


def print_game_board(secret_word: str, correct_letters: list[str], missed_letters: list[str], error: int, attempts: int, status: list[str]):
    """Imprime a situação atual do jogo."""
    
    encoded_word = ""

    for letter in secret_word:
        if letter not in correct_letters:
            encoded_word += "_"
        else:
            encoded_word += letter

    if error <= attempts:
        print(status[error])

        print(encoded_word)

        print(f"\nLetras corretas: {' '.join(correct_letters)}")
        print(f"\nLetras erradas: {' '.join(missed_letters)}")

    return None



def read_input_player():
    """Lê uma letra do usuário."""

    input_char = input("\nDigite uma letra: ").upper()

    while len(input_char) != 1:
        print("Entre com apenas 1 caracter!")
        input_char = input("\nDigite apenas uma letra com um único caracter: ").upper()

    return input_char

# def read_input_player(choice):
#     """Lê uma letra do usuário."""
#     choice = input("Digite uma letra: ")
#     choice = choice.strip().upper()
#     return choice


def guess_letter(input_char: str, secret_word: str, correct_letters: list, wrong_letters: list) -> bool:
    """Verifica se uma letra está na palavra secreta ou já foi jogada, seja certa ou errada."""

    if input_char in secret_word and input_char not in correct_letters:
        correct_letters.append(input_char)
        return True

    elif input_char not in secret_word and input_char not in wrong_letters:
        wrong_letters.append(input_char)
        return False

    else:
        print("\nEsta letra já foi jogada, por favor escolha outra!")
        return False




def game_continue(correct_letters: list, secret_word: str, error: int, attempts: int, status: list) -> bool:
    """Função que decide se jogo já encerrou ou não."""
    
    if set(correct_letters) == set(secret_word):
        print(f"\nVocê venceu! A palavra secreta é {secret_word}")
        return False

    elif error >= attempts:
        print(status[error])
        print(f"A palavra secreta é {secret_word}")
        return False     
    
    return True


secret_word = get_secret_word(WORDS)# variável para palavra secreta
correct_letters = []  # variável que armazena as letras corretas já jogadas
missed_letters = []  # variável que armazena as letras incorretas já jogadas
error = 0  # erro inicial
attempts = 6  # tentativas

while game_continue(correct_letters, secret_word, error, attempts, STATUS):
    print_game_board(secret_word, correct_letters, missed_letters, error, attempts, STATUS)
    input_char = read_input_player()
    if not guess_letter(input_char, secret_word, correct_letters, missed_letters):
        error += 1

