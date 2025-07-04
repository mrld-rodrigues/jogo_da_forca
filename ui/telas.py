import pygame
from .botao import Botao
from .popup import Popup

# Aqui você pode criar classes para telas como TelaInicio, TelaJogo, etc.
# Exemplo de esqueleto para TelaInicio:

class TelaInicio:
    def __init__(self, largura, altura, fonte_titulo, fonte_opcao, cor_fundo, cor_titulo, cor_opcao, cor_botao, cor_botao_texto):
        self.largura = largura
        self.altura = altura
        self.fonte_titulo = fonte_titulo
        self.fonte_opcao = fonte_opcao
        self.cor_fundo = cor_fundo
        self.cor_titulo = cor_titulo
        self.cor_opcao = cor_opcao
        self.cor_botao = cor_botao
        self.cor_botao_texto = cor_botao_texto

    def desenhar(self, tela, opcoes, selecionado, botao_creditos, botao_sair):
        tela.fill(self.cor_fundo)
        titulo = self.fonte_titulo.render('Jogo da Forca', True, self.cor_titulo)
        tela.blit(titulo, (self.largura//2 - titulo.get_width()//2, 80))
        subtitulo = self.fonte_opcao.render('Escolha a dificuldade:', True, self.cor_titulo)
        tela.blit(subtitulo, (self.largura//2 - subtitulo.get_width()//2, 180))
        total_altura = len(opcoes) * 60
        inicio_y = (self.altura // 2) - (total_altura // 2)
        for i, nome in enumerate(opcoes):
            cor = self.cor_opcao if i == selecionado else self.cor_titulo
            txt = self.fonte_opcao.render(nome, True, cor)
            tela.blit(txt, (self.largura//2 - txt.get_width()//2, inicio_y + i*60))
        # Botão de créditos
        pygame.draw.rect(tela, self.cor_botao, botao_creditos, border_radius=12)
        txt_creditos = self.fonte_opcao.render('Créditos', True, self.cor_botao_texto)
        tela.blit(txt_creditos, (botao_creditos.x + (botao_creditos.width-txt_creditos.get_width())//2, botao_creditos.y + (botao_creditos.height-txt_creditos.get_height())//2))
        # Botão de sair
        pygame.draw.rect(tela, self.cor_titulo, botao_sair, border_radius=12)
        txt_sair = self.fonte_opcao.render('Sair', True, self.cor_botao_texto)
        tela.blit(txt_sair, (botao_sair.x + (botao_sair.width-txt_sair.get_width())//2, botao_sair.y + (botao_sair.height-txt_sair.get_height())//2))
        pygame.display.flip()
