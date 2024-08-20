import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

cmap = mpl.colormaps['magma']
colors = cmap(np.linspace(0, 1, 10))
background = 'white'
foreground = 'black'

EF = ["Euler's Forward", lambda l, h: (l*h) + 1 +0j]
EB = ["Euler's Backward", lambda l, h: 1/(1 - (l*h)) + 0j]
RK4 = ["Runge-Kutta 4", lambda l, h: ((l*h)**4)/24 + ((l*h)**3)/6 + ((l*h)**2)/2 + (l*h) + 1 +0j]

def plot_exponential_function(domain, grid, h_val, h_inval, lam, method, pos, real_component):
    # Size and time steps
    t = np.arange(0, grid, 1/1000)

    # Exact
    y = np.exp(lam * t)
    # Method
    t_steps_val = np.arange(0, grid, h_val)
    y_steps_val = method[1](lam, h_val) ** t_steps_val
    y_method_val = np.interp(t, t_steps_val, y_steps_val)
    # Inval
    t_steps_inval = np.arange(0, grid, h_inval)
    y_steps_inval = (method[1](lam, h_inval) ** t_steps_inval)
    y_method_inval = np.interp(t, t_steps_inval, y_steps_inval)
    
    if domain == 'real':
        # Instantiate the graph
        plt.figure(figsize=(10, 10), facecolor=background, edgecolor=foreground)
        ax = plt.gca()
        
        # Exact
        ax.plot(t, y, color=foreground)
        
        # Method
        if real_component == 'real':
            y_points_val = y_steps_val.real
            y_line_val = y_method_val.real
            y_points_inval = y_steps_inval.real
            y_line_inval = y_method_inval.real
        elif real_component == 'imag':
            y_points_val = y_steps_val.imag
            y_line_val = y_method_val.imag
            y_points_inval = y_steps_inval.imag
            y_line_inval = y_method_inval.imag
        elif real_component == 'mag':
            y_points_val = np.abs(y_steps_val)
            y_line_val = np.interp(t, t_steps_val, y_points_val)
            y_points_inval = np.abs(y_steps_inval)
            y_line_inval = np.interp(t, t_steps_inval, y_points_inval)
        
        # Valid
        ax.plot(t, y_line_val, color='green', linestyle='--')
        ax.plot(t_steps_val, y_points_val, color='green', marker='o', markersize=5, linestyle='none')
        # Invalid
        ax.plot(t, y_line_inval, color='red', linestyle='--')
        ax.plot(t_steps_inval, y_points_inval, color='red', marker='o', markersize=5, linestyle='none')

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
        h_val = round(h_val, 3)
        h_inval = round(h_inval, 3)
        plt.legend(labels=[r'$\lambda = {}$'.format(lam), r'$h = {}$'.format(h_val), r'$h = {}$'.format(h_inval) ], labelcolor=[foreground, 'green', 'red'], facecolor=background, edgecolor=foreground, fontsize=15, loc='upper right', handletextpad=0, handlelength=0, markerscale=0)
        plt.savefig(f'/home/puca/University/Senior Sophister/Capstone/Graphs/Exponential Decay/Exact vs Method/{method[0]} {domain}-{real_component}.png', bbox_inches='tight', pad_inches=0)



    elif domain == 'complex':
        # Instantiate the graph
        fig = plt.figure(figsize=(10, 10), facecolor=background, edgecolor=foreground)
        ax = fig.add_subplot(111, projection='3d', facecolor=background)
        ax.view_init(elev=22.5, azim=315, roll=0)
        
        # Exact
        ax.plot(t, y.real, y.imag, color=foreground, linewidth=1.5)
        # Valid
        ax.plot(t, y_method_val.real, y_method_val.imag, color='green', linewidth=2)
        #ax.plot(t_steps_val, y_steps_val.real, y_steps_val.imag, color='green', marker='o', markersize=1)
        # Inval
        ax.plot(t, y_method_inval.real, y_method_inval.imag, color='red', linewidth=0.5)
        #ax.plot(t_steps_inval, y_steps_inval.real, y_steps_inval.imag, color='red', marker='o', markersize=1)

        # Graph settings
        ax.set_xlabel('$t$', color=foreground)
        ax.set_ylabel('$Re(y)$', color=foreground)
        ax.set_zlabel('$Im(y)$', color=foreground)
        plt.legend(labels=[r'$\lambda = {}$'.format(lam), r'$h = {}$'.format(h_val), r'$h = {}$'.format(h_inval) ], labelcolor=[foreground, 'green', 'red'], facecolor=background, edgecolor=foreground, fontsize=15, loc=(pos[0], pos[1]), handletextpad=0, handlelength=0, framealpha=1)
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

        y_real_max = max(y.real.max(), y_method_val.real.max(), y_method_inval.real.max())
        y_real_min = min(y.real.min(), y_method_val.real.min(), y_method_inval.real.min())
        ax.set_ylim(y_real_min, y_real_max)

        y_imag_max = max(y.imag.max(), y_method_val.imag.max(), y_method_inval.imag.max())
        y_imag_min = min(y.imag.min(), y_method_val.imag.min(), y_method_inval.imag.min())
        ax.set_zlim(y_imag_min, y_imag_max)

        ax.set_xticks(np.arange(np.floor(t.min()), np.ceil(t.max()) + 1, grid/5))
        ax.set_yticks(np.arange(np.floor(y_real_min), np.ceil(y_real_max) + 1, np.ceil(y_real_max/5)))
        ax.set_zticks(np.arange(np.floor(y_imag_min), np.ceil(y_imag_max) + 1, np.ceil(y_imag_max/5)))
        
        ax.grid(True)
        ax.grid(color=foreground)
        ax.xaxis._axinfo["grid"].update({"color": foreground, "linewidth": 0.5})
        ax.yaxis._axinfo["grid"].update({"color": foreground, "linewidth": 0.5})
        ax.zaxis._axinfo["grid"].update({"color": foreground, "linewidth": 0.5})
        plt.savefig(f'/home/puca/University/Senior Sophister/Capstone/Graphs/Exponential Decay/Exact vs Method/{method[0]} {domain}.png', bbox_inches='tight', pad_inches=0)


    plt.show()

# Euler's Forward
# Real
#plot_exponential_function(domain = 'real', grid = 10, h_val = 1/6, h_inval = 5/12, lam = -5, method = EF, pos = [0, 0], real_component = 'mag')
# Complex
#plot_exponential_function(domain = 'complex', grid = 300, h_val = 0.03, h_inval = 0.05, lam = -0.5+5j, method = EF, pos = [0.2, 0.3], real_component = 'mag')

# Euler's Backward
# Real
#plot_exponential_function(domain = 'real', grid = 10, h_val = 1/6, h_inval = 5/12, lam = -5, method = EB, pos = [0, 0], real_component = 'mag')
# Complex
#plot_exponential_function(domain = 'complex', grid = 300, h_val = 0.03, h_inval = 0.05, lam = -0.5+5j, method = EB, pos = [0.4, 0.2], real_component = 'mag')

# Runge-Kutta 4
# Real
#plot_exponential_function(domain = 'real', grid = 10, h_val = 0.5, h_inval = 0.57, lam = -5, method = RK4, pos = [0, 0], real_component = 'real')
# Complex
plot_exponential_function(domain = 'complex', grid = 300, h_val = 0.03, h_inval = 0.5875, lam = -0.5+5j, method = RK4, pos = [0.4, 0.2], real_component = 'mag')
