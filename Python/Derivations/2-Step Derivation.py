import sympy as sp

# Define symbols
a, b, lh = sp.symbols('a b lh')
i = sp.I

# Define complex numbers
#z1 = a + b*i
#z2 = lh - z1
z1 = lh/2
z2 = lh/2

# List of stability equations with names and corresponding lambda functions for s1
stability_equations = {
    'EF': ["Euler's Forward Method", lambda z: 1 + z],
    'EB': ["Euler's Backward Method", lambda z: 1/(1 - z)],
    'RK4': ["Runge-Kutta 4", lambda z: 1 + z + z**2/2 + z**3/6 + z**4/24]
    # Add more stability equations as needed
}

# Dictionary to store s2 functions for each stability equation
s2_dict = {}

# Multiply the series expansions for each stability equation and store in s2_dict
for key, (name, s1) in stability_equations.items():
    s2 = sp.simplify(s1(z1) * s1(z2))
    s2_dict[key] = s2

# Define a lambda function to evaluate and simplify the product with a and b as functions of lh
evaluate_product = lambda s2_func, a_expr, b_expr: sp.simplify(s2_func.subs({a: a_expr, b: b_expr}))

# Example usage
a_expr = lh / 2
b_expr = lh / 2

# Print evaluated results with specific formatting
print("\nEvaluated Results for \na = {} \nb = {}".format(a_expr, b_expr))
for key, (name, s1) in stability_equations.items():
    s2 = evaluate_product(s2_dict[key], a_expr, b_expr)
    s1 = sp.simplify(s1(lh))  # Evaluate s1 with lh instead of z

    # Check if the equation needs to be represented as a fraction
    if sp.denom(s1) != 1:
        numerator, denominator = sp.fraction(s1)
        s1 = (numerator * (1 / numerator)) / sp.simplify((denominator * (1 / numerator)))

    if sp.denom(s2) != 1:
        numerator, denominator = sp.fraction(s2)
        s2 = (numerator * (1 / numerator)) / sp.simplify((denominator * (1 / numerator)))

    # Expand the general s2 expression
    s2_expanded = sp.expand(s2_dict[key])

    print(f"\n{name}:")
    print(f"S_1: {s1}")
    print(f"S_2: {s2}")
    print(f"General S_2: {s2_expanded}")  # Output the general expression for s2
print("")
