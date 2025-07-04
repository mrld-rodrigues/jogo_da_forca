import pygame
import sys
from palavras import palavra_facil, palavra_normal, palavra_dificil, palavra_secreta
from jogo_forca import JogoForca
import random
import math
from ui.telas import TelaInicio
from ui.popup import Popup, PopupOpcoes
from config import BRANCO, PRETO, VERMELHO, VERDE, CINZA_CLARO, get_fontes, BOTAO_OPCOES, BOTAO_MENU, POPUP_CREDITOS, POPUP_OPCOES
from ui.efeitos import gradiente_animado, efeito_flashes
from ui.forca import ForcaDesenhavel


def escolher_lista() -> list:
    """Escolhe aleatoriamente uma lista de palavras para o jogo."""
    opcoes = [palavra_facil, palavra_normal, palavra_dificil, palavra_secreta]
    return random.choice(opcoes)

pygame.init()
info = pygame.display.Info()
LARGURA, ALTURA = info.current_w, info.current_h
flags = pygame.FULLSCREEN

tela = pygame.display.set_mode((LARGURA, ALTURA), flags)
pygame.display.set_caption('Jogo da Forca - Pygame')
fonte, fonte_pequena, fonte_popup, fonte_pequena_popup = get_fontes()

# Classe para gerenciar a exibição da forca
forca_ui = ForcaDesenhavel(LARGURA, ALTURA)


def mostrar_creditos() -> None:
    """Exibe o popup de créditos do jogo."""
    popup = Popup(1000, 500, fonte_pequena_popup, fonte_pequena_popup, (240,240,240), PRETO, PRETO)
    linhas = [
        'Desenvolvido por:',
        'Amiraldo Almeida',
        'Python 3 + pygame',
        'Jogo da Forca - 2025',
        'Objetivo:',
        'Descubra a palavra secreta antes de ser enforcado!'
    ]
    popup.mostrar(tela, '', linhas, 'Pressione qualquer tecla para fechar')


def mostrar_opcoes() -> str | None:
    """Exibe o popup de opções e retorna a ação escolhida."""
    popup = PopupOpcoes(500, 220, fonte_pequena_popup, (240,240,240), PRETO, PRETO, PRETO, BRANCO)
    return popup.mostrar(tela)


def tela_inicio() -> list:
    """Exibe a tela inicial e retorna a lista de palavras escolhida pelo usuário."""
    selecionado = 0
    opcoes = [
        ("Fácil", palavra_facil),
        ("Normal", palavra_normal),
        ("Difícil", palavra_dificil),
        ("Secreta", palavra_secreta)
    ]
    nomes_opcoes = [nome for nome, _ in opcoes]
    tela_inicio_ui = TelaInicio(LARGURA, ALTURA, fonte, fonte_pequena, BRANCO, PRETO, VERDE, VERMELHO, BRANCO)
    botao_creditos = pygame.Rect(LARGURA - 260, ALTURA - 90, 220, 60)
    botao_sair = pygame.Rect(40, ALTURA - 90, 220, 60)
    while True:
        tela_inicio_ui.desenhar(tela, nomes_opcoes, selecionado, botao_creditos, botao_sair)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    selecionado = (selecionado - 1) % len(opcoes)
                elif evento.key == pygame.K_DOWN:
                    selecionado = (selecionado + 1) % len(opcoes)
                elif evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
                    return opcoes[selecionado][1]
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_creditos.collidepoint(evento.pos):
                    mostrar_creditos()
                if botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()


def tela_abertura() -> None:
    """Exibe a tela de abertura com efeito animado."""
    tempo_inicial = pygame.time.get_ticks()
    duracao_efeito = 2200  # 2.2 segundos de efeito
    duracao_titulo = 1200  # 1.2 segundos mostrando o título completo
    rodando = True
    efeito_finalizado = False
    titulo_str = 'Jogo da Forca'
    letras_titulo = list(titulo_str)
    letras_mostradas = 0
    tempo_letra = 80  # ms entre cada letra
    flashes = []
    grad_y = 0
    while rodando:
        gradiente_animado(tela, LARGURA, ALTURA, grad_y)
        grad_y += 2
        tempo_atual = pygame.time.get_ticks() - tempo_inicial
        if random.random() < 0.08:
            flashes.append((random.randint(0, LARGURA), random.randint(0, ALTURA), random.randint(32, 64)))
        flashes = efeito_flashes(tela, flashes)
        if tempo_atual < duracao_efeito:
            letras_mostradas = min(len(letras_titulo), int(tempo_atual/tempo_letra))
            titulo = ''.join(letras_titulo[:letras_mostradas])
            texto = fonte.render(titulo, True, VERMELHO)
            tela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 - texto.get_height()//2))
        else:
            if not efeito_finalizado:
                efeito_finalizado = True
                tempo_titulo = pygame.time.get_ticks()
            texto = fonte.render(titulo_str, True, VERMELHO)
            tela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 - texto.get_height()//2))
            if pygame.time.get_ticks() - tempo_titulo > duracao_titulo:
                rodando = False
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


