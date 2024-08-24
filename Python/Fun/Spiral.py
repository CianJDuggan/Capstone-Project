import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

phi = 1.618033988749895
lam = (-0.1 + 4j) * phi

def plot_exponential_function_3d(l):
    t = np.linspace(0, 30, 1000)
    y = np.exp(l * t)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(t, y.real, y.imag, label=f'$\lambda =$ {l}')

    ax.set_xlabel('$t$')
    ax.set_ylabel('$Re(y)$')
    ax.set_zlabel('$Im(y)$')
    ax.set_title('$y(t) = e^{\lambda t}$')

    plt.legend()
    plt.show()


plot_exponential_function_3d(lam)
