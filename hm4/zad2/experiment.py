import random as random
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss

def cdf_approx(n):
    allsn = []
    for k in range(10000):
        sn = 0
        for i in range(n):
            sn += random.choice([-1, 1])
        allsn.append(sn)
    sndict = {}
    for s in allsn:
        if s in sndict.keys():
            sndict[s] += 1
        else:
            sndict[s] = 1

    plt.hist(allsn, density=True, cumulative=True, bins=len(sndict.keys()))
    x2 = np.linspace(min(allsn), max(allsn))
    y2 = ss.norm(loc=0, scale=(max(allsn)-min(allsn))/8).cdf(x2)
    plt.plot(x2, y2, color='red')
    plt.title(f"")
    plt.savefig(f"CDF_S{n}.png")
    plt.close()

def main():
    for i in range(5, 31, 5):
        cdf_approx(i)
    cdf_approx(100)
    
    

if __name__ == "__main__":
    main()