import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter as formatter
from matplotlib.colors import LinearSegmentedColormap, Normalize
import matplotlib as mpl

cmap = mpl.colormaps['magma_r']
# Take colors at regular intervals spanning the colormap
colors = cmap(np.linspace(0, 1, 10))

# Define stability functions
EF = ["Euler's Forward", lambda z: z + 1]
EB = ["Euler's Backward", lambda z: 1/(1 - z)]
RK4 = ["Runge-Kutta 4", lambda z: (z**4)/24 + (z**3)/6 + (z**2)/2 + z + 1]

def plot_stability_region(method, grid, points, cmap):
    # Generate domain (complex grid)
    x = grid/2
    real_domain = np.linspace(-x, x, points)
    imag_domain = np.linspace(-x, x, points)
    real, imag = np.meshgrid(real_domain, imag_domain)
    domain = real + 1j * imag

    # Evaluate Stability Region
    name = method[0]
    function = method[1]
    magnitudes = np.abs(function(domain))
    stable_mags = np.where(magnitudes < 1, magnitudes, np.nan)
    unstable_mags = np.where(magnitudes >= 1, magnitudes, np.nan)
  
    # Define the Figure
    fig = plt.figure(figsize=(grid, grid), facecolor='white', edgecolor='black')
    ax = fig.add_subplot(111, projection='3d', facecolor='white')
    ax.view_init(elev=22.5, azim=22.5, roll=0)

    X, Y, Z = real, imag, stable_mags
    ax.plot_surface(X,Y,Z, edgecolor=colors[3], color=colors[3], linewidth=0.5, alpha=0.3, rcount=100, ccount=100, shade=False)
    ax.contourf(X, Y, Z, zdir='z', offset=0, levels=100, cmap=cmap)
    ax.set_zlim(0, 1)
    ax.set_zticks(np.arange(0, 1.2, 0.2))

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

    # Axes
    ax.set_xlabel('Real', color='black')
    ax.set_ylabel('Imaginary', color='black')
    ax.set_zlabel('Magnitude', color='black')
    ax.set_xlim(-(x+1), x+1)
    ax.set_xticks(np.arange(-x, x+1, 2))
    ax.set_ylim(-(x+1), x+1)
    ax.set_yticks(np.arange(-x, x+1, 2))
    
    relative_path = os.path.join('..', '..', 'Graphs',  'Stability Magnitude', '3D', f'{name}.png')
    plt.savefig(relative_path, bbox_inches='tight', pad_inches=0)
    plt.show()

# Iterate through each function in Functions
plot_stability_region(RK4, 10, 2**12, cmap)

