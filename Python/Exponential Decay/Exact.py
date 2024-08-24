import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

cmap = mpl.colormaps['magma_r']
colors = cmap(np.linspace(0, 1, 10))

def plot_exponential_function(domain, grid, h, lam):
    x = grid/2
    t = np.arange(0, x, 1/1000)

    y = np.exp(lam * t)
    
    if domain == 'real':
        plt.figure(figsize=(grid, grid), facecolor='white', edgecolor='black')
        ax = plt.gca()
        ax.plot(t, y, color=colors[3])
        ax.set_ylabel('$y$', color='black', fontsize=15)
        ax.set_facecolor('white')
        plt.axhline(0, color='black', linewidth=0.75)  # y-axis
        plt.axvline(0, color='black', linewidth=0.75)  # x-axis
        # Set border (spines) linewidth
        for spine in ax.spines.values():
            spine.set_linewidth(0.75)
            spine.set_color('black')

        plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        ax.set_xlim(-2, 3)
        ax.set_ylim(0, x)
        ax.set_aspect(aspect='equal')  # Set the aspect ratio to 1:1
        plt.xticks(np.arange(-2, 4, 1), fontsize=15, color='black')
        plt.yticks(np.arange(0, int(x) + 1, 1), fontsize=15, color='black')
        ax.set_xlabel('$t$', color='black', fontsize=15)
        plt.legend(labels=[r'$\lambda = {}$'.format(lam)], labelcolor=['black', 'black'], facecolor='white', edgecolor='black', fontsize=15, loc='upper right', handletextpad=0, handlelength=0)


    elif domain == 'complex':
        fig = plt.figure(figsize=(10, 10), facecolor='white', edgecolor='black')
        ax = fig.add_subplot(111, projection='3d', facecolor='white')
        ax.view_init(elev=22.5, azim=315, roll=0)
        ax.plot(t, y.real, y.imag, color=colors[3], linewidth=1.5)
        ax.set_xlabel('$t$', color='black')
        ax.set_ylabel('$Re(y)$', color='black')
        ax.set_zlabel('$Im(y)$', color='black')
        plt.legend(labels=[r'$\lambda = {}$'.format(lam)], labelcolor=['black', 'black'], facecolor='white', edgecolor='black', fontsize=15, loc=(0.4,0.2), handletextpad=0, handlelength=0, framealpha=1)
        # Set background color for axes planes
        ax.xaxis.set_pane_color('white')
        ax.yaxis.set_pane_color('white')
        ax.zaxis.set_pane_color('white')
        
        # Customize axis colors
        ax.xaxis.line.set_color('black')
        ax.yaxis.line.set_color('black')
        ax.zaxis.line.set_color('black')
        
        # Set tick colors
        ax.tick_params(axis='x', colors='black')
        ax.xaxis._axinfo['tick']['inward_factor'] = 0
        ax.xaxis._axinfo['tick']['outward_factor'] = 0
        ax.tick_params(axis='y', colors='black')
        ax.yaxis._axinfo['tick']['inward_factor'] = 0
        ax.yaxis._axinfo['tick']['outward_factor'] = 0
        ax.tick_params(axis='z', colors='black')
        ax.zaxis._axinfo['tick']['inward_factor'] = 0
        ax.zaxis._axinfo['tick']['outward_factor'] = 0

        # Set ranges for axes
        ax.set_xlim([t.min(), t.max()])
        ax.set_ylim([y.real.min(), y.real.max()])
        ax.set_zlim([y.imag.min(), y.imag.max()])

        # Set ticks to create square grid boxes
        tick_space = 4
        ax.set_xticks(np.arange(t.min(), t.max() + 1, (np.ceil(t.max()) - np.floor(t.min()))/tick_space))
        ax.set_yticks(np.arange(np.floor(y.real.min()), np.ceil(y.real.max()), (np.ceil(y.real.max()) - np.floor(y.real.min()))/tick_space))
        ax.set_zticks(np.arange(np.floor(y.imag.min()), np.ceil(y.imag.max()), (np.ceil(y.imag.max()) - np.floor(y.imag.min()))/tick_space))

        # Ensure grid lines are drawn on all planes
        ax.grid(True)
        ax.grid(color='black')
        ax.xaxis._axinfo["grid"].update({"color": "black", "linewidth": 0.5})
        ax.yaxis._axinfo["grid"].update({"color": "black", "linewidth": 0.5})
        ax.zaxis._axinfo["grid"].update({"color": "black", "linewidth": 0.5})
    
    # Define output path
    relative_path = os.path.join('..', 'Graphs', 'Exponential Decay', f'Exact with {lam}.png')

    plt.savefig(relative_path, bbox_inches='tight', pad_inches=0)
    plt.show()


#plot_exponential_function(domain = 'real', grid = 10, h = 1/5, lam = -1)
plot_exponential_function(domain = 'complex', grid = 20, h = 1/5, lam = -0.3+5j)
