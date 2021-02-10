from unittest import TestCase

from ex_01 import Bola


class BolaTestCase(TestCase):
    def test_mostra_cor(self):
        bola = Bola()
        self.assertEqual(None, bola.cor)

    def test_troca_cor(self):
        bola = Bola()
        nova_cor = 'Azul'
        bola.troca_cor(nova_cor)
        # assertEqual(valor esperado = 'Azul', valor_obtido = ?)
        self.assertEqual(nova_cor, bola.troca_cor(nova_cor))