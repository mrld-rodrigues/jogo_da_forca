# Lógica reutilizável do jogo da forca para interfaces gráficas e web
import random
import string

class JogoForca:
    def __init__(self, lista_palavra):
        self.palavra = random.choice(lista_palavra).upper()
        while '_' in self.palavra or ' ' in self.palavra:
            self.palavra = random.choice(lista_palavra).upper()
        self.letras_palavra = list(self.palavra)
        self.letras_escolhidas = set()
        self.erros = 0
        self.max_erros = 6

    def tentar_letra(self, letra):
        letra = letra.upper()
        if letra in string.ascii_uppercase and letra not in self.letras_escolhidas:
            self.letras_escolhidas.add(letra)
            if letra in self.letras_palavra:
                self.letras_palavra = [l for l in self.letras_palavra if l != letra]
                return True
            else:
                self.erros += 1
                return False
        return None  # Letra inválida ou já escolhida

    def palavra_atual(self):
        return [letra if letra in self.letras_escolhidas else '_' for letra in self.palavra]

    def venceu(self):
        return len(self.letras_palavra) == 0

    def perdeu(self):
        return self.erros >= self.max_erros

    def finalizado(self):
        return self.venceu() or self.perdeu()

    def letras_usadas(self):
        return sorted(self.letras_escolhidas)

    def get_palavra(self):
        return self.palavra
