from config import *

from .Bloco import Bloco

class Tetramino:
    def __init__(self, forma, grupo, blocos_colisao):
        # Forma do tetraminó
        self.forma = forma

        # Posição dos blocos para formar o tetraminó
        self.posicao_blocos = TETROMINOS[forma]["forma"]
        
        # Cor do tetraminó
        self.cor = TETROMINOS[forma]["cor"]

        # Blocos do tetraminó
        self.blocos = [Bloco(grupo, posicao, self.cor) for posicao in self.posicao_blocos]

        # Blocos para colisão
        self.blocos_colisao = blocos_colisao

    # Rotaciona o tetraminó
    def rotacionar(self):
        if self.forma != "O":
            bloco_eixo = self.blocos[0]

            posicao_blocos_nova = [bloco.rotacionar(bloco_eixo) for bloco in self.blocos]

            # checar colisão
            for posicao in posicao_blocos_nova:
                if posicao.x < 0 or posicao.x >= COLUNAS:
                    return
                
                if self.blocos_colisao[int(posicao.y)][int(posicao.x)]:
                    return

                if posicao.y > LINHAS:
                    return

            for i, bloco in enumerate(self.blocos):
                bloco.posicao = posicao_blocos_nova[i]

    def mover_para_baixo(self, func=None):
        # Checa se o tetraminó está fora da área de jogo
        if not self.colisao_proximo_movimento_vertical(self.blocos, 1):
            # Move os blocos do tetraminó
            for bloco in self.blocos:
                bloco.posicao.y += 1
        else:
            # Cria novo tetraminó
            if func:
                for bloco in self.blocos:
                    self.blocos_colisao[int(bloco.posicao.y)][int(bloco.posicao.x)] = bloco
                func()

    def mover_horizontal(self, amount):
        # Move horizontalmente se não for sair da 
        # superfície de jogo
        if not self.colisao_proximo_movimento_horizontal(self.blocos, amount):
            # Move todos os blocos do tetraminó
            # por uma certa quantidade amount
            for bloco in self.blocos:
                bloco.posicao.x += amount


    def colisao_proximo_movimento_vertical(self, blocos, amount):
        # Tetraminó imaginário para detectar saída da área 
        # de jogo
        lista_colisao = \
            [bloco.colisao_vertical(int(bloco.posicao.y + amount), self.blocos_colisao) for bloco in blocos]

        # Checa e retorna se algum bloco está fora da área 
        # de jogo
        return any(lista_colisao)


    def colisao_proximo_movimento_horizontal(self, blocos, amount):
        # Tetraminó imaginário para checar se o tetraminó sai 
        # da superfície do jogo
        lista_colisao = \
            [bloco.colisao_horizontal(int(bloco.posicao.x + amount), self.blocos_colisao) for bloco in blocos]

        # Retorna se algum dos blocos do tetraminó imaginário 
        # está fora da superfície de jogo
        return any(lista_colisao)
