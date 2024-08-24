import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter as formatter

cmap = mpl.colormaps['magma_r']
# Take colors at regular intervals spanning the colormap
colors = cmap(np.linspace(0, 1, 10))

# Declare Steps
z_1 = lambda l, a, b: a*l + b*1j
z_2 = lambda l, a, b: (1-a)*l - b*1j

# Stability Function for Euler's Forward 2-step
EF = ["Euler's Forward", lambda l, a, b: (1 + z_1(l, a, b)) * (1 + z_2(l, a, b))]

EB = ["Euler's Backward", lambda l, a, b: 1/(1 - z_1(l, a, b)) * 1/(1 - z_2(l, a, b))]

rk4_poly = lambda x: 1 + x + (x**2)/2 + (x**3)/6 + (x**4)/24
RK4 = ["Runge-Kutta 4", lambda l, a, b: rk4_poly(z_1(l, a, b)) * rk4_poly(z_2(l, a, b))]

# Define an array of a values
#varied_a = [[0.537], 0.537] #testing
varied_a = [np.arange(0, 1, 0.001), 0.5] # [a_values, b] where 0<a<1 and b is constant
varied_b = [0.5, np.arange(0, 4, 0.005)] # [a, b_values] where a is constant and 0<b<4

# Plot the Stability Region for a given Stability Function
def plot_Region(stability_function, grid, points, aORb, frame_number):

    # Unpack the stability function and varied values for a or b
    if aORb == 'a':
        a_values = varied_a[0]
        b = varied_a[1]
        a = a_values[frame_number]
        subdir = 'Varied a'
        const = 'b'
        const_val = b
    elif aORb == 'b':
        a = varied_b[0]
        b_values = varied_b[1]
        b = b_values[frame_number]
        subdir = 'Varied b'
        const = 'a'
        const_val = a
    else:
        raise ValueError('Invalid input for aORb')

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
    Range = function(domain, a, b)
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

    # a & b values legend
    plt.legend([f'a = {a:.3f}\nb = {b:.3f}'], loc='upper right', fontsize=15*grid_scale, facecolor='white', edgecolor='black', labelcolor='black', handletextpad=0, handlelength=0)


    # Save plot as a frame
    relative_path = os.path.join('..', '..', '..', 'Graphs',  'Stability Regions', 'Videos')
    video_path = os.path.join(subdir, name, f"{const}={const_val}", 'frames')
    output_path = os.path.join(relative_path, video_path)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    frame_path = f'{frame_number:04d}.png'
    path = os.path.join(output_path, frame_path)
    plt.savefig(path, bbox_inches='tight', pad_inches=0)

    output_dir = f'/home/puca/University/Senior Sophister/Capstone/Graphs/Stability Regions/Videos/{subdir}/{name}/{const}={const_val}/frames'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    plt.savefig(f'{output_dir}/{frame_number:04d}.png')
    #plt.show()
    plt.close()

# Generate frames for Stability Function with multiple a or b values
for i, b in enumerate(varied_b[1]):
    plot_Region(RK4, 40, 1000, 'b', i)
