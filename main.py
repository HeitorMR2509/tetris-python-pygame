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

    while rodando:

        # Muda cor de fundo da janela
        janela.fill(CINZA)

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
