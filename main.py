# Configurações e bibliotecas importadas
from config import *

from random import choice

# Tetraminó
from util.Tetramino import Tetramino

# Temporizador
from util.Temporizador import Temporizador

# Malha da superfície do jogo
from colab1.desenhar_malha import *

# Caminho de arquivo
from os import path

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

    ## Dados da pontuação
    nivel_atual = 1
    pontuacao_atual = 0
    linhas_atuais = 0

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

    ## Gráficos de pré-visualização dos blocos
    superficies_blocos = {forma: pygame.image.load(path.join("assets", "graficos", f"{forma}.png")).convert_alpha() for forma in TETROMINOS.keys()}

    # Malha da superfície do jogo
    superficie_malha, ret_jogo = \
        desenhar_malha_setup(superficie_jogo)

    ## Grupo de blocos
    blocos = pygame.sprite.Group()

    # Blocos para colisão de tetraminós
    blocos_colisao = [[0 for x in range(COLUNAS)] for y in range(LINHAS)]

    # Tetraminós de pré-visualização
    ts = [Tetramino(choice(list(TETROMINOS.keys())), blocos, blocos_colisao) for _ in range(3)]

    def get_t():
        nonlocal ts
        nonlocal blocos
        nonlocal blocos_colisao
        t = ts.pop(0)
        ts.append(Tetramino(choice(list(TETROMINOS.keys())), blocos, blocos_colisao))
        t.add_grupo(blocos)
        t.add_blocos_colisao(blocos_colisao)
        return t

    # Tetraminó de início, escolhido aleatoriamente
    t = get_t() 

    # Função que cria um novo tetraminó
    def criar_novo_tetramino():
        nonlocal blocos_colisao
        nonlocal blocos

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

        
            # Calcular pontuação
            nonlocal nivel_atual
            nonlocal linhas_atuais
            nonlocal pontuacao_atual
            num_linhas = len(linhas_deletar)
            linhas_atuais += num_linhas
            pontuacao_atual += DADO_PONTUACAO[num_linhas] * nivel_atual

            if linhas_atuais / 10 > nivel_atual:
                nonlocal velocidade_vertical
                nonlocal velocidade_vertical_acelerada
                nonlocal temporizadores
                nivel_atual += 1
                velocidade_vertical *= 0.75
                velocidade_vertical_acelerada = velocidade_vertical * 0.3
                temporizadores["movimento vertical"].duracao = velocidade_vertical

        # Cria um novo tetraminó, o qual está 
        # em uma variável no escopo da função pai
        nonlocal t
        t = get_t()

    # Funções de modificação do tetraminó
    def mover_para_baixo() -> None:
        nonlocal t
        nonlocal blocos_colisao
        t.mover_para_baixo(criar_novo_tetramino)

    # Velocidade vertical 
    velocidade_vertical = VELOCIDADE_ATUALIZACAO_INICIAL
    velocidade_vertical_acelerada = velocidade_vertical * 0.3

    # Para acelerar velocidade vertical
    apertado = False

    # Temporizadores para movimentação
    temporizadores = {
        "movimento vertical": Temporizador(
            velocidade_vertical,
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

    # Para a pontuação
    fonte = pygame.font.Font(path.join("assets", "graficos", "Russo_One.ttf"), 18)

    altura_incrementada = superficie_pontuacao.get_height() / 3


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

        # Mexe com a superfície de pontuação
        superficie_pontuacao.fill(CINZA)

        # Linha externa da superfície de pontuação
        pygame.draw.rect(superficie_pontuacao, COR_LINHA, superficie_pontuacao.get_rect(), 2, 2)

        ## Dados da pontuação atualizados na superfície de pontuação
        for i, texto in enumerate([("Pontuação", pontuacao_atual), ("Nível", nivel_atual), ("Linhas", linhas_atuais)]):
            x = superficie_pontuacao.get_width() / 2
            y = altura_incrementada * (i + 1/2)

            superficie_texto = fonte.render(f"{texto[0]}: {texto[1]}", True, "white")
            ret_texto = superficie_texto.get_rect(center=(x, y))

            superficie_pontuacao.blit(superficie_texto, ret_texto)


        # Adiciona a superfície de pré-visualização de bloco
        janela.blit(superficie_previsualizacao, ret_preview)

        # Cor da superfície de pré-visualização de blocos
        superficie_previsualizacao.fill(CINZA)

        # Linha exterior da supefície de pré-visualização
        pygame.draw.rect(superficie_previsualizacao, COR_LINHA, superficie_previsualizacao.get_rect(), 2, 2)

        for i, forma in enumerate(ts):
            forma_s = superficies_blocos[forma.forma]
            x = superficie_previsualizacao.get_width() / 2
            y = superficie_previsualizacao.get_height() / 3 * (1/2 + i)
            ret = forma_s.get_rect(center=(x, y))
            superficie_previsualizacao.blit(forma_s, ret)
        
        # Cor da superfície do jogo
        superficie_jogo.fill(CINZA)

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

        ## Acelerar velocidade de descida
        if not apertado and tecla[pygame.K_s]:
            apertado = True
            temporizadores["movimento vertical"].duracao = velocidade_vertical_acelerada

        if apertado and not tecla[pygame.K_s]:
            apertado = False
            temporizadores["movimento vertical"].duracao = velocidade_vertical


    # Limpa a "tralha" da biblioteca/desinicializa
    pygame.quit()


if __name__ == "__main__":
    main()
