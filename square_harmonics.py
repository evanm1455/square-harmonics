import matplotlib.patches as patch
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


HARMONICS = 4
N = 1000


def sinwave(x, harmonic):
    pts = np.sin(harmonic * x)
    return pts


def sqwave(x):
    pts = signal.square(x, duty=0.5)
    return pts


if __name__ == '__main__':

    fig, axs = plt.subplots(HARMONICS + 1)
    for ax in axs:
        ax.xaxis.set_visible(False)
    
    axs[0].set_title('Harmonics')
    
    # stacked plot of all of the harmonics
    x = np.linspace(0, 4*np.pi, N)
    for n in range(1, HARMONICS * 2, 2):
        axs[0].plot(sinwave(x, n))
    
    
    # plot square wave overlayed with partial sum of harmonics
    for i in range(1, len(axs)):
        axs[i].plot(sqwave(x))
        
        ptsum = np.zeros(N)
        for j in range(1, i*2, 2):
            ptsum += (1/j) * sinwave(x, j)
        
        axs[i].plot(ptsum)

    plt.show()
