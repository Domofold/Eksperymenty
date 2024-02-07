import random

def pi(n):
    c = 0
    rand = [ [random.uniform(-1, 1), random.uniform(-1, 1)] for i in range(n)]

    for i in rand:
        if i[0]**2 + i[1]**2 <= 1:
            c += 1
    
    area = (c/n) * 4
    pi = area / 1

    return pi