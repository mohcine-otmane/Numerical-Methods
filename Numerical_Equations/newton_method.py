import math

def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivative error, make sure it is not zero")
        x = x - fx/dfx
    raise RuntimeError(f"Failed to converge after {max_iter} iterations, make sure theoretically that it converges")

def create_function(expression):
    return lambda x: eval(expression, {"x": x, "math": math})

def get_user_input():
    print("\nEnter function f(x) (use x as variable, like this x**2 - 4):")
    f_expr = input("f(x) = ")
    print("\nEnter derivative df/dx (like this, 2*x):")
    df_expr = input("df/dx = ")
    print("\nEnter initial guess x0:")
    x0 = float(input("x0 = "))
    
    f = create_function(f_expr)
    df = create_function(df_expr)
    return f, df, x0

if __name__ == "__main__":
    try:
        f, df, x0 = get_user_input()
        result = newton_method(f, df, x0)
        print(f"\nRoot found: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")