import unittest
from equação_segundo_grau import resolve_segundo_grau

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(resolve_segundo_grau(0, 0, 0), "Não é uma equação de segundo grau!")
        self.assertEqual(resolve_segundo_grau(0, 1, 1), "Não é uma equação de segundo grau!")
        self.assertEqual(resolve_segundo_grau(0, 0, 1), "Não é uma equação de segundo grau!")
        self.assertEqual(resolve_segundo_grau(0, 1, 0), "Não é uma equação de segundo grau!")
        self.assertEqual(resolve_segundo_grau(2, 0, 0), "0 0")
        self.assertEqual(resolve_segundo_grau(4, 0, 2), "Não há raízes reais.")
        self.assertEqual(resolve_segundo_grau(2, -7, 0), "7/2 0")
        self.assertEqual(resolve_segundo_grau(3, -1, -2), "1 -2/3")
        self.assertEqual(resolve_segundo_grau(5, 8, 10), "Não há raízes reais.")
        self.assertEqual(resolve_segundo_grau("Mari", 8, 10), "Não é uma equação de segundo grau!")
        self.assertEqual(resolve_segundo_grau(77, "Torta de Palmito", 10), "Não é uma equação de segundo grau!")
        self.assertEqual(resolve_segundo_grau(2, 100, "Matemática é legal"), "Não é uma equação de segundo grau!")

if __name__ == '__main__':
    unittest.main()
