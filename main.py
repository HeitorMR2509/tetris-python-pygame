# Configurações e bibliotecas importadas
from config import *

def main() -> None:
    pygame.init()

    rodando = True

    # Cria uma superfície da janela
    janela = pygame.display.set_mode(
        (LARGURA_JANELA, COMPRIMENTO_JANELA)
    )

    pygame.display.set_caption("Tetris")

    # Criação de um "relógio" para FPS e tempo
    relogio = pygame.time.Clock()

    # Criação do jogo
    ## Superfície do jogo
    superficie_jogo = pygame.Surface(
        (LARGURA_JOGO, COMPRIMENTO_JOGO)
    )

    # Criação da parte de pontuação
    ## Superfície da pontuação
    superficie_pontuacao = pygame.Surface(
        (LARGURA_BARRA_LATERAL,
         COMPRIMENTO_JOGO * FRACAO_COMPRIMENTO_PONTUACAO - ESPACAMENTO)
    )


    ## Retângulo pontuação
    ret_pont = superficie_pontuacao.get_rect(
        bottomright=(
            LARGURA_JANELA - ESPACAMENTO,
            COMPRIMENTO_JANELA - ESPACAMENTO
        )
    )

    # Criação da parte da pré-visualização de blocos
    ## Superfície da pré-visualização
    superficie_previsualizacao = pygame.Surface(
        (LARGURA_BARRA_LATERAL,
         COMPRIMENTO_JOGO * FRACAO_COMPRIMENTO_VISUALIZACAO)
    )

    ## Retângulo pré-visualização
    ret_preview = superficie_previsualizacao.get_rect(
        topright=(
            LARGURA_JANELA - ESPACAMENTO,
            ESPACAMENTO
        )
    )

    while rodando:

        # Muda cor de fundo da janela
        janela.fill(CINZA)

        # Adiciona a superfície do jogo na janela
        janela.blit(superficie_jogo, (ESPACAMENTO, ESPACAMENTO))

        # Adiciona a superfície da pontuação na janela
        janela.blit(superficie_pontuacao, ret_pont)

        # Adiciona a superfície de pré-visualização de bloco
        janela.blit(superficie_previsualizacao, ret_preview)

        pygame.display.update()

        # Ritmo de atualização. None=máximo possível e parâmetro 
        # é o fps
        relogio.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

    # Limpa a "tralha" da biblioteca/desinicializa
    pygame.quit()


if __name__ == "__main__":
    main()
