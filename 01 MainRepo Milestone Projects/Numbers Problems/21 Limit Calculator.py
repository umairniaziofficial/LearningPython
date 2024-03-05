from sympy import symbols, limit, oo


def limit_calculator():
    expression_str = input("Enter the function f(x): ")
    x = symbols("x")
    expression = eval(expression_str)

    limit_value_str = input("Enter the limit value (or 'oo' for infinity): ")

    if limit_value_str.lower() == "oo":
        limit_value = oo
    else:
        limit_value = float(limit_value_str)

    result = limit(expression, x, limit_value)

    print(
        f"The limit of {expression_str} as x approaches {limit_value_str} is: {result}"
    )


limit_calculator()
