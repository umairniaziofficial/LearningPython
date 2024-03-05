from mpmath import mp


def VALUE_OF_PI(decimal_points):
    mp.dps = decimal_points + 2
    pi_value = mp.pi
    return str(pi_value)[:-1]


precious = int(input("Enter the number of Preciouse YOu want: "))
ans = VALUE_OF_PI(precious)
print(f"Ans is : {ans}")
