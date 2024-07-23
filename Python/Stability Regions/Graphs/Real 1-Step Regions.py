import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter as formatter

cmap = mpl.colormaps['magma_r']
# Take colors at regular intervals spanning the colormap
colors = cmap(np.linspace(0, 1, 10))

# Stability Functions
EF = ["Euler's Forward", lambda z: z + 1]
EB = ["Euler's Backward", lambda z: 1/(1 - z)]
RK4 = ["Runge-Kutta 4", lambda z: (z**4)/24 + (z**3)/6 + (z**2)/2 + z + 1]
stability_functions = [EF, EB, RK4]

def plot_Region(stability_function, grid, points):
    # Generate domain (complex grid)
    x = grid / 2
    real_domain = np.linspace(-x, x, points)
    imag_domain = np.linspace(-x, x, points)
    real, imag = np.meshgrid(real_domain, imag_domain)
    domain = real + 1j * imag

    # Evaluate Stability Region
    name = stability_function[0]
    function = stability_function[1]
    Range = function(domain)
    distance = np.abs(Range)

    # Define the Figure
    plt.figure(figsize=(grid, grid), facecolor='white', edgecolor='black')
    ax = plt.gca()

    # Plot the Stability Region
    plt.contour(real, imag, distance, levels=[1], colors=[colors[3]], linewidths=1)  # Boundary
    plt.contourf(real, imag, distance, levels=[0, 1], colors=[colors[3]], alpha=0.75)  # Fill

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

    plt.savefig(f'/home/puca/University/Senior Sophister/Capstone/Graphs/Stability Regions/Graphs/Real 1-Step/{name}.png')
    plt.show()

# Iterate through each function in Functions
# for s in stability_functions:
#     plot_Region(s, 10, 2**12)

plot_Region(RK4, 10, 2**13)
