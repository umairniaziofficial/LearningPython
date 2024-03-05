# Find PI to the Nth Digit - Enter a number and have the program generate Tt (pi) up to that many decimal places.
# Keep a limit to how far the program will go.

from mpmath import mp
import os


def Pi_to_Nth_digit(decimal_points):
    mp.dps = decimal_points + 2
    pi_value = mp.pi
    return str(pi_value)[:-1]


if __name__ == "__main__":
    os.system("cls")
    decimalPoints = int(input("Decimal points Values of PI you Want: "))
    try:
        if 1000 < decimalPoints:
            print("Invalid Input!")
            print("Sorry, the program has a limit of 1000 decimal places.")
        else:
            result = Pi_to_Nth_digit(decimalPoints)
            print(f"Pi up to {decimalPoints} decimal places:\n{result}")
    except ValueError:
        print("Please enter a valid integer for the number of decimal places.")
