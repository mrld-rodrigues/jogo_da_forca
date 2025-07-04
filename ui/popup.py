import pygame
import sys

class Popup:
    def __init__(self, largura, altura, fonte_titulo, fonte_texto, cor_fundo, cor_borda, cor_texto):
        self.largura = largura
        self.altura = altura
        self.fonte_titulo = fonte_titulo
        self.fonte_texto = fonte_texto
        self.cor_fundo = cor_fundo
        self.cor_borda = cor_borda
        self.cor_texto = cor_texto

    def mostrar(self, tela, titulo, linhas, instrucoes=None):
        popup_x = (tela.get_width() - self.largura) // 2
        popup_y = (tela.get_height() - self.altura) // 2
        popup = pygame.Surface((self.largura, self.altura))
        popup.fill(self.cor_fundo)
        pygame.draw.rect(popup, self.cor_borda, (0, 0, self.largura, self.altura), 4)
        y = 40
        t = self.fonte_titulo.render(titulo, True, self.cor_texto)
        popup.blit(t, (self.largura//2 - t.get_width()//2, y))
        y += 50
        for linha in linhas:
            l = self.fonte_texto.render(linha, True, self.cor_texto)
            popup.blit(l, (self.largura//2 - l.get_width()//2, y))
            y += 40
        if instrucoes:
            i = self.fonte_texto.render(instrucoes, True, self.cor_texto)
            popup.blit(i, (self.largura//2 - i.get_width()//2, self.altura - 60))
        tela.blit(popup, (popup_x, popup_y))
        pygame.display.flip()
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN or evento.type == pygame.QUIT:
                    esperando = False
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

class PopupOpcoes:
    def __init__(self, largura, altura, fonte, cor_fundo, cor_borda, cor_texto, cor_botao, cor_botao_texto):
        self.largura = largura
        self.altura = altura
        self.fonte = fonte
        self.cor_fundo = cor_fundo
        self.cor_borda = cor_borda
        self.cor_texto = cor_texto
        self.cor_botao = cor_botao
        self.cor_botao_texto = cor_botao_texto

    def mostrar(self, tela):
        popup_x = (tela.get_width() - self.largura) // 2
        popup_y = (tela.get_height() - self.altura) // 2
        popup = pygame.Surface((self.largura, self.altura))
        popup.fill(self.cor_fundo)
        pygame.draw.rect(popup, self.cor_borda, (0, 0, self.largura, self.altura), 4)
        titulo = self.fonte.render('Escolha uma opção:', True, self.cor_texto)
        popup.blit(titulo, (self.largura//2 - titulo.get_width()//2, 30))
        botoes = [
            ("Tela Inicial", (self.largura//2 - 100, 80, 200, 50)),
            ("Fechar Jogo", (self.largura//2 - 100, 140, 200, 50)),
        ]
        for nome, rect in botoes:
            pygame.draw.rect(popup, self.cor_botao if nome == "Tela Inicial" else (255,0,0), rect, border_radius=10)
            txt = self.fonte.render(nome, True, self.cor_botao_texto)
            popup.blit(txt, (rect[0] + (200-txt.get_width())//2, rect[1] + (50-txt.get_height())//2))
        tela.blit(popup, (popup_x, popup_y))
        pygame.display.flip()
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = evento.pos[0] - popup_x, evento.pos[1] - popup_y
                    for i, (_, rect) in enumerate(botoes):
                        rx, ry, rw, rh = rect
                        if rx <= mx <= rx+rw and ry <= my <= ry+rh:
                            if i == 0:
                                return 'inicio'
                            elif i == 1:
                                pygame.quit()
                                sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return None
