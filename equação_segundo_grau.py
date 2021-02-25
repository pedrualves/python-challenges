from math import sqrt
from fractions import Fraction


def resolve_segundo_grau(a: int, b: int, c: int):
    
    if a != 0:
        delta = b * b - (4 * a * c)
        if delta < 0:
            print('Não há raízes reais.')

        elif b == 0 and c == 0:
            print(0, 0)
        
        else:
            raiz = sqrt(delta)

            x1 = ((-1 * b) + raiz) / (2 * a)
            if not isinstance(x1, int):
                x1 = Fraction(x1).limit_denominator(10)

            if delta == 0:
                print(x1, (-1) * x1)
            
            else:
                x2 = ((-1 * b) - raiz) / (2 * a)
                if not isinstance(x2, int):
                    x2 = Fraction(x2).limit_denominator(10)
                print(x1, x2)
    else:
        print('Não é uma equação de segundo grau!')
    
    return


resolve_segundo_grau(3, -1, -2)  # resultado: 1 e -2/3
resolve_segundo_grau(2, -7, 0)  # resultado: 7/2 0
resolve_segundo_grau(4, 0, 2)  # resultado: Não há raízes reais.
resolve_segundo_grau(4, 0, -16)  # resultado: 2 e -2
resolve_segundo_grau(5, 8, 10)  # resultado: Não há raízes reais.
resolve_segundo_grau(0, 1, 2) # resultado: Não é uma equação de segundo grau!
resolve_segundo_grau(2, 0, 0) # resultado: 0 0