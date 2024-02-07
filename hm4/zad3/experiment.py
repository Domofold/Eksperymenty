import random
import matplotlib.pyplot as plt
import scipy.stats as ss
import numpy as np


def approx_pn(n):
    s = 0
    l = 0
    for n in range(1, n+1):
        x = random.choice([-1, 1])
        if x < 0:
            x = -1
        else:
            x = 1
        s += x
        if s >= 0:
            l += 1
    return l

for i in [100, 1000, 10000]:
    pI = []
    for k in range(5000):
        print(k)
        l = approx_pn(i)
        pI.append(l / i)
    rv = ss.arcsine()
    distribution = np.linspace(0, np.minimum(rv.dist.b, 3))

    plt.hist(pI, bins=20, density=True)
    plt.title(f'')
    plt.plot(distribution, rv.pdf(distribution), color='red')
    plt.savefig(f'P{i}_PDF.png')
    plt.close()