import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter as formatter
import os

cmap = mpl.colormaps['magma_r']
# Take colors at regular intervals spanning the colormap
colors = cmap(np.linspace(0, 1, 10))

# Declare Steps
z_1 = lambda l, a, b: (a + b*1j)*l
z_2 = lambda l, a, b: ((1-a) - b*1j)*l

# Stability Function for Euler's Forward 2-step
EF = ["Euler's Forward", lambda l, a, b: (1 + z_1(l, a, b)) * (1 + z_2(l, a, b))]

EB = ["Euler's Backward", lambda l, a, b: 1/(1 - z_1(l, a, b)) * 1/(1 - z_2(l, a, b))]

rk4_poly = lambda x: 1 + x + (x**2)/2 + (x**3)/6 + (x**4)/24
RK4 = ["Runge-Kutta 4", lambda l, a, b: rk4_poly(z_1(l, a, b)) * rk4_poly(z_2(l, a, b))]


# Plot the Stability Region for a given Stability Function
def plot_Region(stability_function, grid, points):

    # Generate domain (complex grid)
    grid_scale = grid / 10
    x = grid / 2
    real_domain = np.linspace(-x, x, points)
    imag_domain = np.linspace(-x, x, points)
    real, imag = np.meshgrid(real_domain, imag_domain)
    domain = real + 1j * imag

    # Evaluate Stability Region
    name = stability_function[0]
    function = stability_function[1]
    # Real
    a_r = 0.5
    b_r = 0
    realRange = function(domain, a_r, b_r)
    realDistance = np.abs(realRange)
    # Complex
    a_c = 0.5
    b_c = 0.5
    complexRange = function(domain, a_c, b_c)
    complexDistance = np.abs(complexRange)

    # Define the Figure
    plt.figure(figsize=(grid, grid), facecolor='white', edgecolor='black')
    ax = plt.gca()

    # Plot the Stability Region
    # Real
    plt.contour(real, imag, realDistance, levels=[1], colors=[colors[3]], linewidths=1)  # Boundary
    plt.contourf(real, imag, realDistance, levels=[0, 1], colors=[colors[3]], alpha=0.75)  # Fill
    # Complex
    plt.contour(real, imag, complexDistance, levels=[1], colors=[colors[6]], linewidths=1)  # Boundary
    plt.contourf(real, imag, complexDistance, levels=[0, 1], colors=[colors[6]], alpha=0.75)  # Fill

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
    plt.xticks(np.arange(-int(x), int(x) + 1, 1*grid_scale), fontsize=15*grid_scale, color='black')
    plt.yticks(np.arange(-int(x), int(x) + 1, 1*grid_scale), fontsize=15*grid_scale, color='black')

    # Remove tick marks
    plt.tick_params(axis='both', which='both', length=0, pad=10*grid_scale)

    # Set border (spines) linewidth
    for spine in ax.spines.values():
        spine.set_linewidth(0.75)
        spine.set_color('black')

    # Labelling
    plt.xlabel('$Real$', fontsize=15*grid_scale, color='black')
    plt.ylabel('$Imaginary$', fontsize=15*grid_scale, color='black')

    # Legend with "Real" and "Complex" labels in colors matching the plot
    plt.legend(labels=['Real', 'Complex'], labelcolor=[colors[3], colors[6]], fontsize=15*grid_scale, loc='upper right', facecolor='white', edgecolor='black', handletextpad=0, handlelength=0)


    # Save plot as a frame
    plt.savefig(f'/home/puca/University/Senior Sophister/Capstone/Graphs/Stability Regions/Graphs/Real VS Complex Comparison/{name}.png', bbox_inches='tight', pad_inches=0)
    plt.show()

plot_Region(EB, 20, 2**13)
