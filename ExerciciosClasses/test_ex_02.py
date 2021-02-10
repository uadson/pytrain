from unittest import TestCase

from ex_02 import Quadrado


class QuadradoTestCase(TestCase):
    def test_retorna_valor(self):
        quadrado = Quadrado()
        quadrado.retorna_valor()
        self.assertEqual(None, quadrado.retorna_valor())

    def test_altera_valor(self):
        quadrado = Quadrado()
        valor = 4
        quadrado.altera_valor(valor)
        quadrado.retorna_valor()
        self.assertEqual(4, quadrado.retorna_valor())

    def test_calcular_area(self):
        quadrado = Quadrado()
        valor = 4
        quadrado.altera_valor(valor)
        quadrado.calcular_area()
        self.assertEqual(16, quadrado.calcular_area())