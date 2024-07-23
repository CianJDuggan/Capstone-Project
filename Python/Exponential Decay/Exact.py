import numpy as np
import matplotlib.pyplot as plt

def plot_exponential_function(grid, h, lam):
    x = grid/2
    t = np.arange(-x, x, 1/1000)

    y = np.exp(lam * t)

    plt.figure(figsize=(grid, x), facecolor='white', edgecolor='black')
    ax = plt.gca()
    ax.plot(t, y, color='black')
    ax.set_ylabel('$y$', color='black', fontsize=15)
#    ax.set_title(r'$ \lambda = {}$'.format(lam), color='black')
    ax.set_facecolor('white')
    plt.axhline(0, color='black', linewidth=0.75)  # y-axis
    plt.axvline(0, color='black', linewidth=0.75)  # x-axis
    # Set border (spines) linewidth
    for spine in ax.spines.values():
        spine.set_linewidth(0.75)
        spine.set_color('black')

    plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    ax.set_xlim(-x, x)
    ax.set_ylim(0, x)
    plt.xticks(np.arange(-int(x), int(x) + 1, 1), fontsize=15, color='black')
    plt.yticks(np.arange(0, int(x) + 1, 1), fontsize=15, color='black')


    
    ax.set_xlabel('$t$', color='black', fontsize=15)
    plt.legend(labels=['$e^{\;\lambda t}$', r'$\lambda = {}$'.format(lam)], labelcolor=['black', 'black'], facecolor='white', edgecolor='black', fontsize=15, loc='upper right', handletextpad=0, handlelength=0)

    plt.savefig(f'/home/puca/University/Senior Sophister/Capstone/Graphs/Exponential Decay/Exact with {lam}.png')
    plt.show()


plot_exponential_function(grid = 10, h = 1/5, lam = -1)
