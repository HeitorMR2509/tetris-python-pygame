from config import *

class Bloco(pygame.sprite.Sprite):
    def __init__(self, grupo, posicao, cor):
        # Inicia o construtor da classe Sprite e
        # adiciona o bloco ao grupo de blocos
        super().__init__(grupo)

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

    def update(self):
        self.rect.x = self.posicao.x * TAMANHO_DE_CELULA
        self.rect.y = self.posicao.y * TAMANHO_DE_CELULA


