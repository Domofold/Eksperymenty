import integral
import pi
import plot
import math

def main():
    sum_avg = 0
    t = [i for i in range(50, 5001, 50)]
    x = []
    y = []
    avg = []

    for i in t:
        for j in range(50):
            x.append(i)
            inte = integral.integral("4x(1-x)^3", 0, 1, 1, i)
            y.append(inte)
            sum_avg += inte
        avg.append(sum_avg/50)
        sum_avg = 0

    plot.plot(x, y, t, avg, 0.2, 0.16, 0.24, "f")
    
    x.clear()
    y.clear()
    avg.clear()

    for i in t:
        for j in range(50):
            x.append(i)
            inte = integral.integral("x^(1/3)", 0, 8, 3, i)
            y.append(inte)
            sum_avg += inte
        avg.append(sum_avg/50)
        sum_avg = 0

    plot.plot(x, y, t, avg, 12, 11, 13, "g")

    x.clear()
    y.clear()
    avg.clear()

    for i in t:
        for j in range(50):
            x.append(i)
            inte = integral.integral("sin(x)", 0, math.pi, 30, i)
            y.append(inte)
            sum_avg += inte
        avg.append(sum_avg/50)
        sum_avg = 0

    plot.plot(x, y, t, avg, 2, 1, 3, "h")

    x.clear()
    y.clear()
    avg.clear()

    for i in t:
        for j in range(50):
            x.append(i)
            inte = pi.pi(i)
            y.append(inte)
            sum_avg += inte
        avg.append(sum_avg/50)
        sum_avg = 0

    plot.plot(x, y, t, avg, math.pi, 3, 3.28, "pi")

main()