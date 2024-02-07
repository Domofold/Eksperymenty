import numpy as np
import matplotlib.pyplot as plt
import stimulate as stim
import plot
import math

def main():
    t = [i for i in range(1000, 100001, 1000)]

    x, lnD1Arr, lnD2Arr = [], [], []

    avgLnD1Arr, avgLnD2Arr = [], []

    for n in t:
        print(n)
        sumLnD1, sumLnD2 = 0, 0
        
        for j in range(50):
            x.append(n)

            lnD1 = stim.stimulate(n, 1)
            lnD2 = stim.stimulate(n, 2)
            lnD1Arr.append(lnD1)
            lnD2Arr.append(lnD2)

            sumLnD1 += lnD1
            sumLnD2 += lnD2
        avgLnD1Arr.append(sumLnD1/50)
        avgLnD2Arr.append(sumLnD2/50)
        sumLnD1 = 0
        sumLnD2 = 0


    plot.plot(x, lnD1Arr, t, avgLnD1Arr, "lnD1")
    plot.plot(x, lnD2Arr, t, avgLnD2Arr, "lnD2")

    plot.plot(t, np.array(avgLnD1Arr)/(np.log(np.array(t))/np.log(np.log(np.array(t)))), t, None, "lnD1przezLnNprzezLnLnN")
    plot.plot(t, np.array(avgLnD2Arr)/(np.log(np.log(np.array(t)))/np.log(2)), t, None, "LnD2przezLnLnNprzezLn2")
                
main()

    



