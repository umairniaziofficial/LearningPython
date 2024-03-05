def FindExponent(base, expo):
    result = 1
    while expo > 0:
        if expo % 2 == 1:
            result = result * base
        base = base * base
        expo = expo // 2
    return result

number, exponent = map(int, input("Enter the Number and Exponent: ").split())

result = FindExponent(number, exponent)
print(f"The Result: {result}")
