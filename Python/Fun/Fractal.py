import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter as formatter
from matplotlib.colors import LinearSegmentedColormap, Normalize
import matplotlib as mpl

cmap = mpl.colormaps['magma_r']
# Take colors at regular intervals spanning the colormap
colors = cmap(np.linspace(0, 1, 10))

# Define stability functions
def euler_forward(z):
    return z + 1

def euler_backward(z):
    return 1 / (1 - z)

def runge_kutta_4(z):
    return (z**4) / 24 + (z**3) / 6 + (z**2) / 2 + z + 1

stability_functions = [
    {"name": "Euler's Forward Method", "function": euler_forward},
    {"name": "Euler's Backward Method", "function": euler_backward},
    {"name": "Runge-Kutta 4", "function": runge_kutta_4}
]

def plot_stability_region(stability, grid, points, cmap):
    # Generate domain (complex grid)
    x = grid/2
    real_domain = np.linspace(-x, x, points)
    imag_domain = np.linspace(-x, x, points)
    real, imag = np.meshgrid(real_domain, imag_domain)
    domain = real + 1j * imag

    # Evaluate Stability Region
    name = stability["name"]
    function = stability["function"]
    distances = np.abs(function(domain))
  
    # Define the Figure
    plt.figure(figsize=(grid, grid))

    # Plot the Stability Region using Colormap
    plt.imshow(distances, extent=(-x, x, -x, x), cmap=cmap, origin='lower', norm=Normalize(vmin=0, vmax=1))
    plt.colorbar(label='Distance')

    # Customize Imaginary axis tick labels to include 'i'
    def im_axis(x, pos):
        return f'{x:.0f}i' if x != 0 else '0'
    
    plt.gca().yaxis.set_major_formatter(formatter(im_axis))

    # Set major grid lines for both Real and Imaginary axes
    plt.grid(which='major', linestyle='-', linewidth='0.5')
    plt.xticks(np.arange(-int(x), int(x)+1, 1))
    plt.yticks(np.arange(-int(x), int(x)+1, 1))

    # Labelling
    plt.title(f'{name} Stability Region')
    plt.xlabel('$Real$')
    plt.ylabel('$Imaginary$')
    
    plt.savefig(f'/home/puca/University/Senior Sophister/Capstone/Graphs/Fun/{name}.png')
    plt.show()

# Iterate through each function in Functions
for stability in stability_functions:
    plot_stability_region(stability, 10, 2**12, cmap)

