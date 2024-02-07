import numpy as np
import matplotlib.pyplot as plt
import stimulate as stim
import plot
import math

def main():
    t = [i for i in range(1000, 100001, 1000)]

    x, bnArr, unArr, cnArr, dnArr, dnSubCnArr = [], [], [], [], [], []

    avgBn, avgUn, avgCn, avgDn, avgDnSubCn = [], [], [], [], []

    for n in t:
        print(n)
        sumBn, sumUn, sumCn, sumDn, sumDnSubCn = 0, 0, 0, 0, 0
        for j in range(50):
            x.append(n)

            bn, un, cn, dn = stim.stimulate(n)
            
            bnArr.append(bn)
            unArr.append(un)
            cnArr.append(cn)
            dnArr.append(dn)
            dnSubCnArr.append(dn - cn)
            sumBn += bn
            sumUn += un
            sumCn += cn
            sumDn += dn
            sumDnSubCn += dn - cn
        
        avgBn.append(sumBn/50)
        avgUn.append(sumUn/50)
        avgCn.append(sumCn/50)
        avgDn.append(sumDn/50)
        avgDnSubCn.append(sumDnSubCn/50)
        sumBn = 0
        sumUn = 0
        sumCn = 0
        sumDn = 0
        sumDnSubCn = 0

    plot.plot(x, bnArr, t, avgBn, "bn")
    plot.plot(x, unArr, t, avgUn, "un")
    plot.plot(x, cnArr, t, avgCn, "cn")
    plot.plot(x, dnArr, t, avgDn, "dn")
    plot.plot(x, dnSubCnArr, t, avgDnSubCn, "dnSubCn")

    plot.plot(t, np.array(avgBn)/np.array(t), t, None, "BprzezN")
    plot.plot(t, np.array(avgBn)/np.array(t)**(1/2), t, None, "BprzezPierwiastekN")

    plot.plot(t, np.array(avgUn)/np.array(t), t, None, "UprzezN")
    
    plot.plot(t, np.array(avgCn)/np.array(t), t, None, "CprzezN")
    plot.plot(t, np.array(avgCn)/(np.array(t)*np.log(np.array(t))), t, None, "CprzezNLnN")
    plot.plot(t, np.array(avgCn)/np.array(t)**2, t, None, "CprzezNkwadrat")

    plot.plot(t, np.array(avgDn)/np.array(t), t, None, "DprzezN")
    plot.plot(t, np.array(avgDn)/(np.array(t)*np.log(np.array(t))), t, None, "DprzezNLnN")
    plot.plot(t, np.array(avgDn)/np.array(t)**2, t, None, "DprzezNkwadrat")

    plot.plot(t, np.array(avgDnSubCn)/np.array(t), t, None, "dnSubCnprzezN")
    plot.plot(t, np.array(avgDnSubCn)/(np.array(t)*np.log(np.array(t))), t, None, "dnSubCnprzezNLogN")
    plot.plot(t, np.array(avgDnSubCn)/np.array(t)*np.log(np.log(np.array(t))), t, None, "dnSubCnprzezNlnlnN")

                
main()

    



