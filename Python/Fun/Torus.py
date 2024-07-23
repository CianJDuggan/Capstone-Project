import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap

# Reading normalized RGB values from the file
file_path = '/home/puca/.cache/wal/colors-RGB.txt'

with open(file_path, 'r') as file:
    normalized_rgb_values = np.loadtxt(file, delimiter=',')

# Creating the colormap
cmap = ListedColormap(normalized_rgb_values)

# Function to generate torus points
def generate_torus(R, r, num_points=100):
    u = np.linspace(0, 2 * np.pi, num_points)
    v = np.linspace(0, 2 * np.pi, num_points)
    u, v = np.meshgrid(u, v)
    
    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)
    
    return x, y, z

# Set the torus parameters
major_radius = 4
minor_radius = 2
# Generate torus points
torus_x, torus_y, torus_z = generate_torus(major_radius, minor_radius)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(torus_x, torus_y, torus_z, rstride=5, cstride=5, color = cmap(0), edgecolors=cmap(0.4), alpha=0.25)

# Ensure equal scaling for all axes
ax.set_box_aspect([np.ptp(coord) for coord in [torus_x, torus_y, torus_z]])
ax.set_axis_off()

# Animation function
def update(frame):
    azim = frame  # Azimuthal rotation
    elev = np.sin(np.radians(frame/25)) * 360  # Elevation oscillation
    ax.view_init(elev=elev, azim=azim)

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360*50, 1), interval=50)

# Show the plot
plt.show()
