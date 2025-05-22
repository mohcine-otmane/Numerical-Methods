import math
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from latex_utils import latex_to_python, create_function

def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x = x - fx/dfx
    raise RuntimeError(f"Failed to converge after {max_iter} iterations")

def get_user_input():
    print("\nNewton-Raphson Method")
    print("For a function f(x), the method uses iteration formula:")
    print("x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}")
    print("\nEnter function f(x) in LaTeX format (e.g., x^2 - 4):")
    f_expr = input("f(x) = ")
    print("\nEnter derivative f'(x) in LaTeX format (e.g., 2x):")
    df_expr = input("f'(x) = ")
    print("\nEnter initial guess x_0 (can use \\frac{a}{b} for fractions):")
    x0_expr = input("x_0 = ")
    
    try:
        x0_expr = latex_to_python(x0_expr)
        x0 = float(eval(x0_expr, {"math": math}))
    except Exception as e:
        raise ValueError(f"Invalid initial guess. Use LaTeX format (e.g., \\frac{{1}}{{2}} for 1/2): {str(e)}")
    
    f = create_function(f_expr)
    df = create_function(df_expr)
    return f, df, x0

if __name__ == "__main__":
    try:
        print("\nNewton-Raphson Method for Root Finding")
        print("=====================================")
        f, df, x0 = get_user_input()
        result = newton_method(f, df, x0)
        print(f"\nRoot found: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")