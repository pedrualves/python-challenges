import unittest
from equacao_segundo_grau import resolve_segundo_grau


class EquacaoSegundoGrauTest(unittest.TestCase):
    def test_nao_equacao_segundo_grau(self):
        with self.assertRaises(Exception):
            resolve_segundo_grau(0, 1, 1)

        with self.assertRaises(Exception):
            resolve_segundo_grau(0, 0, 1)

        with self.assertRaises(Exception):
            resolve_segundo_grau(0, 1, 0)

    def test_equacao_segundo_grau(self):
        x1, x2 = resolve_segundo_grau(2, 0, 0)
        self.assertEqual(x1, 0)
        self.assertEqual(x2, 0)

        x1, x2 = resolve_segundo_grau(4, 0, -16)
        self.assertEqual(x1, 2)
        self.assertEqual(x2, -2)

        x1, x2 = resolve_segundo_grau(2, -7, 0)
        self.assertEqual(str(x1), '7/2')
        self.assertEqual(str(x2), '0')

        x1, x2 = resolve_segundo_grau(3, -1, -2)
        self.assertEqual(str(x1), '1')
        self.assertEqual(str(x2), '-2/3')

        x1, x2 = resolve_segundo_grau(3, 0, 0)
        self.assertEqual(x1, 0)
        self.assertEqual(x2, 0)

    def test_equacao_sem_raizes(self):
        with self.assertRaises(Exception):
            resolve_segundo_grau(4, 0, 2)

        with self.assertRaises(Exception):
            resolve_segundo_grau(5, 8, 10)

    def test_numeros_invalidos(self):
        with self.assertRaises(ValueError):
            resolve_segundo_grau("Mari", 8, 10)

        with self.assertRaises(ValueError):
            resolve_segundo_grau(77, "Torta de Palmito", 10)

        with self.assertRaises(ValueError):
            resolve_segundo_grau(2, 100, "Matemática é legal")
