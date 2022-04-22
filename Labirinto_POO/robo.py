
from time import sleep

from labirinto import Labirinto

class Robo:
    
    ESQUERDA = [0, -1]
    DIREITA  = [0, 1]
    CIMA     = [-1, 0]
    BAIXO    = [1, 0]
    
    POSSIVEIS_DIRECOES = [DIREITA, BAIXO, ESQUERDA, CIMA]
    
    def __init__(self, labirinto: Labirinto) -> None:
        self.labirinto = labirinto

    def movimento(self, posicao: tuple, direcao: list) -> list:
        """
        Movimentação do robo
        Args:
            posicao (tuple): posição do robozinho
            direcao (list): direção a ser percorrida
        Returns:
            list: trajetória e posição do robo após o movimento
        """
        self.labirinto.LABIRINTO[posicao[0]][posicao[1]] = Labirinto.CAMINHO_PERCORRIDO
        self.labirinto.LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = Labirinto.ROBO
        return [posicao[0] + direcao[0], posicao[1] + direcao[1]]
        
    def verifica_movimento(self, posicao: tuple, direcao: list) -> bool: 
        """Verifica se a posição a ser movimentada é valida ou não
        Args:
            posicao (tuple): posição do robozinho
            direcao (list): direção a ser percorrida
        Returns:
            bool: False se encontrar parede ou caminho já percorrido
                True se caminho está livre ou encontrou a saída
        """
        
        possivel_caminho = self.labirinto.LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]]
            
        # Verifica se a direção não é parede e se não percorreu o caminho
        if possivel_caminho == self.labirinto.PAREDE:
            return False
        elif possivel_caminho == self.labirinto.CAMINHO_PERCORRIDO:
            return False
        elif possivel_caminho == self.labirinto.CAMINHO_LIVRE:
            return True
        elif possivel_caminho == self.labirinto.SAIDA:
            return True

    def resolve_labirinto(self):

        posicao_percorrida = [] 
        
        POSICAO_SAIDA = [9,18]
        
        print("\n***********************************************************************************************\n")
        print("BEM VINDO AO LABIRINTO CODE WARS!!\n\nVocê deverá escolher uma posição no labirinto e o seu robozinho irá procurar pela saída!\nEscolha dois números, sendo o primeiro entre 0 e 9 e o segundo entre 0 e 19.\nEstas coordenadas devem estar separadas por uma vírgula. Exemplo: 8, 15\nSe a posição que você escolher for uma parede do labirinto, será solicitado que você digite outro par de números.\n\nBOA SORTE!")
        print("\n***********************************************************************************************\n")

        tamanho_labirinto_linhas = len(self.labirinto.LABIRINTO)
        tamanho_labirinto_colunas = len(self.labirinto.LABIRINTO[0])
        
        posicao_valida = False

        while not posicao_valida:
            POSICAO_INICIAL = list(map(int, input("Digite uma posição para o Robô (linha, coluna): ").split(',')))
            if POSICAO_INICIAL[0] < tamanho_labirinto_linhas and POSICAO_INICIAL[1] < tamanho_labirinto_colunas:
            # verificar se a posição inicial é valida (se é diferente da parede ou saida) então coloca o robozinho
                valor_posicao_robo = self.labirinto.LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]]
                if valor_posicao_robo != self.labirinto.PAREDE and valor_posicao_robo != self.labirinto.SAIDA:
                    posicao_valida = True
                else:
                    print("Posição selecionada é inválida, tente novamente!")
            
        self.labirinto.LABIRINTO[POSICAO_SAIDA[0]][POSICAO_SAIDA[1]] = self.labirinto.SAIDA

        POSICAO_ATUAL = POSICAO_INICIAL 
        
        self.labirinto.print_labirinto()

        contador_direcoes = 0 
        
        posicao_percorrida.append(POSICAO_ATUAL)
        
        while POSICAO_ATUAL != POSICAO_SAIDA:
            
            for direcao in self.POSSIVEIS_DIRECOES:
                if contador_direcoes > 3:
                    #onde o robo travou
                    self.labirinto.LABIRINTO[posicao_percorrida[-1][0]][posicao_percorrida[-1][1]] = self.labirinto.CAMINHO_PERCORRIDO 
                    posicao_percorrida.pop()
                    # posição atual é igual a última possicao percorrida
                    POSICAO_ATUAL = posicao_percorrida[-1] 
                    self.labirinto.LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = self.labirinto.ROBO 
                    self.labirinto.print_labirinto() 
                    sleep(0.5)
                    contador_direcoes = 0

                contador_direcoes += 1
            
                if self.verifica_movimento(POSICAO_ATUAL, direcao): 
                    POSICAO_ATUAL = self.movimento(POSICAO_ATUAL, direcao)                 
                    posicao_percorrida.append(POSICAO_ATUAL)
                    contador_direcoes = 0
                    self.labirinto.print_labirinto()
                    sleep(0.5) 

        print("*********************")
        print("\n****   PARABÉNS  ****\n")
        print("\n*** ACHOU A SAIDA ***\n")
        print("*********************")

# if __name__ == "__main__":
#     main()