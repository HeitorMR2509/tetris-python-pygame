from config import *

class Temporizador:
    def __init__(self, duracao, repetir = False, funcao = None):
        # Atributor iniciais do temporizador
        self.duracao = duracao
        self.repetir = repetir
        self.funcao = funcao

        self.tempo_inicial = 0
        self.ativo = False

    def ativar(self):
        # Ativa o temporizador
        self.ativo = True

        # Pega o tempo atual da aplicação como tempo inicial do temporizador
        self.tempo_inicial = pygame.time.get_ticks()

    def desativar(self):
        # Desativa o temporizador
        self.ativo = False

        # Reinicia o tempo do temporizador
        self.tempo_inciial = 0

    def atualizar(self):
        # Pega o tempo atual da aplicação Pygame
        tempo_atual = pygame.time.get_ticks()

        # Checa se o tempo de ducação foi elapsado quando o temporizador
        # está ativo
        if tempo_atual - self.tempo_inicial >= self.duracao and self.ativo:

            # Chama a função definida para o temporizador
            if self.funcao and self.tempo_inicial != 0:
                self.funcao()

            # Se o tempo estiver elapsado, desativa o temporizador e reinicia
            # o tempo inicial
            self.desativar()


            # Repetir o temporizador se for para repetir
            if self.repetir:
                self.ativar()

