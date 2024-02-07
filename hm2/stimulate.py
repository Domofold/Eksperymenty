import random
import numpy as np

def stimulate(n):
    bn, un, cn, dn = None, None, None, None

    urny = np.zeros(n)
    pustych = n
    jedynek = n

    rzut = 0
    while True:
        urna = random.randint(0, n-1)
        urny[urna] += 1
        rzut += 1

        if bn is None and urny[urna] == 2:
                bn = rzut

        if rzut == n:
              un = pustych

        if urny[urna] == 1:
              pustych -= 1
              if pustych == 0:
                    cn = rzut
        elif urny[urna] == 2:
              jedynek -= 1
              if jedynek == 0:
                    dn = rzut
                    break
              

    return bn, un, cn, dn