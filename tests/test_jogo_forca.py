import unittest
from jogo_forca import JogoForca

class TestJogoForca(unittest.TestCase):
    def setUp(self):
        self.jogo = JogoForca('python')

    def test_inicializacao(self):
        self.assertEqual(self.jogo.palavra, 'PYTHON')
        self.assertEqual(self.jogo.letras_certas, set())
        self.assertEqual(self.jogo.letras_erradas, set())
        self.assertFalse(self.jogo.fim_de_jogo)
        self.assertFalse(self.jogo.ganhou)

    def test_tentativa_correta(self):
        self.jogo.tentar_letra('p')
        self.assertIn('P', self.jogo.letras_certas)
        self.assertFalse(self.jogo.fim_de_jogo)

    def test_tentativa_errada(self):
        self.jogo.tentar_letra('z')
        self.assertIn('Z', self.jogo.letras_erradas)
        self.assertFalse(self.jogo.fim_de_jogo)

    def test_vitoria(self):
        for letra in 'python':
            self.jogo.tentar_letra(letra)
        self.assertTrue(self.jogo.ganhou)
        self.assertTrue(self.jogo.fim_de_jogo)

    def test_derrota(self):
        for letra in 'abcdef':
            self.jogo.tentar_letra(letra)
        self.assertFalse(self.jogo.ganhou)
        self.assertTrue(self.jogo.fim_de_jogo)

    def test_letra_repetida(self):
        self.jogo.tentar_letra('p')
        resultado = self.jogo.tentar_letra('p')
        self.assertFalse(resultado)  # Não deve aceitar letra repetida

    def test_case_insensitive(self):
        self.jogo.tentar_letra('P')
        self.jogo.tentar_letra('p')
        self.assertEqual(len(self.jogo.letras_certas), 1)

    def test_nao_alfabetico(self):
        resultado = self.jogo.tentar_letra('1')
        self.assertFalse(resultado)
        resultado = self.jogo.tentar_letra('-')
        self.assertFalse(resultado)

    def test_palavra_atual(self):
        self.jogo.tentar_letra('p')
        self.jogo.tentar_letra('y')
        atual = self.jogo.palavra_atual()
        self.assertEqual(atual[0], 'P')
        self.assertEqual(atual[1], 'Y')
        self.assertEqual(atual[2], '_')

    def test_get_palavra(self):
        self.assertEqual(self.jogo.get_palavra(), 'PYTHON')

    def test_finalizado(self):
        for letra in 'python':
            self.jogo.tentar_letra(letra)
        self.assertTrue(self.jogo.finalizado())

    def test_letras_usadas(self):
        self.jogo.tentar_letra('p')
        self.jogo.tentar_letra('z')
        usadas = self.jogo.letras_usadas()
        self.assertIn('P', usadas)
        self.assertIn('Z', usadas)

if __name__ == '__main__':
    unittest.main()
