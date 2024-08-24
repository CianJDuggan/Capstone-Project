import sympy as sp

# Define symbols
a, b, c, d, = sp.symbols('a b c d', real=True)
i = sp.I

# Define complex numbers
z1 = a + b*i
z2 = c + d*i

# Define stability equations with names and corresponding lambda functions for s1
stability_equation = {
    'RK4': ["Runge-Kutta 4", lambda z: 1 + z + z**2/2 + z**3/6 + z**4/24]
}

# Expand the stability equation
step_one = stability_equation['RK4'][1](z1)
step_two = stability_equation['RK4'][1](z2)

equation = step_one * step_two
equation = sp.expand(equation)
equation = sp.collect(equation, i)
equation = sp.latex(equation)
# Print the expanded stability equation
print(equation)
