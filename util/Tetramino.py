from config import *

from .Bloco import Bloco

class Tetramino:
    def __init__(self, forma, grupo):

        # Posição dos blocos para formar o tetraminó
        self.posicao_blocos = TETROMINOS[forma]["forma"]
        
        # Cor do tetraminó
        self.cor = TETROMINOS[forma]["cor"]

        # Blocos do tetraminó
        self.blocos = [Bloco(grupo, posicao, self.cor) for posicao in self.posicao_blocos]

    def mover_para_baixo(self):
        for bloco in self.blocos:
            bloco.posicao.y += 1

    def mover_horizontal(self, amount):
        for bloco in self.blocos:
            bloco.posicao.x += amount
