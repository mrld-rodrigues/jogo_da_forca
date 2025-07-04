import pygame
import math

def gradiente_animado(tela, largura, altura, grad_y):
    """Desenha um gradiente animado de fundo na tela."""
    for y in range(altura):
        cor = (20 + int(30 * abs(math.sin((y+grad_y)/80))), 20, 40 + int(60 * abs(math.cos((y+grad_y)/120))))
        pygame.draw.line(tela, cor, (0, y), (largura, y))

def efeito_flashes(tela, flashes):
    """Desenha flashes/brilhos na tela."""
    for fx, fy, fr in flashes:
        pygame.draw.circle(tela, (255,255,255,80), (fx, fy), fr)
    # Retorna lista de flashes atualizada (diminui o raio)
    return [(fx, fy, max(4, fr-4)) for (fx, fy, fr) in flashes if fr > 4]
