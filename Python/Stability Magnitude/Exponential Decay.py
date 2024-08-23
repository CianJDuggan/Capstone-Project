import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

cmap = mpl.colormaps['magma']
colors = cmap(np.linspace(0, 1, 10))
background = 'white'
foreground = 'black'

EF = ["Euler's Forward", lambda l, h: (l*h) + 1]
EB = ["Euler's Backward", lambda l, h: 1/(1 - (l*h))]
RK4 = ["Runge-Kutta 4", lambda l, h: ((l*h)**4)/24 + ((l*h)**3)/6 + ((l*h)**2)/2 + (l*h) + 1]

def plot_exponential_function(domain, grid, h_values, lam, method):
    # Size and time steps
    t = np.arange(0, grid, 1/1000)

    ## Exact ##
    y = np.exp(lam * t)
    
    ## Method ##
    t_steps = np.arange(0, grid+1, 1)
        
    ## Plot ##
    # Instantiate the graph
    plt.figure(figsize=(10, 10), facecolor=background, edgecolor=foreground)
    ax = plt.gca()
    
    # Exact
    ax.plot(t, y, color=foreground)
    
    # Method
    for h in h_values:
        index = h_values.index(h)
        y_steps = method[1](lam, h) ** t_steps
        y_method = np.interp(t, t_steps, y_steps)
        ax.plot(t, y_method, color=colors[2*index], linestyle='--')
        ax.plot(t_steps, y_steps, color=colors[2*index], marker='o', markersize=5, linestyle='none')

    # Graph settings
    ax.set_ylabel('$y$', color=foreground, fontsize=15)
    ax.set_facecolor(background)
    plt.axhline(0, color=foreground, linewidth=0.75)  # y-axis
    plt.axvline(0, color=foreground, linewidth=0.75)  # x-axis
    for spine in ax.spines.values():
        spine.set_linewidth(0.75)
        spine.set_color(foreground)
    ax.set_xlim(0, grid)
    ax.set_ylim(-grid/4, grid/4)
    ax.set_aspect(aspect='equal')  # Set the aspect ratio to 1:1
    plt.xticks(np.arange(0, grid+1, 1), fontsize=15, color=foreground)
    plt.yticks(np.arange(-(grid/4), (grid/4)+1, 1), fontsize=15, color=foreground)
    ax.set_xlabel('$t$', color=foreground, fontsize=15)
    ax.legend([f'Exact with $\lambda ={lam}$', f'$h = {h_values[0]}$', f'$h = {h_values[1]}$', f'$h = {h_values[2]}$', f'$h = {h_values[3]}$', f'$h = {h_values[4]}$'], labelcolor=[foreground, colors[0], colors[2], colors[4], colors[6], colors[8]], facecolor='white', edgecolor='black', fontsize=15, loc='lower right', handletextpad=0, handlelength=0, markerscale=0)

    relative_path = os.path.join('..', '..', 'Graphs',  'Stability Magnitude', 'Exponential Decay', f'{method[0]}.png')
    plt.savefig(relative path, bbox_inches='tight', pad_inches=0)

    plt.show()

# Euler's Forward
#plot_exponential_function(domain = 'real', grid = 10, lam = -5, method = EF, h_values = [0.02, 0.06, 0.1, 0.14, 0.18])

# Euler's Backward
#plot_exponential_function(domain = 'real', grid = 10, lam = -5, method = EB, h_values = [0.02222, 0.08571, 0.2, 0.46667, 1.8])

# Runge-Kutta 4
plot_exponential_function(domain = 'real', grid = 10, lam = -5, method = RK4, h_values = [0.02107213, 0.07134797, 0.13911561, 0.25762445, 0.31926346])
