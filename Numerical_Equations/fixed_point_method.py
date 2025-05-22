import math
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from latex_utils import latex_to_python, create_function

def fixed_point_method(g, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise RuntimeError(f"Failed to converge after {max_iter} iterations, try a different g(x) transformation")

def get_user_input():
    print("\nFixed Point Method")
    print("For equation f(x) = 0, rewrite it as x = g(x)")
    print("The method uses simple iteration:")
    print("x_{n+1} = g(x_n)")
    print("\nConvergence requires |g'(x)| < 1 near the solution")
    print("\nExample: For equation x^2 - 4 = 0")
    print("Rewrite as:")
    print("1) x = \\sqrt{4} or")
    print("2) x = \\frac{x^2 + 4}{2}")
    print("\nEnter iteration function g(x) in LaTeX format:")
    g_expr = input("g(x) = ")
    print("\nEnter initial guess x_0 (can use \\frac{a}{b} for fractions):")
    x0_expr = input("x_0 = ")
    
    try:
        x0_expr = latex_to_python(x0_expr)
        x0 = float(eval(x0_expr, {"math": math}))
    except Exception as e:
        raise ValueError(f"Invalid initial guess. Use LaTeX format (e.g., \\frac{{1}}{{2}} for 1/2): {str(e)}")
    
    g = create_function(g_expr)
    return g, x0

if __name__ == "__main__":
    try:
        print("\nFixed Point Method for Root Finding")
        print("==================================")
        g, x0 = get_user_input()
        result = fixed_point_method(g, x0)
        print(f"\nFixed point found: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")