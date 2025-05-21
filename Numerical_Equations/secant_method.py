import math

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
    raise RuntimeError(f"Failed to converge after {max_iter} iterations, make sure theoretically that it converges")

def create_function(expression):
    return lambda x: eval(expression, {"x": x, "math": math})

def get_user_input():
    print("\nEnter function f(x) (use x as variable, like this x**2 - 4):")
    f_expr = input("f(x) = ")
    print("\nEnter first initial guess x0:")
    x0 = float(input("x0 = "))
    print("\nEnter second initial guess x1:")
    x1 = float(input("x1 = "))
    
    f = create_function(f_expr)
    return f, x0, x1

if __name__ == "__main__":
    try:
        f, x0, x1 = get_user_input()
        result = secant_method(f, x0, x1)
        print(f"\nRoot found: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")