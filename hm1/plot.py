import matplotlib.pyplot as plt

def plot(x, y, t, avg, axhline, ylim1, ylim2, pngName):
    plt.scatter(x, y, color="slateblue", s=5)
    plt.scatter(t, avg, color="red", s=60)
    plt.axhline(y=axhline, color='lightgreen', linewidth=4)
    plt.ylim(ylim1, ylim2)
    plt.savefig(f"{pngName}.png")
    plt.close()
