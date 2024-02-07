import stimulate as stim
import plot
import numpy as np


def main():
    t = [i for i in range(100, 10001, 100)]

    x, comparisonsArr, swapsArr = [], [], []

    avgComparisonsArr, avgSwapsArr = [], []

    for n in t:
        print(n)
        sumComparisons, sumSwaps = 0, 0

        for i in range(50):
            x.append(n)

            comparisons, swaps = stim.stimulate(n)

            comparisonsArr.append(comparisons)
            swapsArr.append(swaps)

            sumComparisons += comparisons
            sumSwaps += swaps
        
        avgComparisonsArr.append(sumComparisons/50)
        avgSwapsArr.append(sumSwaps/50)
        sumComparisons = 0
        sumSwaps = 0

    plot.plot(x, comparisonsArr, t, avgComparisonsArr, "cmp")
    plot.plot(x, swapsArr, t, avgSwapsArr, "s")

    plot.plot(t, np.array(avgComparisonsArr)/np.array(t), t, None, "cmpPrzezN")
    plot.plot(t, np.array(avgComparisonsArr)/(np.array(t)**2), t, None, "cmpPrzezNkwadrat")
    
    plot.plot(t, np.array(avgSwapsArr)/np.array(t), t, None, "sPrzezN")
    plot.plot(t, np.array(avgSwapsArr)/(np.array(t)**2), t, None, "sPrzezNkwadrat")



main()



