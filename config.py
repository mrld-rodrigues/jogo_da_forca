# Configurações globais do jogo (cores, fontes, dimensões)
import pygame

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 200, 0)
CINZA_CLARO = (240, 240, 240)

# Fontes (padrão, pode ser ajustado conforme necessidade)
def get_fontes():
    pygame.font.init()
    fonte = pygame.font.SysFont('arial', 72)
    fonte_pequena = pygame.font.SysFont('arial', 48)
    fonte_popup = pygame.font.SysFont('arial', 48)
    fonte_pequena_popup = pygame.font.SysFont('arial', 32)
    return fonte, fonte_pequena, fonte_popup, fonte_pequena_popup

# Dimensões padrão de botões, popups, etc.
BOTAO_OPCOES = (260, 80)
BOTAO_MENU = (220, 60)
POPUP_CREDITOS = (1000, 500)
POPUP_OPCOES = (500, 220)
