# Permite colocar todas as variáveis globais e 
# bibliotecas importadas em outro arquivo.
from config import *

def main() -> None:
    # Configuração geral
    # Inicia o Pygame
    pygame.init()

    # Variável de continuidade
    rodando = True

    # Cria uma superfície da janela
    janela_superficie = pygame.display.set_mode(
        (LARGURA_JANELA, COMPRIMENTO_JANELA)
    )

    # Muda título da janela
    pygame.display.set_caption("Tetris")

    # Criação de um "relógio" para FPS e tempo
    relogio = pygame.time.Clock()

    # Repetição do jogo
    while rodando:

        # Muda cor de fundo da janela
        janela_superficie.fill(CINZA)

        # Atualiza a janela
        pygame.display.update()

        # Ritmo de atualização. None=máximo possível e parâmetro 
        # é o fps
        relogio.tick()

        # Lida com eventos do Pygame
        for event in pygame.event.get():
            # Evento de fechar janela
            if event.type == pygame.QUIT:
                rodando = False


if __name__ == "__main__":
    main()
