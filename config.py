import pygame

# Tamanho de jogo
COLUNAS = 10
LINHAS = 20
TAMANHO_DE_CELULA = 40
LARGURA_JOGO, COMPRIMENTO_JOGO = \
    COLUNAS * TAMANHO_DE_CELULA, LINHAS * TAMANHO_DE_CELULA

# Tamanho da barra lateral
LARGURA_BARRA_LATERAL = 200
FRACAO_COMPRIMENTO_VISUALIZACAO = 0.7
FRACAO_COMPRIMENTO_PONTUACAO = 1 - FRACAO_COMPRIMENTO_VISUALIZACAO

# Janela
ESPACAMENTO = 20
LARGURA_JANELA = LARGURA_JOGO + LARGURA_BARRA_LATERAL \
    + ESPACAMENTO * 3
COMPRIMENTO_JANELA = COMPRIMENTO_JOGO + ESPACAMENTO * 2

# Comportamento de jogo
VELOCIDADE_ATUALIZACAO_INICIAL = 400
TEMPO_ESPERA_MOVER = 200
TEMPO_ESPERA_ROTACIONAR = 200
ESPACAMENTO_BLOCO = pygame.Vector2(COLUNAS // 2, 5)

# Cores
AMARELO = "#f1e60d"
VERMELHO = "#e51b20"
AZUL = "#204b9b"
VERDE = "#65b32e"
ROXO = "#7b217f"
CIANO = "#6cc6d9"
LARANJA = "#f07e13"
CINZA = "#1c1c1c"
COR_LINHA = "#FFFFFF"

# Formas
TETROMINOS = {
    "T": {"forma": [(0, 0), (-1, 0), (1, 0), (0, -1)], "cor": ROXO},
    "O": {"forma": [(0, 0), (0, -1), (1, 0), (1, -1)], "cor": AMARELO},
    "J": {"forma": [(0, 0), (0, -1), (0, 1), (-1, 1)], "cor": AZUL},
    "L": {"forma": [(0, 0), (0, -1), (0, 1), (1, 1)], "cor": LARANJA},
    "I": {"forma": [(0, 0), (0, -1), (0, -2), (0, 1)], "cor": CIANO},
    "S": {"forma": [(0, 0), (-1, 0), (0, -1), (1, -1)], "cor": VERDE},
    "Z": {"forma": [(0, 0), (1, 0), (0, -1), (-1, -1)], "cor": VERMELHO}
}

DADO_PONTUACAO = [None, 40, 100, 300, 1200]
