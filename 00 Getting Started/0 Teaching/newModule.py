# Find PI to the Nth Digit - Enter a number and have the program generate Tt (pi) up to that many decimal places.
# Keep a limit to how far the program will go.

from mpmath import mp


def Pi_Value(nthValue):
    mp.dps = nthValue + 2
    pi_value = mp.pi
    return str(pi_value)[:-1]


if __name__ == "__main__":
    try:
        nth_digit = int(input("Enter The Nth Digit YOu Want: "))
        if nth_digit < 1000:
            ans = Pi_Value(nth_digit)
            print(ans)
        else:
            print("Invalid Input")
    except ValueError:
        print("Error Occurred! Erro is Value Error ")
    except:
        print("other Error")
1
