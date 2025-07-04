import pygame
from config import PRETO

class ForcaDesenhavel:
    """Classe para desenhar a forca e o boneco."""
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def desenhar(self, tela, erros):
        base_x = (self.largura // 2) - 100
        base_y = self.altura - 250
        altura = 200
        largura = 100
        # Base
        pygame.draw.line(tela, PRETO, (base_x, base_y), (base_x + largura, base_y), 6)
        pygame.draw.line(tela, PRETO, (base_x + largura//2, base_y), (base_x + largura//2, base_y - altura), 6)
        pygame.draw.line(tela, PRETO, (base_x + largura//2, base_y - altura), (base_x + largura + 30, base_y - altura), 6)
        pygame.draw.line(tela, PRETO, (base_x + largura + 30, base_y - altura), (base_x + largura + 30, base_y - altura + 30), 6)
        # Cabeça
        if erros > 0:
            pygame.draw.circle(tela, PRETO, (base_x + largura + 30, base_y - altura + 60), 20, 4)
        # Tronco
        if erros > 1:
            pygame.draw.line(tela, PRETO, (base_x + largura + 30, base_y - altura + 80), (base_x + largura + 30, base_y - altura + 140), 4)
        # Braço esquerdo
        if erros > 2:
            pygame.draw.line(tela, PRETO, (base_x + largura + 30, base_y - altura + 90), (base_x + largura + 5, base_y - altura + 110), 4)
        # Braço direito
        if erros > 3:
            pygame.draw.line(tela, PRETO, (base_x + largura + 30, base_y - altura + 90), (base_x + largura + 55, base_y - altura + 110), 4)
        # Perna esquerda
        if erros > 4:
            pygame.draw.line(tela, PRETO, (base_x + largura + 30, base_y - altura + 140), (base_x + largura + 5, base_y - altura + 180), 4)
        # Perna direita
        if erros > 5:
            pygame.draw.line(tela, PRETO, (base_x + largura + 30, base_y - altura + 140), (base_x + largura + 55, base_y - altura + 180), 4)
