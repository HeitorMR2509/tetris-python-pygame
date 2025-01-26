import pygame
from settings import * 

# Função para configurar a malha do jogo
def desenhar_malha_setup(superficie_jogo):
    # Criar uma superfície para a malha
    superficie_malha = superficie_jogo.copy()
    superficie_malha.fill((0, 255, 0))
    superficie_malha.set_colorkey((0, 255, 0))
    superficie_malha.set_alpha(126)

    # Criar um retângulo para a superfície do jogo
    ret_jogo = superficie_jogo.get_rect(topleft=(PADDING, PADDING))

    return superficie_malha, ret_jogo

# Função para desenhar a malha na tela
def desenhar_malha_render(superficie_jogo, superficie_malha, ret_jogo):
    # Desenhar as linhas verticais
    for col in range(1, COLUMNS):
        x = col * CELL_SIZE
        pygame.draw.line(superficie_malha, LINE_COLOR, (x, 0), (x, superficie_malha.get_height()), 1)

    # Desenhar as linhas horizontais
    for row in range(1, ROWS):
        y = row * CELL_SIZE
        pygame.draw.line(superficie_malha, LINE_COLOR, (0, y), (superficie_malha.get_width(), y), 1)

    # Renderizar a malha na superfície do jogo
    superficie_jogo.blit(superficie_malha, (PADDING, PADDING))

# Exemplo de uso
if __name__ == "__main__":
    pygame.init()
    
    # Configurações da janela do jogo
    tela = pygame.display.set_mode((GAME_WIDTH + 2 * PADDING, GAME_HEIGHT + 2 * PADDING))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    # Superfície do jogo
    superficie_jogo = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
    superficie_malha, ret_jogo = desenhar_malha_setup(superficie_jogo)

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Preencher a superfície do jogo com a cor de fundo
        superficie_jogo.fill(GRAY)

        # Renderizar a malha
        desenhar_malha_render(superficie_jogo, superficie_malha, ret_jogo)

        # Exibir tudo na tela
        tela.fill((0, 0, 0))
        tela.blit(superficie_jogo, (PADDING, PADDING))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
