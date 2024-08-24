import numpy as np
from scipy.optimize import fsolve
import math

def objective_function(x, c):
    """
    Objective function to be solved for |sum| = c
    """
    sum_expression = np.sum([(-5*x)**n / math.factorial(n) for n in range(5)])
    return np.abs(sum_expression) - c

def find_solutions(c, initial_guess=0.0):
    """
    Find the roots of the objective function for the given constant c.
    
    Parameters:
    c (float): The constant value to solve for
    initial_guess (float): Initial guess for the root-finding algorithm
    
    Returns:
    numpy.ndarray: Array of solutions (x values) for |sum| = c
    """
    solutions = fsolve(objective_function, initial_guess, args=(c,))
    return solutions

# Example usage
c = 0.9
solutions = find_solutions(c)
print(f"Solutions for |sum| = {c}:")
print(solutions)
