def Prime_factorization(the_Number):
    divisor = 2
    factors = []
    while divisor <= the_Number:
        if the_Number % divisor == 0:
            factors.append(divisor)
            the_Number = the_Number // divisor
        else:
            divisor += 1
    return factors


if __name__ == "__main__":
    number = int(input("Enter the Number: "))
    result = Prime_factorization(number)
    result_to_string = ",".join(map(str, result))
    is_prime = not result

    if is_prime:
        print(f"{number} is a Prime Number")
    elif result:
        print(f"Prime Factors: {result_to_string}")
    else:
        print("Invalid Input")
