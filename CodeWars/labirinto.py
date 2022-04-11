"""
How Bootcamps - Stone - /código[s]
Data: 07/04/2022
Autor: Ângela Maria Felini, Flavia Fernandes dos Santos, Jaqueline Rocha Otero, Ludmila Custodio Timoteo, William Machado,
Enunciado:
Implementar um sistema em Python que efetue o comportamento de um robô tentando encontrar
a saída de um labirinto.
As inspirações para esse projeto foram: aspiradores de pó automáticos (como o Roomba),
navegação no Google Maps e o problema clássico do Labirinto do Minotauro.
O objetivo do projeto é posicionar um robô em um labirinto e desenvolver a lógica para que ele
percorra esse labirinto em busca da saída, avançando pelas células em branco, respeitando as
paredes e retornando por um caminho caso esteja encurralado. O robô não pode avançar 2 vezes
por um mesmo caminho, assim, ao descobrir que está encurralado pode retornar pelas células
percorridas, mas não deve avançar novamente por este caminho.
"""

from time import sleep

PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = '-'
ROBO = 'R'
SAIDA = 'S'

ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

LABIRINTO = [
    # 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14  15   16    17   18  19
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], # 0
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], # 1
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], # 2
    ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], # 3
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], # 4
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], # 5
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], # 6
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], # 7
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], # 8
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']  # 9
]

def print_labirinto():
    """Imprime o desenho do labirinto
    
    Returns: None
    """

    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")

def movimento(posicao: tuple, direcao: list) -> list:
    """
    Movimentação do robo
    Args:
        posicao (tuple): posição do robozinho
        direcao (list): direção a ser percorrida
    Returns:
        list: trajetória e posição do robo após o movimento
    """
    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
    return [posicao[0] + direcao[0], posicao[1] + direcao[1]]
    
def verifica_movimento(posicao: tuple, direcao: list) -> bool: 
    """Verifica se a posição a ser movimentada é valida ou não
    Args:
        posicao (tuple): posição do robozinho
        direcao (list): direção a ser percorrida
    Returns:
        bool: False se encontrar parede ou caminho já percorrido
              True se caminho está livre ou encontrou a saída
    """
    
    possivel_caminho = LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]]
        
    # Verifica se a direção não é parede e se não percorreu o caminho
    if possivel_caminho == PAREDE:
        return False
    elif possivel_caminho == CAMINHO_PERCORRIDO:
        return False
    elif possivel_caminho == CAMINHO_LIVRE:
        return True
    elif possivel_caminho == SAIDA:
        return True

def main():

    #Guardar a posição percorrida pelo robo
    posicao_percorrida = [] 
    
    possiveis_direcoes = [DIREITA, BAIXO, ESQUERDA, CIMA]
    
    POSICAO_SAIDA = [9,18]
    
    print("\n***********************************************************************************************\n")
    print("BEM VINDO AO LABIRINTO CODE WARS!!\n\nVocê deverá escolher uma posição no labirinto e o seu robozinho irá procurar pela saída!\nEscolha dois números, sendo o primeiro entre 0 e 9 e o segundo entre 0 e 19.\nEstas coordenadas devem estar separadas por uma vírgula. Exemplo: 8, 15\nSe a posição que você escolher for uma parede do labirinto, será solicitado que você digite outro par de números.\n\nBOA SORTE!")
    print("\n***********************************************************************************************\n")

    # recebendo a posição inicial do robozinho
    tamanho_labirinto_linhas = len(LABIRINTO)
    tamanho_labirinto_colunas = len(LABIRINTO[0])
    
    posicao_valida = False

    while not posicao_valida:
        POSICAO_INICIAL = list(map(int, input("Digite uma posição para o Robô (linha, coluna): ").split(',')))
        if POSICAO_INICIAL[0] < tamanho_labirinto_linhas and POSICAO_INICIAL[1] < tamanho_labirinto_colunas:
        # verificar se a posição inicial é valida (se é diferente da parede ou saida) então coloca o robozinho
            valor_posicao_robo = LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]]
            if valor_posicao_robo != PAREDE and valor_posicao_robo != SAIDA:
                posicao_valida = True
            else:
                print("Posição selecionada é inválida, tente novamente!")
        
    LABIRINTO[POSICAO_SAIDA[0]][POSICAO_SAIDA[1]] = SAIDA

    POSICAO_ATUAL = POSICAO_INICIAL 
    
    print_labirinto()

    contador_direcoes = 0 
    
    posicao_percorrida.append(POSICAO_ATUAL)
    
    while POSICAO_ATUAL != POSICAO_SAIDA:
        
        for direcao in possiveis_direcoes:
            if contador_direcoes > 3:
                #onde o robo travou
                LABIRINTO[posicao_percorrida[-1][0]][posicao_percorrida[-1][1]] = CAMINHO_PERCORRIDO 
                posicao_percorrida.pop()
                # posição atual é igual a última possicao percorrida
                POSICAO_ATUAL = posicao_percorrida[-1] 
                LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = ROBO 
                print_labirinto() 
                sleep(0.5)
                contador_direcoes = 0

            contador_direcoes += 1
        
            if verifica_movimento(POSICAO_ATUAL, direcao): 
                POSICAO_ATUAL = movimento(POSICAO_ATUAL, direcao)                 
                posicao_percorrida.append(POSICAO_ATUAL)
                contador_direcoes = 0
                print_labirinto()
                sleep(0.5) 

    print("*********************")
    print("\n****   PARABÉNS  ****\n")
    print("\n*** ACHOU A SAIDA ***\n")
    print("*********************")

if __name__ == "__main__":
    main()