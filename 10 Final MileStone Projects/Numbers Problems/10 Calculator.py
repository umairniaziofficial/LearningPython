import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


def power(x, y):
    return x**y


def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Cannot calculate square root of a negative number"


def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def tan(x):
    return math.tan(math.radians(x))


def calculator():
    print("Simple/Scientific Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("0. Exit")

    choice = input("Enter choice (0-9): ")

    if choice == "0":
        print("Exiting the calculator.")
        return

    if choice in ("1", "2", "3", "4", "5"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    elif choice in ("6", "7", "8", "9"):
        num1 = float(input("Enter the number: "))
    else:
        print("Invalid input. Please enter a number between 0 and 9.")
        return

    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == "4":
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == "5":
        print(num1, "^", num2, "=", power(num1, num2))
    elif choice == "6":
        print("Square root of", num1, "=", square_root(num1))
    elif choice == "7":
        print("Sine of", num1, "degrees =", sin(num1))
    elif choice == "8":
        print("Cosine of", num1, "degrees =", cos(num1))
    elif choice == "9":
        print("Tangent of", num1, "degrees =", tan(num1))

    calculator()


calculator()
