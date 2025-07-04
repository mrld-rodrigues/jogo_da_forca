import pygame

class Botao:
    def __init__(self, rect, texto, fonte, cor_fundo, cor_texto, border_radius=10):
        self.rect = pygame.Rect(rect)
        self.texto = texto
        self.fonte = fonte
        self.cor_fundo = cor_fundo
        self.cor_texto = cor_texto
        self.border_radius = border_radius

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor_fundo, self.rect, border_radius=self.border_radius)
        txt = self.fonte.render(self.texto, True, self.cor_texto)
        tela.blit(txt, (self.rect.x + (self.rect.width-txt.get_width())//2, self.rect.y + (self.rect.height-txt.get_height())//2))

    def clicado(self, pos):
        return self.rect.collidepoint(pos)
