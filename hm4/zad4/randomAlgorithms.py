import random as random
from lcg import LCG

# linear congruential generator (LCG)
def randomLCGbit():
    return LCG.choice([0, 1])

# Mersenne Twister
def randomMTbit():
    return random.choice([0, 1])


def main():
    open('randomLCGbit.txt', 'w').write(''.join([str(randomLCGbit()) for i in range(1000000)]))
    open('randomMTbit.txt', 'w').write(''.join([str(randomMTbit()) for i in range(1000000)]))


if __name__ == '__main__':
    main()