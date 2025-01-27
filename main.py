# Configurações e bibliotecas importadas
from config import *

from random import choice

# Tetraminó
from util.Tetramino import Tetramino

# Temporizador
from util.Temporizador import Temporizador

# Malha da superfície do jogo
from colab1.desenhar_malha import *

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

    # Malha da superfície do jogo
    superficie_malha, ret_jogo = \
        desenhar_malha_setup(superficie_jogo)

    ## Grupo de blocos
    blocos = pygame.sprite.Group()

    # Blocos para colisão de tetraminós
    blocos_colisao = [[0 for x in range(COLUNAS)] for y in range(LINHAS)]

    # Tetraminó de início, escolhido aleatoriamente
    t = Tetramino(choice(list(TETROMINOS.keys())), blocos, blocos_colisao)

    # Função que cria um novo tetraminó
    def criar_novo_tetramino() -> None:
        nonlocal blocos_colisao

        # Checar linhas completas
        linhas_deletar = []

        # Adiciona as linhas que podem ser deletadas
        for i, linha in enumerate(blocos_colisao):
            if all(linha):
                linhas_deletar.append(i)

        # Se existir uma linha para deletar
        if linhas_deletar:
            for linha_deletar in linhas_deletar:
                # Deleta a linha inteira
                for bloco in blocos_colisao[linha_deletar]:
                    bloco.kill()

                # Mover os blocos para baixo
                for linha in blocos_colisao:
                    for bloco in linha:
                        if bloco and bloco.posicao.y < linha_deletar:
                            bloco.posicao.y += 1


            # Reconstruir os blocos de colisao para atualizar 
            # o campo invisível lógico do jogo
            blocos_colisao = [[0 for x in range(COLUNAS)] for y in range(LINHAS)]

            for bloco in blocos:
                blocos_colisao[int(bloco.posicao.y)][int(bloco.posicao.x)] = bloco


        # Cria um novo tetraminó, o qual está 
        # em uma variável no escopo da função pai
        nonlocal t
        t = Tetramino(choice(list(TETROMINOS.keys())), blocos, blocos_colisao)

    # Funções de modificação do tetraminó
    def mover_para_baixo() -> None:
        t.mover_para_baixo(criar_novo_tetramino)

    # Temporizadores para movimentação
    temporizadores = {
        "movimento vertical": Temporizador(
            VELOCIDADE_ATUALIZACAO_INICIAL,
            True,
            mover_para_baixo 
        ),
        "movimento horizontal": Temporizador(
            TEMPO_ESPERA_MOVER
        ),
        "rotacionar": Temporizador(
            TEMPO_ESPERA_ROTACIONAR
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

        # Superfície da malha do jogo
        desenhar_malha_render(
            superficie_jogo,
            superficie_malha,
            ret_jogo
        )

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

        # Entrada de usuário
        tecla = pygame.key.get_pressed()

        ## Movimentação do tetraminó
        if not temporizadores["movimento horizontal"].ativo:
            if tecla[pygame.K_d]:
                t.mover_horizontal(1)
                temporizadores["movimento horizontal"].ativar()

            if tecla[pygame.K_a]:
                t.mover_horizontal(-1)
                temporizadores["movimento horizontal"].ativar()

        ## Rotacionar o tetraminó
        if not temporizadores["rotacionar"].ativo:
            if tecla[pygame.K_w]:
                t.rotacionar()
                temporizadores["rotacionar"].ativar()


    # Limpa a "tralha" da biblioteca/desinicializa
    pygame.quit()


if __name__ == "__main__":
    main()
