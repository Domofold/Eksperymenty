import random
import numpy as np

def stimulate(n, d):
    urns = np.zeros(n)
    ln = 0

    for i in range(n):
        if d == 1:
            urn = random.randint(0, n-1)
            urns[urn] += 1
        elif d == 2:
            urn1, urn2 = random.randint(0, n-1), random.randint(0, n-1)
            urn = urn1 if urns[urn1] < urns[urn2] else urn2
            urns[urn] += 1
        
        ln = max(ln, urns[urn])
    
    return ln