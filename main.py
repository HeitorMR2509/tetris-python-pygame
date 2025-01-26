# Configurações e bibliotecas importadas
from config import *

from random import choice

# Tetraminó
from util.Tetramino import Tetramino

# Temporizador
from util.Temporizador import Temporizador

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

    ## Grupo de blocos
    blocos = pygame.sprite.Group()

    # Tetraminó de início, escolhido aleatoriamente
    t = Tetramino(choice(list(TETROMINOS.keys())), blocos)

    # Funções de modificação do tetraminó
    def mover_para_baixo() -> None:
        t.mover_para_baixo()

    # Temporizadores para movimentação
    temporizadores = {
        "movimento vertical": Temporizador(
            VELOCIDADE_ATUALIZACAO_INICIAL,
            True,
            mover_para_baixo 
        )
    }

    # Ativa o temporizador de movimento vertical
    temporizadores["movimento vertical"].ativar()

    # Laço de repetição principal do jogo
    while rodando:
        # Eventos principais do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        # Muda cor de fundo da janela
        janela.fill(CINZA)

        # Adiciona a superfície do jogo na janela
        janela.blit(superficie_jogo, (ESPACAMENTO, ESPACAMENTO))

        # Adiciona a superfície da pontuação na janela
        janela.blit(superficie_pontuacao, ret_pont)

        # Adiciona a superfície de pré-visualização de bloco
        janela.blit(superficie_previsualizacao, ret_preview)

        # Cor da superfície do jogo
        superficie_jogo.fill("black")

        # Atualiza os temporizadores
        for temporizador in temporizadores.values():
            temporizador.atualizar()

        # Atualiza os blocos
        blocos.update()

        # Desenha os blocos
        blocos.draw(superficie_jogo)

        # Ritmo de atualização. None=máximo possível; e parâmetro 
        # é o fps
        relogio.tick()

        # Atualiza a superfície da janela
        pygame.display.update()


    # Limpa a "tralha" da biblioteca/desinicializa
    pygame.quit()


if __name__ == "__main__":
    main()
