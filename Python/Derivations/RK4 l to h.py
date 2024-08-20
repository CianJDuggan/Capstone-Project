import sympy as sp
import numpy as np
from scipy.optimize import fsolve

# Define the RK4 stability polynomial
RK4 = lambda z: 1 + z + z**2/2 + z**3/6 + z**4/24

h = sp.symbols('h', real=True, positive=True)
l = 0.5+5j

poly = RK4(h*l)
print(poly)
