import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

lam = -0.1+5j

def plot_exponential_function_3d(l):
    t = np.linspace(0, 30, 1000)
    y = np.exp(l * t)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(t, y.real, y.imag, label=f'$\lambda =$ {l}')

    ax.set_xlabel('$t$')
    ax.set_ylabel('$Re(y)$')
    ax.set_zlabel('$Im(y)$')
    ax.set_title('$y(t) = e^{\lambda t}$')

    plt.legend()
    plt.show()


plot_exponential_function_3d(lam)
