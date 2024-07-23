import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Stability Functions
EF = ["Euler's Forward", lambda l: l + 1]
EB = ["Euler's Backward", lambda l: 1/(1 - l)]
RK4 = ["Runge-Kutta 4", lambda l: (l**4)/24 + (l**3)/6 + (l**2)/2 + l + 1]

def plot_exponential_function_3d(h, lam, method, domain):
    t = np.arange(0, 10, 1/1000)
    steps = round(10/h)
    t_step = np.linspace(0, 10, steps)

    y_exact = np.exp(lam * t)

    method_name = method[0]
    method_func = method[1]
    y_method_step = method_func(lam)**t_step
    y_method = np.interp(t, t_step, y_method_step)

    fig = plt.figure()

    if domain == 'real':
        ax = fig.add_subplot(111)
        ax.plot(t, y_exact.real, label='Exact', color='white')
        ax.plot(t, y_method.real, label=f'{method_name}', color='red', linewidth=1)
        ax.plot(t_step, y_method_step.real, 'o', color='red')
        ax.set_ylabel('$y$')
        ax.set_title(r'$ \lambda = {}$'.format(lam))
        ax.set_box_aspect(1)


    elif domain == 'complex':
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(t, y_exact.real, y_exact.imag, label='Exact', color='white')
        ax.plot(t, y_method.real, y_method.imag, label=f'{method_name}', color='red', linewidth=1)
        ax.plot(t_step, y_method_step.real, y_method_step.imag, 'o', color='red')
        ax.set_ylabel('$Re(y)$')
        ax.set_zlabel('$Im(y)$')
        ax.set_title(r'$ \lambda = {}$'.format(lam))

    ax.set_xlabel('$t$') 


    plt.legend()

    plt.savefig(f'/home/puca/University/Senior Sophister/Capstone/Graphs/Exponential Decay/{method_name} with {lam}.png')
    plt.show()


plot_exponential_function_3d(h = 1/5, lam = -0.5-0.5j, method = EB, domain = 'complex')
