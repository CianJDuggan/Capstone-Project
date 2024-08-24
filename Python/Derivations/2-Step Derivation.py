import sympy as sp
import re

# Define symbols
a, b, h, l = sp.symbols('a b h l')
i = sp.I

# Define the complex step pair
z = [a + b*i, h - (a + b*i)]

# Set fixed values for a and b (change these values to test different cases)
a_fixed = h / 2
b_fixed = h / 2  # b=0 for real 2-step

# Set fixed value for l (change this value to test different cases)
# Remember that Re(l) < 0 and l \in C
l_fixed = -1

# Dictionary of methods and corresponding stability equations for 1-step
stability_equations = {
    'EF': ("Euler's Forward Method", lambda l, t: 1 + (l*t)),
    'EB': ("Euler's Backward Method", lambda l, t: 1/(1 - (l*t))),
    'RK4': ("Runge-Kutta 4", lambda l, t: 1 + (l*t) + (l*t)**2/2 + (l*t)**3/6 + (l*t)**4/24)
}


def calculate_stability_equations(method_name, one_step_eq):
    """
    Calculate stability equations for a given method.
    
    Args:
    method_name (str): Name of the method
    one_step_eq (function): Lambda function for the 1-step stability equation
    
    Returns:
    dict: Dictionary containing all calculated stability equations
    """
    # 1-step stability equation in terms of lh
    one_step_general = one_step_eq(l, h)
    
    # Calculate the 1-step stability equation for each complex step
    first_step = one_step_eq(l, z[0])
    second_step = one_step_eq(l, z[1])
    
    # Combine the 1-step stability equations to get the 2-step stability equation
    two_step = sp.simplify(first_step * second_step)

    # Calculate various forms of the 2-step stability equation
    two_step_general = sp.expand(two_step)
    two_step_varied_a = sp.expand(sp.simplify(two_step.subs({a: a, b: b_fixed})))
    two_step_varied_b = sp.expand(sp.simplify(two_step.subs({a: a_fixed, b: b})))
    two_step_varied_l = sp.expand(sp.simplify(two_step.subs({a: a_fixed, b: b_fixed})))
    two_step_fixed = sp.expand(sp.simplify(two_step.subs({a: a_fixed, b: b_fixed, l: l_fixed})))

    # Collect terms for each expression, prioritizing l*h
    collect_order = [l*h, l, h, a, b]
    two_step_general = sp.collect(two_step_general, collect_order)
    two_step_varied_a = sp.collect(two_step_varied_a, collect_order)
    two_step_varied_b = sp.collect(two_step_varied_b, collect_order)
    two_step_varied_l = sp.collect(two_step_varied_l, collect_order)
    two_step_fixed = sp.collect(two_step_fixed, [h])

    return {
        "method_name": method_name,
        "one_step_general": one_step_general,
        "two_step_general": two_step_general,
        "two_step_varied_a": two_step_varied_a,
        "two_step_varied_b": two_step_varied_b,
        "two_step_varied_l": two_step_varied_l,
        "two_step_fixed": two_step_fixed
    }


def custom_latex(expr):
    """
    Convert expression to LaTeX with custom substitutions.
    
    Args:
    expr (sympy.Expr): The expression to convert
    
    Returns:
    str: LaTeX representation of the expression with custom substitutions
    """
    latex_str = sp.latex(expr)
    
    # Replace l*h or h*l with \lh
    latex_str = re.sub(r'(l\s*\*\s*h|h\s*\*\s*l)', r'\\lh', latex_str)
    
    # Replace remaining l with \lambda, but not if it's part of \lh
    latex_str = re.sub(r'(?<!\\)l(?!h)', r'\\lambda', latex_str)
    
    # Add $ delimiters
    return f"${latex_str}$"


def print_results(results):
    """
    Print the results for a given method.
    
    Args:
    results (dict): Dictionary containing all calculated stability equations
    """
    print(f"\n{results['method_name']}:")
    print(f"General 1-Step: {custom_latex(results['one_step_general'])}")
    print(f"General 2-Step: {custom_latex(results['two_step_general'])}")
    print(f"2-Step (b = {b_fixed}): {custom_latex(results['two_step_varied_a'])}")
    print(f"2-Step (a = {a_fixed}): {custom_latex(results['two_step_varied_b'])}")
    print(f"2-Step (a = {a_fixed}, b = {b_fixed}): {custom_latex(results['two_step_varied_l'])}")
    print(f"2-Step (a = {a_fixed}, b = {b_fixed}, l = {l_fixed}): {custom_latex(results['two_step_fixed'])}")
    print("")

def main():
    print(f"\nEvaluated Results for a = {a_fixed} and b = {b_fixed}")
    for method_name, (full_name, one_step_eq) in stability_equations.items():
        results = calculate_stability_equations(full_name, one_step_eq)
        print_results(results)

if __name__ == "__main__":
    main()




    # Check if the equation needs to be represented as a fraction
#    if sp.denom(1_step) != 1:
#        numerator, denominator = sp.fraction(1_step)
#        1_step = (numerator * (1 / numerator)) / sp.simplify((denominator * (1 / numerator)))

#    if sp.denom(2_step) != 1:
#        numerator, denominator = sp.fraction(2_step)
#        2_step = (numerator * (1 / numerator)) / sp.simplify((denominator * (1 / numerator)))

    # Expand the general 2_step expression
#    2_step_expanded = sp.expand(2_step_dict[key])
