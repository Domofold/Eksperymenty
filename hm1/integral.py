import random
import functions

def integral(fun, a, b, m, n):
    c = 0
    rand = [ [random.uniform(a, b), random.uniform(0, m)] for i in range(n)]
    
    for i in rand:
        if fun == "x^(1/3)":
            if i[1] <= functions.f(i[0]):
                c += 1

        elif fun == "sin(x)":
            if i[1] <= functions.g(i[0]):
                c += 1

        elif fun == "4x(1-x)^3":
            if i[1] <= functions.h(i[0]):
                c += 1

    return (c/n)*(b-a)*m