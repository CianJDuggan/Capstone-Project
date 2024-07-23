import sympy as sp

# Define symbols
a, b, lh = sp.symbols('a b lh', real=True)
i = sp.I

# Define complex numbers
z1 = a + b*i
z2 = lh - z1

# Define stability equations with names and corresponding lambda functions for s1
stability_equations = {
    'EF': ["Euler's Forward Method", lambda z: 1 + z],
    'EB': ["Euler's Backward Method", lambda z: 1/(1 - z)],
    'RK4': ["Runge-Kutta 4", lambda z: 1 + z + z**2/2 + z**3/6 + z**4/24]
}

# Dictionary to store s2 functions for each stability equation
s2_dict = {}

# Multiply the series expansions for each stability equation and store in s2_dict
for key, (name, s1) in stability_equations.items():
    s2 = sp.simplify(s1(z1) * s1(z2))
    s2_dict[key] = s2

# Define a lambda function to evaluate and simplify the product with a and b as functions of lh
evaluate_product = lambda s2_func, a_expr, b_expr: sp.simplify(s2_func.subs({a: a_expr, b: b_expr}))

# Function to apply fraction tweak
def apply_fraction_tweak(expr):
    if sp.denom(expr) != 1:
        numerator, denominator = sp.fraction(expr)
        return (numerator * (1 / numerator)) / sp.simplify((denominator * (1 / numerator)))
    return expr

# Example usage
a_expr = lh / 2
b_expr = lh / 2

# Print evaluated results with specific formatting
print("\nEvaluated Results for \na = {} \nb = {}".format(a_expr, b_expr))
for key, (name, s1) in stability_equations.items():
    s2 = evaluate_product(s2_dict[key], a_expr, b_expr)
    s1 = sp.simplify(s1(lh))  # Evaluate s1 with lh instead of z

    s1 = apply_fraction_tweak(s1)
    s2 = apply_fraction_tweak(s2)

    # Expand the general s2 expression
    s2_expanded = sp.expand(s2_dict[key])

    print(f"\n{name}:")
    print(f"S_1: {s1}")
    print(f"S_2: {s2}")
    print(f"General S_2: {s2_expanded}")  # Output the general expression for s2

    # New additions: Calculate S_2 with a = lh/2 and b as variable
    s2_new = evaluate_product(s2_dict[key], lh/2, b)
    s2_new_expanded = sp.expand(s2_new)
    s2_new_tweaked = apply_fraction_tweak(s2_new_expanded)
    
    real_part = sp.re(s2_new_expanded)
    imag_part = sp.im(s2_new_expanded)

    # Simplify and factor real and imaginary parts
    real_part_factored = sp.factor(real_part)
    imag_part_factored = sp.factor(imag_part)

    # Apply fraction tweak to real and imaginary parts
    real_part_tweaked = apply_fraction_tweak(real_part_factored)
    imag_part_tweaked = apply_fraction_tweak(imag_part_factored)

    print(f"\nS_2 (a = lh/2, b as variable): {s2_new_tweaked}")
    print("Real part:")
    print(f"f = {real_part_tweaked}")
    print("Imaginary part:")
    print(f"g = {imag_part_tweaked}")

print("")
