from mpmath import mp


def e_to_nth(decimal_digit):
    mp.dps = decimal_digit + 2
    e_value = mp.e
    return str(e_value)[:-1]


if __name__ == "__main__":
    nth_digit = int(input("Enter your Nth Digit: "))
    try:
        if nth_digit > 1000:
            print("Input Must be 1-1000")
            print("Invalid Input")
        else:
            result = e_to_nth(nth_digit)
            print(f"Value of e to {nth_digit} nth digit is: {result}")
    except ValueError:
        print("Error! Value Error Because the Value is Invalid")
