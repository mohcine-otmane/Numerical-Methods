import math
import re

def latex_to_python(expr):
    expr = re.sub(r'\((.*?)\)\^(\d+)', r'(\1)**\2', expr)
    expr = re.sub(r'\\frac{(.*?)}{(.*?)}', r'(\1)/(\2)', expr)
    expr = re.sub(r'\\sqrt{(.*?)}', r'math.sqrt(\1)', expr)
    expr = re.sub(r'(\w+)\^(\d+)', r'\1**\2', expr)
    expr = re.sub(r'\\[a-zA-Z]+{(.*?)}', r'\1', expr)
    return expr

def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1) < tol:
            return x1
        if fx1 - fx0 == 0:
            raise ValueError("Division by zero error, try different initial points")
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x_new
    raise RuntimeError(f"Failed to converge after {max_iter} iterations")

def create_function(expression):
    expression = latex_to_python(expression)
    return lambda x: eval(expression, {"x": x, "math": math})

def get_user_input():
    print("\nSecant Method")
    print("For a function f(x), the method uses iteration formula:")
    print("x_{n+1} = x_n - f(x_n)\\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}")
    print("\nEnter function f(x) in LaTeX format (e.g., x^2 - 4):")
    f_expr = input("f(x) = ")
    print("\nEnter first initial guess x_0 (can use \\frac{a}{b} for fractions):")
    x0_expr = input("x_0 = ")
    print("\nEnter second initial guess x_1 (can use \\frac{a}{b} for fractions):")
    x1_expr = input("x_1 = ")
    
    try:
        x0_expr = latex_to_python(x0_expr)
        x1_expr = latex_to_python(x1_expr)
        x0 = float(eval(x0_expr, {"math": math}))
        x1 = float(eval(x1_expr, {"math": math}))
    except Exception as e:
        raise ValueError(f"Invalid initial guess. Use LaTeX format (e.g., \\frac{{1}}{{2}} for 1/2): {str(e)}")
    
    f = create_function(f_expr)
    return f, x0, x1

if __name__ == "__main__":
    try:
        print("\nSecant Method for Root Finding")
        print("============================")
        f, x0, x1 = get_user_input()
        result = secant_method(f, x0, x1)
        print(f"\nRoot found: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")