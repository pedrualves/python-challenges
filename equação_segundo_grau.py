from math import sqrt
from fractions import Fraction


def resolve_segundo_grau(a: int, b: int, c: int):
    delta = b * b - (4 * a * c)

    if delta < 0 and (b == 0 or c == 0):
        print('equação incompleta, com raiz com número negativo, logo conjunto solução é 0')
    else:
        print('delta negativo, não admite solução')

    if delta > 0:
        raiz = sqrt(delta)

        x1 = ((-1 * b) + raiz) / (2 * a)
        if not isinstance(x1, int):
            x1 = Fraction(x1).limit_denominator(10)

        x2 = ((-1 * b) - raiz) / (2 * a)
        if not isinstance(x2, int):
            x2 = Fraction(x2).limit_denominator(10)

        print(x1, x2)
    
    return


resolve_segundo_grau(3, -1, -2)  # resultado: 1 e 2/3
resolve_segundo_grau(2, -7, 0)  # resultado: 7/2 0
resolve_segundo_grau(4, 0, 2)  # resultado: equação incompleta, com raiz com número negativo, logo conjunto solução é 0
resolve_segundo_grau(4, 0, -16)  # resultado: 2 e -2
resolve_segundo_grau(5, 8, 10)  # resultado: delta negativo, não admite solução
