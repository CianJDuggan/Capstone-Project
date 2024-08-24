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

def plot_exponential_function(domain, grid, h_stable, h_unstable, lam, method, pos, red_width):
    # Size and time steps
    t = np.arange(0, grid, 1/1000)

    ## Exact ##
    y = np.exp(lam * t)
    
    ## Method ##
    
    # Stable
    t_steps_stable = np.arange(0, grid+1, 1)
    y_steps_stable = method[1](lam, h_stable) ** t_steps_stable
    y_method_stable = np.interp(t, t_steps_stable, y_steps_stable)
    
    # Unstable
    t_steps_unstable = np.arange(0, grid+1, 1)
    y_steps_unstable = (method[1](lam, h_unstable) ** t_steps_unstable)
    y_method_unstable = np.interp(t, t_steps_unstable, y_steps_unstable)
    
    ## Plot ##
    if domain == 'real':
        # Instantiate the graph
        plt.figure(figsize=(10, 10), facecolor=background, edgecolor=foreground)
        ax = plt.gca()
        
        # Exact
        ax.plot(t, y, color=foreground)
        
        # Stable
        ax.plot(t, y_method_stable, color='green', linestyle='--')
        ax.plot(t_steps_stable, y_steps_stable, color='green', marker='o', markersize=5, linestyle='none')
        # Unstable
        ax.plot(t, y_method_unstable, color='red', linestyle='--')
        ax.plot(t_steps_unstable, y_steps_unstable, color='red', marker='o', markersize=5, linestyle='none')

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
        h_stable = round(h_stable, 3)
        h_unstable = round(h_unstable, 3)
        plt.legend(labels=[r'$\lambda = {}$'.format(lam), r'$h = {}$'.format(h_stable), r'$h = {}$'.format(h_unstable) ], labelcolor=[foreground, 'green', 'red'], facecolor=background, edgecolor=foreground, fontsize=15, loc='upper right', handletextpad=0, handlelength=0, markerscale=0)



    elif domain == 'complex':
        # Instantiate the graph
        fig = plt.figure(figsize=(10, 10), facecolor=background, edgecolor=foreground)
        ax = fig.add_subplot(111, projection='3d', facecolor=background)
        ax.view_init(elev=22.5, azim=315, roll=0)
        
        # Exact
        ax.plot(t, y.real, y.imag, color=foreground, linewidth=1.5)
        # Valid
        ax.plot(t, y_method_stable.real, y_method_stable.imag, color='green', linewidth=2)
        #ax.plot(t_steps_stable, y_steps_stable.real, y_steps_stable.imag, color='green', marker='o', markersize=1)
        # Instable
        ax.plot(t, y_method_unstable.real, y_method_unstable.imag, color='red', linewidth=red_width)
        #ax.plot(t_steps_unstable, y_steps_unstable.real, y_steps_unstable.imag, color='red', marker='o', markersize=1)

        # Graph settings
        ax.set_xlabel('$t$', color=foreground)
        ax.set_ylabel('$Re(y)$', color=foreground)
        ax.set_zlabel('$Im(y)$', color=foreground)
        plt.legend(labels=[r'$\lambda = {}$'.format(lam), r'$h = {}$'.format(h_stable), r'$h = {}$'.format(h_unstable) ], labelcolor=[foreground, 'green', 'red'], facecolor=background, edgecolor=foreground, fontsize=15, loc=(pos[0], pos[1]), handletextpad=0, handlelength=0, framealpha=1)
        ax.xaxis.set_pane_color(background)
        ax.yaxis.set_pane_color(background)
        ax.zaxis.set_pane_color(background)
        ax.xaxis.line.set_color(foreground)
        ax.yaxis.line.set_color(foreground)
        ax.zaxis.line.set_color(foreground)
        ax.tick_params(axis='x', colors=foreground)
        ax.xaxis._axinfo['tick']['inward_factor'] = 0
        ax.xaxis._axinfo['tick']['outward_factor'] = 0
        ax.tick_params(axis='y', colors=foreground)
        ax.yaxis._axinfo['tick']['inward_factor'] = 0
        ax.yaxis._axinfo['tick']['outward_factor'] = 0
        ax.tick_params(axis='z', colors=foreground)
        ax.zaxis._axinfo['tick']['inward_factor'] = 0
        ax.zaxis._axinfo['tick']['outward_factor'] = 0

        ax.set_xlim(t.min(), t.max())

        y_real_max = max(y.real.max(), y_method_stable.real.max(), y_method_unstable.real.max())
        y_real_min = min(y.real.min(), y_method_stable.real.min(), y_method_unstable.real.min())
        ax.set_ylim(y_real_min, y_real_max)

        y_imag_max = max(y.imag.max(), y_method_stable.imag.max(), y_method_unstable.imag.max())
        y_imag_min = min(y.imag.min(), y_method_stable.imag.min(), y_method_unstable.imag.min())
        ax.set_zlim(y_imag_min, y_imag_max)

        ax.set_xticks(np.arange(np.floor(t.min()), np.ceil(t.max()) + 1, grid/5))
        ax.set_yticks(np.arange(np.floor(y_real_min), np.ceil(y_real_max) + 1, np.ceil(y_real_max/5)))
        ax.set_zticks(np.arange(np.floor(y_imag_min), np.ceil(y_imag_max) + 1, np.ceil(y_imag_max/5)))
        
        ax.grid(True)
        ax.grid(color=foreground)
        ax.xaxis._axinfo["grid"].update({"color": foreground, "linewidth": 0.5})
        ax.yaxis._axinfo["grid"].update({"color": foreground, "linewidth": 0.5})
        ax.zaxis._axinfo["grid"].update({"color": foreground, "linewidth": 0.5})
    
    relative_path = os.path.join('..', '..', 'Graphs', 'Exponential Decay', 'Exact vs Method', f'{method[0]} {domain}.png')
    plt.savefig(relative_path, bbox_inches='tight', pad_inches=0)

    plt.show()

# Euler's Forward
# Real
#plot_exponential_function(domain = 'real', grid = 10, h_stable = 1/6, h_unstable = 5/12, lam = -5, method = EF, pos = [0, 0], red_width = 2)
# Complex
#plot_exponential_function(domain = 'complex', grid = 300, h_stable = 0.03, h_unstable = 0.05, lam = -0.5+5j, method = EF, pos = [0.1, 0.3], red_width = 2)

# Euler's Backward
# Real
#plot_exponential_function(domain = 'real', grid = 10, h_stable = 1/6, h_unstable = 5/12, lam = -5, method = EB, pos = [0, 0], red_width = 2)
# Complex
#plot_exponential_function(domain = 'complex', grid = 300, h_stable = 0.03, h_unstable = 0.05, lam = -0.5+5j, method = EB, pos = [0.4, 0.2], red_width = 2)

# Runge-Kutta 4
# Real
#plot_exponential_function(domain = 'real', grid = 10, h_stable = 0.5, h_unstable = 0.57, lam = -5, method = RK4, pos = [0, 0], red_width = 2)
# Complex
plot_exponential_function(domain = 'complex', grid = 300, h_stable = 0.03, h_unstable = 0.5875, lam = -0.5+5j, method = RK4, pos = [0.4, 0.2], red_width = 0.5)