class JogoForcaApp:
    """Classe principal do aplicativo Jogo da Forca (Pygame)."""
    def __init__(self) -> None:
        self.tela = tela
        self.largura = LARGURA
        self.altura = ALTURA
        self.fonte = fonte
        self.fonte_pequena = fonte_pequena
        self.forca_ui = forca_ui

    def rodar(self) -> None:
        """Executa o loop principal do jogo da forca."""
        tela_abertura()
        while True:
            lista_palavra = tela_inicio()
            jogo = JogoForca(lista_palavra)
            input_letra = ''
            fim = False
            mensagem = ''
            mostrar_popup = False
            acao = None
            while True:
                self.tela.fill(BRANCO)
                palavra_mostrar = ' '.join(jogo.palavra_atual())
                texto_palavra = self.fonte.render(palavra_mostrar, True, PRETO)
                y_palavra = 180
                self.tela.blit(texto_palavra, (self.largura//2 - texto_palavra.get_width()//2, y_palavra))
                texto_input = self.fonte_pequena.render(f'Digite uma letra:', True, PRETO)
                y_input = y_palavra + texto_palavra.get_height() + 40
                self.tela.blit(texto_input, (self.largura//2 - texto_input.get_width()//2, y_input))
                texto_usadas = self.fonte_pequena.render('Letras usadas: ' + ' '.join(jogo.letras_usadas()), True, VERMELHO)
                y_usadas = y_input + texto_input.get_height() + 40
                self.tela.blit(texto_usadas, (self.largura//2 - texto_usadas.get_width()//2, y_usadas))
                if not fim:
                    texto_letra = self.fonte_pequena.render(input_letra, True, PRETO)
                    y_letra = y_usadas + texto_usadas.get_height() + 40
                    self.tela.blit(texto_letra, (self.largura//2 - texto_letra.get_width()//2, y_letra))
                else:
                    texto_reiniciar = self.fonte_pequena.render('Pressione R para jogar novamente ou ESC para sair', True, PRETO)
                    self.tela.blit(texto_reiniciar, (self.largura//2 - texto_reiniciar.get_width()//2, self.altura - 80))
                self.forca_ui.desenhar(self.tela, jogo.erros)
                base_y = self.altura - 250
                botao_opcoes = pygame.Rect(self.largura - 320, 30, 260, 80)
                pygame.draw.rect(self.tela, PRETO, botao_opcoes, border_radius=16)
                txt_opcoes = self.fonte_pequena.render('Opções', True, BRANCO)
                self.tela.blit(txt_opcoes, (self.largura - 320 + (260-txt_opcoes.get_width())//2, 30 + (80-txt_opcoes.get_height())//2))
                msg_y = base_y + 20
                if jogo.venceu():
                    mensagem = 'Parabéns! Você venceu!'
                    fim = True
                elif jogo.perdeu():
                    mensagem = f'Você perdeu! Palavra: {jogo.get_palavra()}'
                    fim = True
                if mensagem:
                    texto_msg = self.fonte.render(mensagem, True, VERDE if jogo.venceu() else VERMELHO)
                    self.tela.blit(texto_msg, (self.largura//2 - texto_msg.get_width()//2, msg_y))
                pygame.display.flip()
                if mostrar_popup:
                    acao = mostrar_opcoes()
                    mostrar_popup = False
                    if acao == 'inicio':
                        break
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.KEYDOWN:
                        if not fim:
                            if evento.key == pygame.K_ESCAPE:
                                pygame.quit()
                                sys.exit()
                            elif pygame.K_a <= evento.key <= pygame.K_z:
                                letra = chr(evento.key).upper()
                                if letra not in jogo.letras_usadas():
                                    jogo.tentar_letra(letra)
                                    input_letra = ''
                                else:
                                    input_letra = letra
                            elif evento.key == pygame.K_BACKSPACE:
                                input_letra = input_letra[:-1]
                        else:
                            if evento.key == pygame.K_r:
                                jogo = JogoForca(lista_palavra)
                                input_letra = ''
                                fim = False
                                mensagem = ''
                            elif evento.key == pygame.K_ESCAPE:
                                pygame.quit()
                                sys.exit()
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if botao_opcoes.collidepoint(evento.pos):
                            mostrar_popup = True


def main() -> None:
    """Função principal: instancia e executa o app do Jogo da Forca."""
    app = JogoForcaApp()
    app.rodar()


if __name__ == '__main__':
    main()
