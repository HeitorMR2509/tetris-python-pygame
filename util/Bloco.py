from config import *

class Bloco(pygame.sprite.Sprite):
    def __init__(self, grupo, posicao, cor):
        # Inicia o construtor da classe Sprite e
        # adiciona o bloco ao grupo de blocos
        if grupo:
            super().__init__(grupo)
        else:
            super().__init__()

        # Superfície do bloco
        self.image = pygame.Surface(
            (
                TAMANHO_DE_CELULA,
                TAMANHO_DE_CELULA
            )
        )

        # Superfície do bloco vermelha
        self.image.fill(cor)

        # Posição do bloco
        self.posicao = pygame.Vector2(posicao) + ESPACAMENTO_BLOCO

        # Retângulo da superfície do bloco
        self.rect = self.image.get_rect(
            topleft=self.posicao * TAMANHO_DE_CELULA
        )

    # Rotaciona o bloco em torno de um bloco eixo
    def rotacionar(self, bloco_eixo):
        return bloco_eixo.posicao + (self.posicao - bloco_eixo.posicao).rotate(90)

    # Detecta se a posição do bloco está 
    # fora da área de jogo determinada nas configurações
    # ou se está colidindo com outro bloco
    def colisao_horizontal(self, x, blocos_colisao):
        return (not 0 <= x < COLUNAS) or blocos_colisao[int(self.posicao.y)][x]

    # Detecta se o bloco está fora da área de jogo 
    # na vertical ou está colidindo com outro bloco
    def colisao_vertical(self, y, blocos_colisao):
        return (not 0 <= y < LINHAS) or blocos_colisao[y][int(self.posicao.x)]

    # Atualiza a posição do bloco
    def update(self):
        self.rect.x = self.posicao.x * TAMANHO_DE_CELULA
        self.rect.y = self.posicao.y * TAMANHO_DE_CELULA


