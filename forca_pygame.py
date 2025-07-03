import pygame
import sys
from palavras import palavra_facil, palavra_normal, palavra_dificil, palavra_secreta
from jogo_forca import JogoForca
import random
import math  # Necessário para os efeitos

# Configurações iniciais
def escolher_lista():
    opcoes = [palavra_facil, palavra_normal, palavra_dificil, palavra_secreta]
    return random.choice(opcoes)

pygame.init()
info = pygame.display.Info()
LARGURA, ALTURA = info.current_w, info.current_h
# Inicia em fullscreen
flags = pygame.FULLSCREEN

tela = pygame.display.set_mode((LARGURA, ALTURA), flags)
pygame.display.set_caption('Jogo da Forca - Pygame')
fonte = pygame.font.SysFont('arial', 72)  # Fonte grande para o jogo
fonte_pequena = pygame.font.SysFont('arial', 48)  # Fonte grande para menus e textos gerais
fonte_popup = pygame.font.SysFont('arial', 48)  # Fonte padrão dos popups (igual à antiga fonte)
fonte_pequena_popup = pygame.font.SysFont('arial', 32)  # Fonte pequena dos popups (igual à antiga fonte_pequena)

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 200, 0)

# Função para desenhar a forca e boneco
def desenhar_forca(erros):
    # Forca centralizada horizontalmente
    base_x = (LARGURA // 2) - 100
    base_y = ALTURA - 250  # 250 pixels acima do bottom
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

def mostrar_creditos():
    popup_largura, popup_altura = 1000, 500  # Área ainda maior para não cortar frases
    popup_x = (LARGURA - popup_largura) // 2
    popup_y = (ALTURA - popup_altura) // 2
    popup = pygame.Surface((popup_largura, popup_altura))
    popup.fill((240, 240, 240))
    pygame.draw.rect(popup, PRETO, (0, 0, popup_largura, popup_altura), 4)
    titulo = fonte_pequena_popup.render('Desenvolvido por:', True, PRETO)
    nome = fonte_popup.render('Amiraldo Almeida', True, VERMELHO)
    info1 = fonte_pequena_popup.render('Python 3 + pygame', True, PRETO)
    info2 = fonte_pequena_popup.render('Jogo da Forca - 2025', True, PRETO)
    objetivo1 = fonte_pequena_popup.render('Objetivo:', True, PRETO)
    objetivo2 = fonte_pequena_popup.render('Descubra a palavra secreta antes de ser enforcado!', True, PRETO)
    instrucao = fonte_pequena_popup.render('Pressione qualquer tecla para fechar', True, PRETO)
    popup.blit(titulo, (popup_largura//2 - titulo.get_width()//2, 40))
    popup.blit(nome, (popup_largura//2 - nome.get_width()//2, 90))
    popup.blit(info1, (popup_largura//2 - info1.get_width()//2, 160))
    popup.blit(info2, (popup_largura//2 - info2.get_width()//2, 200))
    popup.blit(objetivo1, (popup_largura//2 - objetivo1.get_width()//2, 260))
    popup.blit(objetivo2, (popup_largura//2 - objetivo2.get_width()//2, 300))
    popup.blit(instrucao, (popup_largura//2 - instrucao.get_width()//2, 420))
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

def mostrar_opcoes():
    popup_largura, popup_altura = 500, 220
    popup_x = (LARGURA - popup_largura) // 2
    popup_y = (ALTURA - popup_altura) // 2
    popup = pygame.Surface((popup_largura, popup_altura))
    popup.fill((240, 240, 240))
    pygame.draw.rect(popup, PRETO, (0, 0, popup_largura, popup_altura), 4)
    titulo = fonte_pequena_popup.render('Escolha uma opção:', True, PRETO)
    popup.blit(titulo, (popup_largura//2 - titulo.get_width()//2, 30))
    # Botões simplificados
    botoes = [
        ("Tela Inicial", (popup_largura//2 - 100, 80, 200, 50)),
        ("Fechar Jogo", (popup_largura//2 - 100, 140, 200, 50)),
    ]
    for nome, rect in botoes:
        pygame.draw.rect(popup, VERMELHO if nome == "Fechar Jogo" else PRETO, rect, border_radius=10)
        txt = fonte_pequena_popup.render(nome, True, BRANCO)
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

def tela_inicio():
    selecionado = 0
    opcoes = [
        ("Fácil", palavra_facil),
        ("Normal", palavra_normal),
        ("Difícil", palavra_dificil),
        ("Secreta", palavra_secreta)
    ]
    while True:
        tela.fill(BRANCO)
        titulo = fonte.render('Jogo da Forca', True, PRETO)
        tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 80))
        subtitulo = fonte_pequena.render('Escolha a dificuldade:', True, PRETO)
        tela.blit(subtitulo, (LARGURA//2 - subtitulo.get_width()//2, 180))
        # Centraliza o menu de opções
        total_altura = len(opcoes) * 60
        inicio_y = (ALTURA // 2) - (total_altura // 2)
        for i, (nome, _) in enumerate(opcoes):
            cor = VERDE if i == selecionado else PRETO
            txt = fonte_pequena.render(nome, True, cor)
            tela.blit(txt, (LARGURA//2 - txt.get_width()//2, inicio_y + i*60))
        # Botão de créditos
        botao_creditos = pygame.Rect(LARGURA - 260, ALTURA - 90, 220, 60)
        pygame.draw.rect(tela, VERMELHO, botao_creditos, border_radius=12)
        txt_creditos = fonte_pequena.render('Créditos', True, BRANCO)
        tela.blit(txt_creditos, (LARGURA - 260 + (220-txt_creditos.get_width())//2, ALTURA - 90 + (60-txt_creditos.get_height())//2))
        # Botão de sair
        botao_sair = pygame.Rect(40, ALTURA - 90, 220, 60)
        pygame.draw.rect(tela, PRETO, botao_sair, border_radius=12)
        txt_sair = fonte_pequena.render('Sair', True, BRANCO)
        tela.blit(txt_sair, (40 + (220-txt_sair.get_width())//2, ALTURA - 90 + (60-txt_sair.get_height())//2))
        pygame.display.flip()
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

def tela_abertura():
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
        # Gradiente animado de fundo
        for y in range(ALTURA):
            cor = (20 + int(30 * abs(math.sin((y+grad_y)/80))), 20, 40 + int(60 * abs(math.cos((y+grad_y)/120))))
            pygame.draw.line(tela, cor, (0, y), (LARGURA, y))
        grad_y += 2
        tempo_atual = pygame.time.get_ticks() - tempo_inicial
        # Flashes/brilhos aleatórios (tamanho aumentado)
        if random.random() < 0.08:
            flashes.append((random.randint(0, LARGURA), random.randint(0, ALTURA), random.randint(32, 64)))
        for i, (fx, fy, fr) in enumerate(flashes):
            pygame.draw.circle(tela, (255,255,255,80), (fx, fy), fr)
        # Decremento proporcional ao tamanho para suavidade
        flashes = [(fx, fy, max(4, fr-4)) for (fx, fy, fr) in flashes if fr > 4]
        # Efeito de digitação do título
        if tempo_atual < duracao_efeito:
            letras_mostradas = min(len(letras_titulo), int(tempo_atual/tempo_letra))
            titulo = ''.join(letras_titulo[:letras_mostradas])
            texto = fonte.render(titulo, True, VERMELHO)
            tela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 - texto.get_height()//2))
        else:
            if not efeito_finalizado:
                efeito_finalizado = True
                tempo_titulo = pygame.time.get_ticks()
            # Exibe o nome do jogo completo
            texto = fonte.render(titulo_str, True, VERMELHO)
            tela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 - texto.get_height()//2))
            if pygame.time.get_ticks() - tempo_titulo > duracao_titulo:
                rodando = False
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def main():
    tela_abertura()  # Chama a tela de abertura antes de tudo
    while True:
        lista_palavra = tela_inicio()
        jogo = JogoForca(lista_palavra)
        letras_disponiveis = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        input_letra = ''
        fim = False
        mensagem = ''
        mostrar_popup = False
        acao = None
        while True:
            tela.fill(BRANCO)
            # Palavra exibida acima da forca
            palavra_mostrar = ' '.join(jogo.palavra_atual())
            texto_palavra = fonte.render(palavra_mostrar, True, PRETO)
            y_palavra = 180
            tela.blit(texto_palavra, (LARGURA//2 - texto_palavra.get_width()//2, y_palavra))

            # Frase: Digite uma letra (abaixo da palavra, com mais espaço)
            texto_input = fonte_pequena.render(f'Digite uma letra:', True, PRETO)
            y_input = y_palavra + texto_palavra.get_height() + 40  # +30px extra
            tela.blit(texto_input, (LARGURA//2 - texto_input.get_width()//2, y_input))

            # Letras já usadas (abaixo do input, com espaçamento maior)
            texto_usadas = fonte_pequena.render('Letras usadas: ' + ' '.join(jogo.letras_usadas()), True, VERMELHO)
            y_usadas = y_input + texto_input.get_height() + 40  # +30px extra
            tela.blit(texto_usadas, (LARGURA//2 - texto_usadas.get_width()//2, y_usadas))

            # Input de letra digitada (abaixo das letras usadas)
            if not fim:
                texto_letra = fonte_pequena.render(input_letra, True, PRETO)
                y_letra = y_usadas + texto_usadas.get_height() + 40  # +30px extra
                tela.blit(texto_letra, (LARGURA//2 - texto_letra.get_width()//2, y_letra))
            else:
                texto_reiniciar = fonte_pequena.render('Pressione R para jogar novamente ou ESC para sair', True, PRETO)
                tela.blit(texto_reiniciar, (LARGURA//2 - texto_reiniciar.get_width()//2, ALTURA - 80))

            # Forca (ajustada para baixo)
            desenhar_forca(jogo.erros)
            base_y = ALTURA - 250  # base_y da forca

            # Botão de opções sempre visível (canto superior direito)
            botao_opcoes = pygame.Rect(LARGURA - 320, 30, 260, 80)  # Aumentado
            pygame.draw.rect(tela, PRETO, botao_opcoes, border_radius=16)
            txt_opcoes = fonte_pequena.render('Opções', True, BRANCO)
            tela.blit(txt_opcoes, (LARGURA - 320 + (260-txt_opcoes.get_width())//2, 30 + (80-txt_opcoes.get_height())//2))

            # Mensagem de fim de jogo (20px abaixo da forca)
            msg_y = base_y + 20
            if jogo.venceu():
                mensagem = 'Parabéns! Você venceu!'
                fim = True
            elif jogo.perdeu():
                mensagem = f'Você perdeu! Palavra: {jogo.get_palavra()}'
                fim = True
            if mensagem:
                texto_msg = fonte.render(mensagem, True, VERDE if jogo.venceu() else VERMELHO)
                tela.blit(texto_msg, (LARGURA//2 - texto_msg.get_width()//2, msg_y))

            pygame.display.flip()

            if mostrar_popup:
                acao = mostrar_opcoes()
                mostrar_popup = False
                if acao == 'inicio':
                    break  # Volta para tela_inicio
                # continuar apenas fecha o popup

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
                            # Reinicia o jogo com nova palavra da mesma lista
                            jogo = JogoForca(lista_palavra)
                            letras_disponiveis = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                            input_letra = ''
                            fim = False
                            mensagem = ''
                        elif evento.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botao_opcoes.collidepoint(evento.pos):
                        mostrar_popup = True
            # Removido: if mostrar_popup and acao == 'inicio':
            # O fluxo já é controlado dentro do bloco do popup

if __name__ == '__main__':
    main()
