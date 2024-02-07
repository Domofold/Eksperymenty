import matplotlib.pyplot as plt

def plot(x, y, t, avg, pngName):
    plt.scatter(x, y, color="slateblue", s=5)
    if avg is not None:
        plt.scatter(t, avg, color="red", s=60)
    plt.savefig(f"{pngName}.png")
    plt.close()
