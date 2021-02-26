from math import sqrt
from fractions import Fraction


def resolve_segundo_grau(a: float, b: float, c: float):
    _confere_numeros(a, b, c)

    delta = b * b - (4 * a * c)
    if delta < 0:
        raise Exception('Não há raízes reais.')

    raiz = sqrt(delta)

    x1 = ((-1 * b) + raiz) / (2 * a)
    if not isinstance(x1, float):
        x1 = Fraction(x1).limit_denominator(10)

    if delta == 0:
        return x1, x1
    else:
        x2 = ((-1 * b) - raiz) / (2 * a)
        if not isinstance(x2, float):
            x2 = Fraction(x2).limit_denominator(10)
        return x1, x2


def _confere_numeros(a: float, b: float, c: float):
    try:
        float(a)
        float(b)
        float(c)
    except ValueError:
        raise ValueError('valor errado mermão')
    
    if a == 0:
        raise Exception('Não é uma equação de segundo grau!')
    
    if b == 0 and c == 0:
        return 0, 0
    
