# Factorial using loops
def factorial_with_loop(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def factorial_with_recursion(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_with_recursion(n - 1)


def main():
    try:
        n = int(input("Enter a non-negative integer to find its factorial: "))

        result_loop = factorial_with_loop(n)
        print(f"Factorial using loop: {result_loop}")

        result_recursion = factorial_with_recursion(n)
        print(f"Factorial using recursion: {result_recursion}")

    except ValueError:
        print("Please enter a valid non-negative integer.")


if __name__ == "__main__":
    main()
