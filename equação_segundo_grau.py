from math import sqrt
from fractions import Fraction


def resolve_segundo_grau(a: int, b: int, c: int):
    if a != 0 and confere_numero(a) and confere_numero(b) and confere_numero(c):
        delta = b * b - (4 * a * c)
        if delta < 0:
            return 'Não há raízes reais.'

        elif b == 0 and c == 0:
            return '0 0'
        
        else:
            raiz = sqrt(delta)

            x1 = ((-1 * b) + raiz) / (2 * a)
            if not isinstance(x1, int):
                x1 = Fraction(x1).limit_denominator(10)

            if delta == 0:
                return str(x1) + ' ' + str(x1)
            else:
                x2 = ((-1 * b) - raiz) / (2 * a)
                if not isinstance(x2, int):
                    x2 = Fraction(x2).limit_denominator(10)
                return str(x1) + ' ' + str(x2)
    else:
        return 'Não é uma equação de segundo grau!'

def confere_numero(value):
    try:
        float(value)
    except:
        return False
    return True
