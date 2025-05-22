import math
import re

def latex_to_python(expr):
    expr = expr.strip()
    expr = re.sub(r'\((.*?)\)\^(\d+)', r'(\1)**\2', expr)
    expr = re.sub(r'\\frac{(.*?)}{(.*?)}', r'(\1)/(\2)', expr)
    expr = re.sub(r'\\sqrt{(.*?)}', r'math.sqrt(\1)', expr)
    expr = re.sub(r'(\d+)x', r'\1*x', expr)
    expr = re.sub(r'x\^(\d+)', r'x**\1', expr)
    expr = re.sub(r'\\[a-zA-Z]+{(.*?)}', r'\1', expr)
    return expr

def create_function(expression):
    expression = latex_to_python(expression)
    return lambda x: eval(expression, {"x": x, "math": math})
