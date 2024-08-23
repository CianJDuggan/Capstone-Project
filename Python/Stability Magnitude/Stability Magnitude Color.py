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
    unstable_mags = np.where(magnitudes > 1, magnitudes, np.nan)
  
        # Define the Figure
    plt.figure(figsize=(grid, grid), facecolor='white', edgecolor='black')
    ax = plt.gca()

    # Plot the Stability Region
    plt.contourf(real, imag, stable_mags, levels=[0,0.2,0.4,0.6,0.8,1], cmap=cmap)
    cbar = plt.colorbar(label='Magnitude', format='%.2f', ticks=[0, 0.2, 0.4, 0.6, 0.8, 1])
    # Colorbar
    cbar.ax.tick_params(colors='black', labelsize=15)
    cbar.ax.yaxis.label.set_color('black')
    cbar.ax.yaxis.label.set_size(15)
    # Unstable region
    plt.contourf(real, imag, unstable_mags, levels=1, colors='white')
    # Boundary line
    plt.contour(real, imag, magnitudes, levels=[1], colors='black', linewidths=2)

    # Customize Imaginary axis tick labels to include 'i'
    def im_axis(x, pos):
        return f'{x:.0f}i' if x != 0 else '0'
    ax.yaxis.set_major_formatter(formatter(im_axis))
    ax.set_facecolor('white')

    # Plot bold lines for Real and Imaginary axes
    plt.axhline(0, color='black', linewidth=0.75)  # Imaginary axis
    plt.axvline(0, color='black', linewidth=0.75)  # Real axis

    # Set major grid lines for both Real and Imaginary axes
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    ax.set_box_aspect(1)
    ax.set_xlim(-x, x)
    ax.set_ylim(-x, x)
    plt.xticks(np.arange(-int(x), int(x) + 1, 1), fontsize=15, color='black')
    plt.yticks(np.arange(-int(x), int(x) + 1, 1), fontsize=15, color='black')

    # Remove tick marks
    plt.tick_params(axis='both', which='both', length=0, pad=10)

    # Set border (spines) linewidth
    for spine in ax.spines.values():
        spine.set_linewidth(0.75)
        spine.set_color('black')

    # Labelling
    plt.xlabel('$Real$', fontsize=15, color='black')
    plt.ylabel('$Imaginary$', fontsize=15, color='black')
    
    relative_path = os.path.join('..', '..', 'Graphs',  'Stability Magnitude', 'Color', f'{name}.png')
    plt.savefig(relative_path, bbox_inches='tight', pad_inches=0)
    plt.show()

# Iterate through each function in Functions
plot_stability_region(RK4, 10, 2**12, cmap)

