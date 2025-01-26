from config import * 

# Função para configurar a malha do jogo
def desenhar_malha_setup(superficie_jogo):
    # Criar uma superfície para a malha
    superficie_malha = superficie_jogo.copy()
    superficie_malha.fill((0, 255, 0))
    superficie_malha.set_colorkey((0, 255, 0))
    superficie_malha.set_alpha(126)

    # Criar um retângulo para a superfície do jogo
    ret_jogo = superficie_jogo.get_rect()

    return superficie_malha, ret_jogo

# Função para desenhar a malha na tela
def desenhar_malha_render(superficie_jogo, superficie_malha, ret_jogo):
    # Desenhar as linhas verticais
    for col in range(1, COLUNAS):
        x = col * TAMANHO_DE_CELULA
        pygame.draw.line(superficie_malha, COR_LINHA, (x, 0), (x, superficie_malha.get_height()), 1)

    # Desenhar as linhas horizontais
    for row in range(1, LINHAS):
        y = row * TAMANHO_DE_CELULA
        pygame.draw.line(superficie_malha, COR_LINHA, (0, y), (superficie_malha.get_width(), y), 1)

    # Renderizar a malha na superfície do jogo
    superficie_jogo.blit(superficie_malha, (0, 0))

    # Desenha as linhas externas da área de jogo
    pygame.draw.rect(superficie_jogo, COR_LINHA, ret_jogo, 2, 2)

