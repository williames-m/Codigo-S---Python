
class Labirinto:
    
    PAREDE = '#'
    CAMINHO_LIVRE = ' '
    CAMINHO_PERCORRIDO = '-'
    ROBO = 'R'
    SAIDA = 'S'

    def __init__(self, mapa):
        self.LABIRINTO = mapa
    
    def print_labirinto(self) -> None:
        """Imprime o desenho do labirinto
        
        Returns: None
        """

        print("")
        for linha in self.LABIRINTO:
            print("".join(linha))
        print("")
